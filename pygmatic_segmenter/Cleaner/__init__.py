from pygmatic_segmenter.Cleaner import Rules
from pygmatic_segmenter.types import Text
from pygmatic_segmenter.languages import Common
import re

class Cleaner():
    """An opinionated class that removes errant newlines, xhtml, inline formatting, etc."""
    def __init__(self, text, doc_type = None, language = Common):
        """ 
        Clean text of unwanted formatting.

        Example:
            >> text = "This is a sentence\ncut off in the middle because pdf."
            >> PragmaticSegmenter::Cleaner(text: text).clean
            "This is a sentence cut off in the middle because pdf."

        :param text: string representing text to clean
        :param language: optional two-character ISO 639-1 language code (e.g. 'en')
        :param doc_type: optional e.g. 'pdf'
        """
        super(Cleaner, self).__init__()
        self.text = Text(text)
        self.doc_type = doc_type
        self.language = language

    def clean(self):
        if not self.text: return
        self.remove_all_newlines()
        self.replace_double_newlines()
        self.replace_newlines()
        self.replace_escaped_newlines()

        self.text = self.text.apply(Rules.HTML.All)

        self.replace_punctuation_in_brackets()
        self.text = self.text.apply(Rules.InlineFormattingRule)
        self.clean_quotations()
        self.clean_table_of_contents()
        self.check_for_no_space_in_between_sentences()
        self.clean_consecutive_characters()
        return self.text

    def abbreviations(self):
        return self.language.Abbreviation.ABBREVIATIONS

    def check_for_no_space_in_between_sentences(self):
        words = self.text.split(' ')
        for word in words:
            self.search_for_connected_sentences(word, Rules.NO_SPACE_BETWEEN_SENTENCES_REGEX, Rules.NoSpaceBetweenSentencesRule)
            self.search_for_connected_sentences(word, Rules.NO_SPACE_BETWEEN_SENTENCES_DIGIT_REGEX, Rules.NoSpaceBetweenSentencesDigitRule)
        return self.text

    def replace_punctuation_in_brackets(self):
        def handle_match(match):
            return re.sub(r"\?", '&ᓷ&', match.group())

        self.text = Text(re.sub(r"\[(?:[^\]])*\]", handle_match, self.text))

    def search_for_connected_sentences(self, word, regex, rule):
        word = Text(word)
        if re.match(regex, word):
            if not [web for web in Rules.URL_EMAIL_KEYWORDS if re.match(web, word)]:
                if not [abbr for abbr in Rules.URL_EMAIL_KEYWORDS if re.match(abbr, word)]:
                    new_word = word.apply(rule)
                    self.text = Text(self.text.replace(word, new_word))

    def remove_all_newlines(self):
        self.remove_newline_in_middle_of_sentence()
        self.remove_newline_in_middle_of_word()

    def remove_newline_in_middle_of_sentence(self):
        def handle_matches(match):
            return re.sub(Rules.NEWLINE_IN_MIDDLE_OF_SENTENCE_REGEX, '', match.group())
        self.text = Text(re.sub(r"(?:[^\.])*", handle_matches, self.text))

    def remove_newline_in_middle_of_word(self):
        self.text = self.text.apply(Rules.NewLineInMiddleOfWordRule)

    def replace_escaped_newlines(self):
        self.text = self.text.apply(Rules.EscapedNewLineRule, Rules.EscapedCarriageReturnRule, 
                            Rules.TypoEscapedNewLineRule, Rules.TypoEscapedCarriageReturnRule)

    def replace_double_newlines(self):
        self.text = self.text.apply(Rules.DoubleNewLineWithSpaceRule, Rules.DoubleNewLineRule)

    def replace_newlines(self):
        if self.doc_type == 'pdf':
            self.remove_pdf_line_breaks()
        else:
            self.text = self.text.apply(Rules.NewLineFollowedByPeriodRule, Rules.ReplaceNewlineWithCarriageReturnRule)

    def remove_pdf_line_breaks(self):
        self.text = self.text.apply(Rules.NewLineFollowedByBulletRule,
                                Rules.PDF.NewLineInMiddleOfSentenceRule,
                                Rules.PDF.NewLineInMiddleOfSentenceNoSpacesRule)

    def clean_quotations(self):
        self.text = self.text.apply(Rules.QuotationsFirstRule, Rules.QuotationsSecondRule)

    def clean_table_of_contents(self):
        self.text = self.text.apply(Rules.TableOfContentsRule, Rules.ConsecutivePeriodsRule,
                                Rules.ConsecutiveForwardSlashRule)

    def clean_consecutive_characters(self):
        self.text = self.text.apply(Rules.ConsecutivePeriodsRule, Rules.ConsecutiveForwardSlashRule)
