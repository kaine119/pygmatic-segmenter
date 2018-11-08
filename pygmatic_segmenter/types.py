# -*- coding: utf-8 -*-
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
        processed_string = self
        for rule in flatten(rules, Rule):
            processed_string = re.sub(rule.pattern, rule.replacement, self)
        return Text(processed_string)

# HACK: Some of the regexes don't have the \A cases; need to test if this affects anything
class List:
    """This class searches for a list within a string and adds 
    newlines before each list item."""
    ROMAN_NUMERALS = "i ii iii iv v vi vii viii ix x xi xii xiii xiv x xi xii xiii xv xvi xvii xviii xix xx".split(" ")
    LATIN_NUMERALS = list(ascii_lowercase)

    # Rubular: http://rubular.com/r/XcpaJKH0sz
    # HACK: missing \A
    ALPHABETICAL_LIST_WITH_PERIODS = r"(?<=^)[a-z](?=\.)|(?<=\s)[a-z](?=\.)"

    # Rubular: http://rubular.com/r/Gu5rQapywf
    # the (?i) at the end represents the case-insensitive flag (i.e. /pattern/i)
    # HACK: missing \A
    ALPHABETICAL_LIST_WITH_PARENS = r"(?<=\()[a-z]+(?=\))|(?<=^)[a-z]+(?=\))|(?<=\s)[a-z]+(?=\))(?i)"

    SubstituteListPeriodRule = Rule(r"♨", '∯')
    ListMarkerRule = Rule(r"☝", '')

    # Rubular: http://rubular.com/r/Wv4qLdoPx7
    SpaceBetweenListItemsFirstRule = Rule(r"(?<=\S\S|^)\s(?=\S\s*\d{1,2}♨)", "\r")

    # Rubular: http://rubular.com/r/AizHXC6HxK
    SpaceBetweenListItemsSecondRule = Rule(r"(?<=\S\S|^)\s(?=\d{1,2}♨)", "\r")

    # Rubular: http://rubular.com/r/GE5q6yID2j
    SpaceBetweenListItemsThirdRule = Rule(r"(?<=\S\S|^)\s(?=\d{1,2}☝)", "\r")

    NUMBERED_LIST_REGEX_1 = r"\s\d{1,2}(?=\.\s)|^\d{1,2}(?=\.\s)|\s\d{1,2}(?=\.\))|^\d{1,2}(?=\.\))|(?<=\s\-)\d{1,2}(?=\.\s)|(?<=^\-)\d{1,2}(?=\.\s)|(?<=\s\⁃)\d{1,2}(?=\.\s)|(?<=^\⁃)\d{1,2}(?=\.\s)|(?<=s\-)\d{1,2}(?=\.\))|(?<=^\-)\d{1,2}(?=\.\))|(?<=\s\⁃)\d{1,2}(?=\.\))|(?<=^\⁃)\d{1,2}(?=\.\))"
    
    NUMBERED_LIST_REGEX_2 = r"(?<=\s)\d{1,2}\.(?=\s)|^\d{1,2}\.(?=\s)|(?<=\s)\d{1,2}\.(?=\))|^\d{1,2}\.(?=\))|(?<=\s\-)\d{1,2}\.(?=\s)|(?<=^\-)\d{1,2}\.(?=\s)|(?<=\s\⁃)\d{1,2}\.(?=\s)|(?<=^\⁃)\d{1,2}\.(?=\s)|(?<=\s\-)\d{1,2}\.(?=\))|(?<=^\-)\d{1,2}\.(?=\))|(?<=\s\⁃)\d{1,2}\.(?=\))|(?<=^\⁃)\d{1,2}\.(?=\))"
    
    NUMBERED_LIST_PARENS_REGEX = r"\d{1,2}(?=\)\s)"

    # Rubular: http://rubular.com/r/NsNFSqrNvJ
    EXTRACT_ALPHABETICAL_LIST_LETTERS_REGEX = r"\([a-z]+(?=\))|(?<=^)[a-z]+(?=\))|(?<=\A)[a-z]+(?=\))|(?<=\s)[a-z]+(?=\))(?i)"

    # Rubular: http://rubular.com/r/wMpnVedEIb
    ALPHABETICAL_LIST_LETTERS_AND_PERIODS_REGEX = r"(?<=^)[a-z]\.|(?<=\A)[a-z]\.|(?<=\s)[a-z]\.(?i)"

    # Rubular: http://rubular.com/r/GcnmQt4a3I
    ROMAN_NUMERALS_IN_PARENTHESES = r"\(((?=[mdclxvi])m*(c[md]|d?c*)(x[cl]|l?x*)(i[xv]|v?i*))\)(?=\s[A-Z])"

    def __init__(self, text):
        self.text = Text(text)

    def add_line_break(self):
        self.format_alphabetical_lists()
        self.format_roman_numeral_lists()
        self.format_numbered_list_with_periods()
        return self.format_numbered_list_with_parens()

    def replace_parens(self):
        re.sub(ROMAN_NUMERALS_IN_PARENTHESES, r"&✂&\1&⌬&", self.text)
        return self.text

    def format_numbered_list_with_parens(self):
        self.replace_parens_in_numbered_list()
        self.add_line_breaks_for_numbered_list_with_parens()
        return self.text.apply(self.ListMarkerRule)

    def format_numbered_list_with_periods(self):
        self.replace_periods_in_numbered_list()
        self.add_line_breaks_for_numbered_list_with_periods()
        self.text = self.text.apply(self.SubstituteListPeriodRule)

    def format_alphabetical_lists(self):
        self.add_line_breaks_for_alphabetical_list_with_periods(roman_numeral = False)
        self.add_line_breaks_for_alphabetical_list_with_parens(roman_numeral = False)

    def format_roman_numeral_lists(self):
        self.add_line_breaks_for_alphabetical_list_with_periods(roman_numeral = True)
        self.add_line_breaks_for_alphabetical_list_with_parens(roman_numeral = True)

    def replace_periods_in_numbered_list(self):
        self.scan_lists(self.NUMBERED_LIST_REGEX_1, self.NUMBERED_LIST_REGEX_2, '♨', strip = True)

    def add_line_breaks_for_numbered_list_with_periods(self):
        if '♨' in self.text and (not re.match(r"♨.+\n.+♨|♨.+\r.+♨/ && @text !~ /for\s\d{1,2}♨\s[a-z]", self.text)):
            self.text.apply(SpaceBetweenListItemsFirstRule, SpaceBetweenListItemsSecondRule)

    def replace_parens_in_numbered_list(self):
        self.scan_lists(self.NUMBERED_LIST_PARENS_REGEX, self.NUMBERED_LIST_PARENS_REGEX, '☝')
        self.scan_lists(self.NUMBERED_LIST_PARENS_REGEX, self.NUMBERED_LIST_PARENS_REGEX, '☝')

    def add_line_breaks_for_numbered_list_with_parens(self):
        if '☝' in self.text and (not re.match(r"☝.+\n.+☝|☝.+\r.+☝", self.text)):
            self.text.apply(SpaceBetweenListItemsThirdRule)

    def scan_lists(self, regex1, regex2, replacement, strip = False):
        list_array = [int(i) for i in re.findall(regex1, self.text)]

        for a, i in enumerate(list_array):
            if ( a + 1 == list_array[i + 1] or a - 1 == (list_array[i - 1]) or
                (a == 0 and list_array[i - 1] == 9) or (a == 9 and list_array[i + 1] == 0) ):
                continue
            substitute_found_list_items(regex2, a, strip, replacement)


    def substitute_found_list_items(self, regex, a, strip, replacement):
        def handle_results(match):
            match = match.group()
            if str(a) == (match.strip() if strip else match):
                return "\r{}".format(re.escape(str(a)))
            else:
                return match

        self.text = re.sub(regex, handle_results, self.text)

    def add_line_breaks_for_alphabetical_list_with_periods(self, roman_numeral = False):
        self.iterate_alphabet_array(self.ALPHABETICAL_LIST_WITH_PERIODS, roman_numeral =  roman_numeral)

    def add_line_breaks_for_alphabetical_list_with_parens(self, roman_numeral = False):
        self.iterate_alphabet_array(self.ALPHABETICAL_LIST_WITH_PARENS,
            parens = True,
            roman_numeral = roman_numeral)

    def replace_alphabet_list(self, a):
        handle_results = lambda m: "\r{}∯".format(re.escape(str(a))) if a == m.group().rstrip('.') else m.group()
        self.text = re.sub(self.ALPHABETICAL_LIST_LETTERS_AND_PERIODS_REGEX, handle_results, self.text)
        return self.text

    def replace_alphabet_list_parens(self, a):
        def handle_results(m):
            m = m.group()
            if '(' in m:
                return "r&✂&{}".format(re.escape(m.replace("(", ""))) if a == m.lower().replace('/', '') else m
        self.text = re.sub(self.EXTRACT_ALPHABETICAL_LIST_LETTERS_REGEX, handle_results, self.text)
        return self.text

    def replace_correct_alphabet_list(self, a, parens):
        if parens:
            return self.replace_alphabet_list_parens(a)
        else:
            return self.replace_alphabet_list(a)

    def last_array_item_replacement(self, a, i, alphabet, list_array, parens):
        if ( (not set(alphabet).intersection(list_array)) or
                    (not list_array[i - 1] in alphabet) or
                    (not a in alphabet) ):
            return
        if abs(alphabet.index(list_array[i - 1]) - alphabet.index(a)) != 1:
            return

        self.replace_correct_alphabet_list(a, parens)


    def other_items_replacement(self, a, i, alphabet, list_array, parens):
        if ( (not set(alphabet).intersection(list_array)) or
                (not list_array[i - 1] in alphabet) or
                (not list_array[i + 1] in alphabet) or
                (not a in alphabet) ):
            return
        if ( (alphabet.index(list_array[i + 1]) - alphabet.index(a)) != 1 and
            abs(alphabet.index(list_array[i - 1]) - alphabet_index(a)) != 1 ):
            return

        self.replace_correct_alphabet_list(a, parens) 


    def iterate_alphabet_array(self, regex, parens = False, roman_numeral = False):
        list_array = [ n.lower() for n in re.findall(regex, self.text) ]
        alphabet = self.ROMAN_NUMERALS if roman_numeral else self.LATIN_NUMERALS
        list_array = [ i for i in list_array if any(i in a for a in alphabet) ]
        for i, a in enumerate(list_array):
            if i == len(list_array) - 1:
                return self.last_array_item_replacement(a, i, alphabet, list_array, parens)
            else:
                return self.other_items_replacement(a, i, alphabet, list_array, parens)
