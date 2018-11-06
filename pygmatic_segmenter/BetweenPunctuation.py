from pygmatic_segmenter.PunctuationReplacer import PunctuationReplacer
import re

class BetweenPunctuation:
    # TODO: regexes with ?< don't work at all
    ## Either find another regex engine or change the regex

    # Rubular: http://rubular.com/r/2YFrKWQUYi
    # BETWEEN_SINGLE_QUOTES_REGEX = r"(?<=\s)'(?:[^']|'[a-zA-Z])*'"
    BETWEEN_SINGLE_QUOTES_REGEX = r"(\s)'(?:[^']|'[a-zA-Z])*'"

    # BETWEEN_SINGLE_QUOTE_SLANTED_REGEX = r"(?<=\s)‘(?:[^’]|’[a-zA-Z])*’"
    BETWEEN_SINGLE_QUOTE_SLANTED_REGEX = r"(\s)‘(?:[^’]|’[a-zA-Z])*’"

    # Rubular: http://rubular.com/r/3Pw1QlXOjd
    # BETWEEN_DOUBLE_QUOTES_REGEX = r'(?>[^"\\]+|\\{2}|\\.)*"'
    BETWEEN_DOUBLE_QUOTES_REGEX = r'([^"\\]+|\\{2}|\\.)*"'

    # Rubular: http://rubular.com/r/x6s4PZK8jc
    # BETWEEN_QUOTE_ARROW_REGEX = r"«(?>[^»\\]+|\\{2}|\\.)*»"
    BETWEEN_QUOTE_ARROW_REGEX = r"«([^»\\]+|\\{2}|\\.)*»"

    # Rubular: http://rubular.com/r/JbAIpKdlSq
    # BETWEEN_QUOTE_SLANTED_REGEX = r"“(?>[^”\\]+|\\{2}|\\.)*”"
    BETWEEN_QUOTE_SLANTED_REGEX = r"“([^”\\]+|\\{2}|\\.)*”"

    # Rubular: http://rubular.com/r/WX4AvnZvlX
    # BETWEEN_SQUARE_BRACKETS_REGEX = r"\[(?>[^\]\\]+|\\{2}|\\.)*\]"
    BETWEEN_SQUARE_BRACKETS_REGEX = r"\[([^\]\\]+|\\{2}|\\.)*\]"

    # Rubular: http://rubular.com/r/6tTityPflI
    # BETWEEN_PARENS_REGEX = r"\((?>[^\(\)\\]+|\\{2}|\\.)*\)"
    BETWEEN_PARENS_REGEX = r"\(([^\(\)\\]+|\\{2}|\\.)*\)"

    # Rubular: http://rubular.com/r/mXf8cW025o
    # WORD_WITH_LEADING_APOSTROPHE = r"(?<=\s)'(?:[^']|'[a-zA-Z])*'\S"
    WORD_WITH_LEADING_APOSTROPHE = r"(=\s)'(?:[^']|'[a-zA-Z])*'\S"

    # Rubular: http://rubular.com/r/jTtDKfjxzr
    # BETWEEN_EM_DASHES_REGEX = r"\-\-(?>[^\-\-])*\-\-"
    BETWEEN_EM_DASHES_REGEX = r"\-\-([^\-\-])*\-\-"

    def __init__(self, text):
        self.text = text

    def replace(self):
        self.sub_punctuation_between_quotes_and_parens(self.text)

    def sub_punctuation_between_quotes_and_parens(self, txt):
        self.sub_punctuation_between_single_quotes(txt)
        self.sub_punctuation_between_single_quote_slanted(txt)
        self.sub_punctuation_between_double_quotes(txt)
        self.sub_punctuation_between_square_brackets(txt)
        self.sub_punctuation_between_parens(txt)
        self.sub_punctuation_between_quotes_arrow(txt)
        self.sub_punctuation_between_em_dashes(txt)
        self.sub_punctuation_between_quotes_slanted(txt)

    def sub_punctuation_between_parens(self, txt):
        PunctuationReplacer(matches_array = re.findall(self.BETWEEN_PARENS_REGEX, txt), text = txt).replace()

    def sub_punctuation_between_square_brackets(self, txt):
        PunctuationReplacer(matches_array = re.findall(self.BETWEEN_SQUARE_BRACKETS_REGEX, txt), text = txt).replace()

    def sub_punctuation_between_single_quotes(self, txt):
        if not (re.match(self.WORD_WITH_LEADING_APOSTROPHE, txt) and not re.match(r"/'\s", txt)):
            PunctuationReplacer(matches_array = re.findall(self.BETWEEN_SINGLE_QUOTES_REGEX, txt), text = txt).replace()

    def sub_punctuation_between_single_quote_slanted(self, txt):
        PunctuationReplacer(matches_array = re.findall(self.BETWEEN_SINGLE_QUOTE_SLANTED_REGEX, txt), text = txt).replace()

    def sub_punctuation_between_double_quotes(self, txt):
        PunctuationReplacer(matches_array = re.findall(self.BETWEEN_DOUBLE_QUOTES_REGEX, txt), text = txt).replace()

    def sub_punctuation_between_quotes_arrow(self, txt):
        PunctuationReplacer(matches_array = re.findall(self.BETWEEN_QUOTE_ARROW_REGEX, txt), text = txt).replace()

    def sub_punctuation_between_em_dashes(self, txt):
        PunctuationReplacer(matches_array = re.findall(self.BETWEEN_EM_DASHES_REGEX, txt), text = txt).replace()

    def sub_punctuation_between_quotes_slanted(self, txt):
        PunctuationReplacer(matches_array = re.findall(self.BETWEEN_QUOTE_SLANTED_REGEX, txt), text = txt).replace()