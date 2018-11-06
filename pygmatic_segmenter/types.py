"""Types used to declare rules and apply them."""
from collections import namedtuple
import re
from string import ascii_lowercase # all letters a-z as a string

Rule = namedtuple("Rule", ["pattern", "replacement"])

def flatten(arr, type):
    """Flatten an array of type."""
    res = []
    for i in arr:
        if isinstance(i, type):
            res.append(i)
        else:
            res.extend(flatten(i, type))
    return res

class Text(str):
    """Extension of the base string class to include apply()"""
    
    def apply(self, *rules):
        """apply an arbitrarily nested set of rules, to the string
        and return a new instance of Text.
        This can be stacked, i.e. Text('abc').apply(...).apply(...)"""
        for rule in flatten(rules, Rule):
            processed_string = re.sub(rule.pattern, rule.replacement, self)
            return Text(processed_string)

# TODO: finish this class up
# class List:
#     """This class searches for a list within a string and adds 
#     newlines before each list item."""
#     ROMAN_NUMERALS = "i ii iii iv v vi vii viii ix x xi xii xiii xiv x xi xii xiii xv xvi xvii xviii xix xx".split(" ")
#     LATIN_NUMERALS = list(ascii_lowercase)

#     # Rubular: http://rubular.com/r/XcpaJKH0sz
#     ALPHABETICAL_LIST_WITH_PERIODS = r"(?<=^)[a-z](?=\.)|(?<=\A)[a-z](?=\.)|(?<=\s)[a-z](?=\.)"

#     # Rubular: http://rubular.com/r/Gu5rQapywf
#     # the (?i) at the end represents the case-insensitive flag (i.e. /pattern/i)
#     ALPHABETICAL_LIST_WITH_PARENS = r"(?<=\()[a-z]+(?=\))|(?<=^)[a-z]+(?=\))|(?<=\A)[a-z]+(?=\))|(?<=\s)[a-z]+(?=\))(?i)"

#     SubstituteListPeriodRule = Rule(r"♨", '∯')
#     ListMarkerRule = Rule(r"☝", '')

#     # Rubular: http://rubular.com/r/Wv4qLdoPx7
#     SpaceBetweenListItemsFirstRule = Rule(r"(?<=\S\S|^)\s(?=\S\s*\d{1,2}♨)", "\r")

#     # Rubular: http://rubular.com/r/AizHXC6HxK
#     SpaceBetweenListItemsSecondRule = Rule(r"(?<=\S\S|^)\s(?=\d{1,2}♨)", "\r")

#     # Rubular: http://rubular.com/r/GE5q6yID2j
#     SpaceBetweenListItemsThirdRule = Rule(r"(?<=\S\S|^)\s(?=\d{1,2}☝)", "\r")

#     NUMBERED_LIST_REGEX_1 = r"\s\d{1,2}(?=\.\s)|^\d{1,2}(?=\.\s)|\s\d{1,2}(?=\.\))|^\d{1,2}(?=\.\))|(?<=\s\-)\d{1,2}(?=\.\s)|(?<=^\-)\d{1,2}(?=\.\s)|(?<=\s\⁃)\d{1,2}(?=\.\s)|(?<=^\⁃)\d{1,2}(?=\.\s)|(?<=s\-)\d{1,2}(?=\.\))|(?<=^\-)\d{1,2}(?=\.\))|(?<=\s\⁃)\d{1,2}(?=\.\))|(?<=^\⁃)\d{1,2}(?=\.\))"
    
#     NUMBERED_LIST_REGEX_2 = r"(?<=\s)\d{1,2}\.(?=\s)|^\d{1,2}\.(?=\s)|(?<=\s)\d{1,2}\.(?=\))|^\d{1,2}\.(?=\))|(?<=\s\-)\d{1,2}\.(?=\s)|(?<=^\-)\d{1,2}\.(?=\s)|(?<=\s\⁃)\d{1,2}\.(?=\s)|(?<=^\⁃)\d{1,2}\.(?=\s)|(?<=\s\-)\d{1,2}\.(?=\))|(?<=^\-)\d{1,2}\.(?=\))|(?<=\s\⁃)\d{1,2}\.(?=\))|(?<=^\⁃)\d{1,2}\.(?=\))"
    
