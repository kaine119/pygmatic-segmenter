from pygmatic_segmenter.PunctuationReplacer import PunctuationReplacer
import re

class BetweenPunctuation:
    # The original regexes used atomic grouping (?>regexp), which aren't supported in Python
    # this  is used to emulate them: 
    # https://stackoverflow.com/a/13577411
    # (?=(?P<tmp>{regexp}))(?P=tmp)

    # Rubular: http://rubular.com/r/2YFrKWQUYi
    BETWEEN_SINGLE_QUOTES_REGEX = r"(?<=\s)'(?:[^']|'[a-zA-Z])*'"

    BETWEEN_SINGLE_QUOTE_SLANTED_REGEX = r"(?<=\s)‘(?:[^’]|’[a-zA-Z])*’"

    # Rubular: http://rubular.com/r/3Pw1QlXOjd
    # original was /(?>[^"\\]+|\\{2}|\\.)*"/
    BETWEEN_DOUBLE_QUOTES_REGEX = r'(?=(?P<tmp>[^"\\]+|\\{2}|\\.))(?P=tmp)*"'

    # Rubular: http://rubular.com/r/x6s4PZK8jc
    # original was /«(?>[^»\\]+|\\{2}|\\.)*/
    BETWEEN_QUOTE_ARROW_REGEX = r"«([^»\\]+|\\{2}|\\.)*»"

    # Rubular: http://rubular.com/r/JbAIpKdlSq
    # original was /“(?>[^”\\]+|\\{2}|\\.)*”/
    BETWEEN_QUOTE_SLANTED_REGEX = r"“(?=(?P<tmp>[^”\\]+|\\{2}|\\.))(?P=tmp)*”"


    # Rubular: http://rubular.com/r/WX4AvnZvlX
    # original was /\[(?>[^\]\\]+|\\{2}|\\.)*\]/
    BETWEEN_SQUARE_BRACKETS_REGEX = r"\[(?=(?P<tmp>[^\]\\]+|\\{2}|\\.))(?P=tmp)*\]"

    # Rubular: http://rubular.com/r/6tTityPflI
    # original was /\((?>[^\(\)\\]+|\\{2}|\\.)*\)/
    BETWEEN_PARENS_REGEX = r"\(([^\(\)\\]+|\\{2}|\\.)*\)"

    # Rubular: http://rubular.com/r/mXf8cW025o
    WORD_WITH_LEADING_APOSTROPHE = r"(?<=\s)'(?:[^']|'[a-zA-Z])*'\S"

    # Rubular: http://rubular.com/r/jTtDKfjxzr
    # original was /\-\-(?>[^\-\-])*\-\-/
    BETWEEN_EM_DASHES_REGEX = r"\-\-(?=(?P<tmp>[^\-\-]))(?P=tmp)*\-\-"

    def __init__(self, text):
        self.text = text

    def replace(self):
        self.sub_punctuation_between_quotes_and_parens()
        return self.text


    def sub_punctuation_between_quotes_and_parens(self):
        self.sub_punctuation_between_single_quotes()
        self.sub_punctuation_between_single_quote_slanted()
        self.sub_punctuation_between_double_quotes()
        self.sub_punctuation_between_square_brackets()
        self.sub_punctuation_between_parens()
        self.sub_punctuation_between_quotes_arrow()
        self.sub_punctuation_between_em_dashes()
        self.sub_punctuation_between_quotes_slanted()
        return self.text

    def sub_punctuation_between_parens(self):
        self.text = PunctuationReplacer(matches_array = re.findall(self.BETWEEN_PARENS_REGEX, self.text), text = self.text).replace()

    def sub_punctuation_between_square_brackets(self):
        self.text = PunctuationReplacer(matches_array = re.findall(self.BETWEEN_SQUARE_BRACKETS_REGEX, self.text), text = self.text).replace()

    def sub_punctuation_between_single_quotes(self):
        if not (re.search(self.WORD_WITH_LEADING_APOSTROPHE, self.text) and not re.search(r"/'\s", self.text)):
            self.text = PunctuationReplacer(matches_array = re.findall(self.BETWEEN_SINGLE_QUOTES_REGEX, self.text), text = self.text).replace()

    def sub_punctuation_between_single_quote_slanted(self):
        self.text = PunctuationReplacer(matches_array = re.findall(self.BETWEEN_SINGLE_QUOTE_SLANTED_REGEX, self.text), text = self.text).replace()

    def sub_punctuation_between_double_quotes(self):
        self.text = PunctuationReplacer(matches_array = re.findall(self.BETWEEN_DOUBLE_QUOTES_REGEX, self.text), text = self.text).replace()

    def sub_punctuation_between_quotes_arrow(self):
        self.text = PunctuationReplacer(matches_array = re.findall(self.BETWEEN_QUOTE_ARROW_REGEX, self.text), text = self.text).replace()

    def sub_punctuation_between_em_dashes(self):
        self.text = PunctuationReplacer(matches_array = re.findall(self.BETWEEN_EM_DASHES_REGEX, self.text), text = self.text).replace()

    def sub_punctuation_between_quotes_slanted(self):
        self.text = PunctuationReplacer(matches_array = re.findall(self.BETWEEN_QUOTE_SLANTED_REGEX, self.text), text = self.text).replace()