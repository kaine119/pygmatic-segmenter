from pygmatic_segmenter.types import Rule

class PunctuationReplacer():
    class Rules:
        class EscapeRegexReservedCharacters:
            LeftParen = Rule( '(', r'\(' )
            RightParen = Rule( ')', r'\)' )
            LeftBracket = Rule( '[', r'\[' )
            RightBracket = Rule( ']', r'\]' )
            Dash = Rule( '-', r'\-' )

            All = [ LeftParen, RightParen, LeftBracket, RightBracket, Dash ]

        class SubEscapedRegexReservedCharacters:
            SubLeftParen = Rule( r'\(', '(' )
            SubRightParen = Rule( r'\)', ')' )
            SubLeftBracket = Rule( r'\[', '[' )
            SubRightBracket = Rule( r'\]', ']' )
            SubDash = Rule( r'\-', '-' )

            All = [SubLeftParen, SubRightParen, SubLeftBracket, SubRightBracket, SubDash]

    def __init__(self, text, matches_array, match_type = None):
        self.text = text
        self.matches_array = matches_array
        self.match_type = match_type

    def replace(self):
        self.replace_punctuation(self.matches_array)

    def replace_punctuation(self, array):
        if not array or len(array) == 0:
            return

        self.text = self.text.apply(self.Rules.EscapeRegexReservedCharacters.All)

        for a in array:
            a = a.apply(Rules.EscapeRegexReservedCharacters.All)
            sub = sub_characters(a, '.', '∯')
            sub_1 = sub_characters(sub, '。', '&ᓰ&')
            sub_2 = sub_characters(sub_1, '．', '&ᓱ&')
            sub_3 = sub_characters(sub_2, '！', '&ᓳ&')
            sub_4 = sub_characters(sub_3, '!', '&ᓴ&')
            sub_5 = sub_characters(sub_4, '?', '&ᓷ&')
            sub_6 = sub_characters(sub_5, '？', '&ᓸ&')
            if match_type != "single":
                sub_7 = sub_characters(sub_6, "'", '&⎋&')

        self.text = self.text.apply(Rules.SubEscapedRegexReservedCharacters.All)

    def sub_characters(string, char_a, char_b):
        sub = re.sub(char_a, char_b, string)
        self.text = re.sub(re.escape(string), sub, self.text)
        return sub