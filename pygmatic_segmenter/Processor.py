from pygmatic_segmenter.languages import Common
from pygmatic_segmenter.types import Text, List, flatten
from pygmatic_segmenter import ExclamationWords
from pygmatic_segmenter import BetweenPunctuation
from pygmatic_segmenter import AbbreviationReplacer
import itertools # for map()
import re

class Processor:
    def __init__(self, language = Common):
        self.language = language
        
    def process(self, text):
        self.text = List(text = text).add_line_break()
        self.replace_abbreviations()
        self.replace_numbers()
        self.replace_continuous_punctuation()
        self.replace_periods_before_numeric_references()
        self.text = self.text.apply(self.language.Abbreviations.WithMultiplePeriodsAndEmailRule)\
                             .apply(self.language.GeoLocationRule)\
                             .apply(self.language.FileFormatRule)
        return self.split_into_segments()

    def split_into_segments(self):
        segments = self.check_for_parens_between_quotes(self.text).split("\r")
        segments = map(lambda seg: Text(seg), segments)

        segments = map(lambda seg: seg.apply(self.language.SingleNewLineRule,
                                                     self.language.EllipsisRules.All),
                       segments)
        segments = flatten(map(self.check_for_punctuation, segments), str)
        segments = map(lambda seg: seg.apply(self.language.SubSymbolsRules.All), segments)
        segments = map(lambda seg: seg.apply(self.language.SubSymbolsRules.Period), segments)
        segments = flatten(map(lambda seg: self.post_process_segments(seg), segments), str)
        segments = [seg for seg in segments if seg is not None]
        return list(map(lambda seg: seg.apply(self.language.SubSingleQuoteRule), segments))

    def post_process_segments(self, txt):
        # HACK: replaced \A and \Z with ^*, shouldn't affect anything
        if len(txt) < 2 and re.match(r"^[a-zA-Z]*$", txt):
            return txt
        if len(txt) < 2 or self.check_consecutive_underscore(txt):
            return

        txt = txt.apply(
            self.language.ExtraWhiteSpaceRule,
            self.language.ReinsertEllipsisRules.All
        )

        if re.match(self.language.QUOTATION_AT_END_OF_SENTENCE_REGEX, txt):
            return [Text(n) for n in re.split(self.language.SPLIT_SPACE_QUOTATION_AT_END_OF_SENTENCE_REGEX, txt)]
        else:
            return Text(txt.replace("\n", "").strip())

    def check_for_parens_between_quotes(self, txt):
        if not re.match(self.language.PARENS_BETWEEN_DOUBLE_QUOTES_REGEX, txt):
            return txt

        def handle_matches(match):
            first = re.sub(r"\s(?=\()", "\r", match)
            return re.sub(r"(?<=\))\s", "\r", first)

        return re.sub(self.language.PARENS_BETWEEN_DOUBLE_QUOTES_REGEX, handle_matches, txt)

    def replace_continuous_punctuation(self):
        def handle_matches(match):
            first = re.sub(r"!", "\r", match)
            return re.sub(r"\?", '&ᓷ&', first)

        self.text = re.sub(self.language.CONTINUOUS_PUNCTUATION_REGEX, handle_matches, self.text)

    def replace_periods_before_numeric_references(self):
        self.text = re.sub(self.language.NUMBERED_REFERENCE_REGEX, "∯\\2\r\\7", self.text)
        self.text = Text(self.text)

    def check_consecutive_underscore(self, txt):
        # Rubular: http://rubular.com/r/fTF2Ff3WBL
        return len(re.sub(r"_{3,}", '', txt)) == 0

    def check_for_punctuation(self, txt):
        if any(char in self.language.PUNCTUATIONS for char in txt):
            return self.process_text(txt)
        else:
            return txt

    def process_text(self, txt):
        if txt[-1] not in self.language.PUNCTUATIONS:
            txt += "ȸ"
        ExclamationWords.apply_rules(txt)
        self.between_punctuation(txt)
        txt = txt.apply(
            self.language.DoublePunctuationRules.All,
            self.language.QuestionMarkInQuotationRule,
            self.language.ExclamationPointRules.All
            )
        # TODO: enable next line after List class is done
        # txt = List(text = txt).replace_parens
        return self.sentence_boundary_punctuation(txt)

    def replace_numbers(self):
        self.text = self.text.apply(self.language.Numbers.All)
        return self.text


    def replace_abbreviations(self):
        try:
            abbreviations_replacer = self.language.AbbreviationReplacer.AbbreviationReplacer
        except AttributeError:
            abbreviations_replacer = AbbreviationReplacer.AbbreviationReplacer
        self.text = abbreviations_replacer(self.text, self.language).replace()

    def between_punctuation(self, txt):
        try:
            between_punctuation_processor = self.language.BetweenPunctuation
        except AttributeError:
            between_punctuation_processor = BetweenPunctuation
        self.text = between_punctuation_processor.BetweenPunctuation(txt).replace()


    def sentence_boundary_punctuation(self, txt):
        try:
            txt = txt.apply(self.language.ReplaceColonBetweenNumbersRule,
                            self.language.ReplaceNonSentenceBoundaryCommaRule)
        except AttributeError as e:
            pass # TODO: huh?

        return list(map(lambda x: Text(x), re.findall(self.language.SENTENCE_BOUNDARY_REGEX, txt)))