#     NUMBERED_LIST_PARENS_REGEX = r"\d{1,2}(?=\)\s)"

#     # Rubular: http://rubular.com/r/NsNFSqrNvJ
#     EXTRACT_ALPHABETICAL_LIST_LETTERS_REGEX = r"\([a-z]+(?=\))|(?<=^)[a-z]+(?=\))|(?<=\A)[a-z]+(?=\))|(?<=\s)[a-z]+(?=\))(?i)"

#     # Rubular: http://rubular.com/r/wMpnVedEIb
#     ALPHABETICAL_LIST_LETTERS_AND_PERIODS_REGEX = r"(?<=^)[a-z]\.|(?<=\A)[a-z]\.|(?<=\s)[a-z]\.(?i)"

#     # Rubular: http://rubular.com/r/GcnmQt4a3I
#     ROMAN_NUMERALS_IN_PARENTHESES = r"\(((?=[mdclxvi])m*(c[md]|d?c*)(x[cl]|l?x*)(i[xv]|v?i*))\)(?=\s[A-Z])"

#     def __init__(self, text):
#         self.text = text

#     def add_line_break(self):
#         self.format_alphabetical_lists()
#         self.format_roman_numeral_lists()
#         self.format_numbered_list_with_periods()
#         self.format_numbered_list_with_parens()

#     def replace_parens(self):
#         re.sub(ROMAN_NUMERALS_IN_PARENTHESES, r"&✂&\1&⌬&", self.text)
#         return self.text

#     def format_numbered_list_with_periods(self):
#         self.replace_periods_in_numbered_list()
#         self.add_line_breaks_for_numbered_list_with_periods()
#         self.text = self.text.apply(SubstituteListPeriodRule)

#     def format_alphabetical_lists(self):
#         self.add_line_breaks_for_alphabetical_list_with_periods(roman_numeral = false)
#         self.add_line_breaks_for_alphabetical_list_with_parens(roman_numeral = false)

#     def format_roman_numeral_lists(self):
#         self.add_line_breaks_for_alphabetical_list_with_periods(roman_numeral: true)
#         self.add_line_breaks_for_alphabetical_list_with_parens(roman_numeral: true)

#     def replace_periods_in_numbered_list(self):
#         self.scan_lists(NUMBERED_LIST_REGEX_1, NUMBERED_LIST_REGEX_2, '♨', strip: true)

#     def add_line_breaks_for_numbered_list_with_periods(self):
#         if '♨' in self.text and (not re.match(r"♨.+\n.+♨|♨.+\r.+♨/ && @text !~ /for\s\d{1,2}♨\s[a-z]", self.text)):
#             self.text.apply(SpaceBetweenListItemsFirstRule, SpaceBetweenListItemsSecondRule)

#     def replace_parens_in_numbered_list(self):
#         scan_lists(NUMBERED_LIST_PARENS_REGEX, NUMBERED_LIST_PARENS_REGEX, '☝')
#         scan_lists(NUMBERED_LIST_PARENS_REGEX, NUMBERED_LIST_PARENS_REGEX, '☝')

#     def add_line_breaks_for_numbered_list_with_parens(self):
#         if '☝' in self.text and (not re.match(r"☝.+\n.+☝|☝.+\r.+☝", self.text)):
#             self.text.apply(SpaceBetweenListItemsThirdRule)

#     def scan_lists(self, regex1, regex2, replacement, strip = false):
#         list_array = re.findall(regex1, self.text).map(&:to_i)

#         for a, i in enumerate(list_array):
#             if ( a + 1 == list_array[i + 1] or
#                  a - 1 == (list_array[i - 1]) or
#                 (a == 0 and list_array[i - 1] == 9) or
#                 (a == 9 and list_array[i + 1] == 0) ):
#                 continue
#             substitute_found_list_items(regex2, a, strip, replacement)

#     def substitute_found_list_items(self, regex, a, strip, replacement):
