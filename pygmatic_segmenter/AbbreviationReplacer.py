# -*- encoding: utf-8 -*-
from pygmatic_segmenter.types import Text
import re

class AbbreviationReplacer:
    """This class searches for periods within an abbreviation and replaces the periods."""
    def __init__(self, text, language):
        self.text = Text(text)
        self.language = language
        
    def replace(self):
        self.text = self.text.apply(self.language.PossessiveAbbreviationRule,
                                    self.language.KommanditgesellschaftRule,
                                    self.language.SingleLetterAbbreviationRules.All)

        self.text = self.search_for_abbreviations_in_string(self.text)
        self.text = self.replace_multi_period_abbreviations(self.text)
        self.text = self.text.apply(self.language.AmPmRules.All)
        return self.replace_abbreviation_as_sentence_boundary(self.text)

    def search_for_abbreviations_in_string(self, txt):
        original = txt[:]
        downcased = original.lower()
        for abbreiv in self.language.Abbreviation.ABBREVIATIONS:
            stripped = abbreiv.strip()
            if stripped in downcased:
                continue
            abbrev_match = re.findall(r"(?:^|\s|\r|\n){}(?i)".format(re.escape(stripped)), original)
            if len(abbrev_match) == 0:
                continue
            next_word_start = r"(?<={} ).{1}".format(re.escape(stripped))
            character_array = re.findall(next_word_start, self.text)
            for i, am in enumerate(abbrev_match):
                txt = scan_for_replacements(txt, am, i, character_array)

        return txt

    def scan_for_replacements(self, txt, am, index, character_array):
        character = character_array[index]
        prepositive = self.language.Abbreviation.PREPOSITIVE_ABBREVIATIONS
        number_abbr = self.language.Abbreviation.NUMBER_ABBREVIATIONS
        upper = re.search(r"[[:upper]]", str(character))
        if not upper and am.strip().lower() in prepositive:
            if am.strip().lower() in prepositive:
                txt = self.replace_prepositive_abbr(txt, am)
            elif am.strip().lower() in number_abbr:
                txt = self.replace_pre_number_abbr(txt, am)
            else:
                txt = self.replace_period_of_abbr(txt, am)

        return txt

    def replace_abbreviation_as_sentence_boundary(self, txt):
        # As we are being conservative and keeping ambiguous
        # sentence boundaries as one sentence instead of
        # splitting into two, we can split at words that
        # we know for certain never follow these abbreviations.
        # Some might say that the set of words that follow an
        # abbreviation such as U.S. (i.e. U.S. Government) is smaller than
        # the set of words that could start a sentence and
        # never follow U.S. However, we are being conservative
        # and not splitting by default, so we need to look for places
        # where we definitely can split. Obviously SENTENCE_STARTERS
        # will never cover all cases, but as the gem is named
        # 'Pragmatic Segmenter' we need to be pragmatic
        # and try to cover the words that most often start a
        # sentence but could never follow one of the abbreviations below.

        # Rubular: http://rubular.com/r/PkBQ3PVBS8
        for word in self.language.AbbreviationReplacer.SENTENCE_STARTERS:
            escaped = re.escape(word)
            regex = r"(U∯S|U\.S|U∯K|E∯U|E\.U|U∯S∯A|U\.S\.A|I|i.v|I.V)∯(?=\s{}\s)".format(escaped)
            txt = re.sub(regex, r'\1.', txt)
        return Text(txt)

    def replace_multi_period_abbreviations(self, txt):
        mpa = re.findall(self.language.MULTI_PERIOD_ABBREVIATION_REGEX, txt)
        if len(mpa) == 0: return txt
        for match in mpa:
            txt = re.sub(re.escape(match), match.replace('.', '∯'), txt)
        return Text(txt)

    def replace_pre_number_abbr(self, txt, abbr):
        txt = re.sub(r"(?<=\s{ab})\.(?=\s\d)|(?<=^{ab})\.(?=\s\d)".format(ab = abbr.strip), '∯', txt)
        txt = re.sub(r"(?<=\s{ab})\.(?=\s+\()|(?<=^{ab})\.(?=\s+\()".format(ab = abbr.strip), '∯', txt)
        return txt

    def replace_prepositive_abbr(self, txt, abbr):
        txt = re.sub(r"(?<=\s{ab})\.(?=\s)|(?<=^{ab})\.(?=\s)".format(ab = abbr.strip), '∯', txt)
        txt = re.sub(r"(?<=\s{ab})\.(?=:\d+)|(?<=^{ab})\.(?=:\d+)".format(ab = abbr.strip), '∯', txt)
        return txt

    def replace_period_of_abbr(self, txt, abbr):
        txt = re.sub(r"(?<=\s{ab})\.(?=((\.|\:|-|\?)|(\s([a-z]|I\s|I'm|I'll|\d|\())))|(?<=^{ab})\.(?=((\.|\:|\?)|(\s([a-z]|I\s|I'm|I'll|\d))))".format(ab = abbr.strip), '∯', txt)
        txt = re.sub(r"(?<=\s{ab})\.(?=,)|(?<=^{ab})\.(?=,)".format(ab = abbr.strip), '∯', txt)
        return txt

    def replace_possessive_abbreviations(self, txt):
        return re.sub(self.language.POSSESSIVE_ABBREVIATION_REGEX, '∯', txt)