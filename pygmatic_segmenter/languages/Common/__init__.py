# import pygmatic_segmenter.languages.Common.numbers
# import pygmatic_segmenter.languages.Common.ellipsis

from pygmatic_segmenter.types import Rule

PUNCTUATIONS = ['。', '．', '.', '！', '!', '?', '？']

class Abbreviation:
    """Defines the abbreviations for each language (if available)"""
    ABBREVIATIONS = {'adj', 'adm', 'adv', 'al', 'ala', 'alta', 'apr', 'arc', 'ariz', 'ark', 'art', 'assn', 'asst', 'attys', 'aug', 'ave', 'bart', 'bld', 'bldg', 'blvd', 'brig', 'bros', 'btw', 'cal', 'calif', 'capt', 'cl', 'cmdr', 'co', 'col', 'colo', 'comdr', 'con', 'conn', 'corp', 'cpl', 'cres', 'ct', 'd.phil', 'dak', 'dec', 'del', 'dept', 'det', 'dist', 'dr', 'dr.phil', 'dr.philos', 'drs', 'e.g', 'ens', 'esp', 'esq', 'etc', 'exp', 'expy', 'ext', 'feb', 'fed', 'fla', 'ft', 'fwy', 'fy', 'ga', 'gen', 'gov', 'hon', 'hosp', 'hr', 'hway', 'hwy', 'i.e', 'ia', 'id', 'ida', 'ill', 'inc', 'ind', 'ing', 'insp', 'is', 'jan', 'jr', 'jul', 'jun', 'kan', 'kans', 'ken', 'ky', 'la', 'lt', 'ltd', 'maj', 'man', 'mar', 'mass', 'may', 'md', 'me', 'med', 'messrs', 'mex', 'mfg', 'mich', 'min', 'minn', 'miss', 'mlle', 'mm', 'mme', 'mo', 'mont', 'mr', 'mrs', 'ms', 'msgr', 'mssrs', 'mt', 'mtn', 'neb', 'nebr', 'nev', 'no', 'nos', 'nov', 'nr', 'oct', 'ok', 'okla', 'ont', 'op', 'ord', 'ore', 'p', 'pa', 'pd', 'pde', 'penn', 'penna', 'pfc', 'ph', 'ph.d', 'pl', 'plz', 'pp', 'prof', 'pvt', 'que', 'rd', 'rs', 'ref', 'rep', 'reps', 'res', 'rev', 'rt', 'sask', 'sec', 'sen', 'sens', 'sep', 'sept', 'sfc', 'sgt', 'sr', 'st', 'supt', 'surg', 'tce', 'tenn', 'tex', 'univ', 'usafa', 'u.s', 'ut', 'va', 'v', 'ver', 'viz', 'vs', 'vt', 'wash', 'wis', 'wisc', 'wy', 'wyo', 'yuk'}
    PREPOSITIVE_ABBREVIATIONS = {'adm', 'attys', 'brig', 'capt', 'cmdr', 'col', 'cpl', 'det', 'dr', 'gen', 'gov', 'ing', 'lt', 'maj', 'mr', 'mrs', 'ms', 'mt', 'messrs', 'mssrs', 'prof', 'ph', 'rep', 'reps', 'rev', 'sen', 'sens', 'sgt', 'st', 'supt', 'v', 'vs'}
    NUMBER_ABBREVIATIONS = {'art', 'ext', 'no', 'nos', 'p', 'pp'}

class Abbreviations:
    # Rubular: http://rubular.com/r/EUbZCNfgei
    WithMultiplePeriodsAndEmailRule = Rule(r"(\w)(\.)(\w)", r'\1∮\3')

# Rubular: http://rubular.com/r/G2opjedIm9
GeoLocationRule = Rule(r"(?<=[a-zA-z]°)\.(?=\s*\d+)", r'∯')
FileFormatRule = Rule(r"(?<=\s)\.(?=(jpe?g|png|gif|tiff?|pdf|ps|docx?|xlsx?|svg|bmp|tga|exif|odt|html?|txt|rtf|bat|sxw|xml|zip|exe|msi|blend|wmv|mp[34]|pptx?|flac|rb|cpp|cs|js)\s)", r'∯')
SingleNewLineRule = Rule(r"\n", r'ȹ')

class DoublePunctuationRules:
    FirstRule = Rule(r"\?!", r'☉')
    SecondRule = Rule(r"!\?", r'☈')
    ThirdRule = Rule(r"\?\?", r'☇')
    ForthRule = Rule(r"!!", r'☄')

    All = [ FirstRule, SecondRule, ThirdRule, ForthRule ]

# Rubular: http://rubular.com/r/aXPUGm6fQh

QuestionMarkInQuotationRule = Rule(r"\?(?=(\'|\"))", r'&ᓷ&')

class ExclamationPointRules:
    # Rubular: http://rubular.com/r/XS1XXFRfM2
    InQuotationRule = Rule(r"\!(?=(\'|\"))", r'&ᓴ&')

    # Rubular: http://rubular.com/r/sl57YI8LkA
    BeforeCommaMidSentenceRule = Rule(r"\!(?=\,\s[a-z])", r'&ᓴ&')

    # Rubular: http://rubular.com/r/f9zTjmkIPb
    MidSentenceRule = Rule(r"\!(?=\s[a-z])", r'&ᓴ&')

    All = [ InQuotationRule, BeforeCommaMidSentenceRule, MidSentenceRule ]

class SubSymbolsRules:
    Period = Rule(r"/", r'.')
    ArabicComma = Rule(r"♬", r'،')
    SemiColon = Rule(r"♭", r':')
    FullWidthPeriod = Rule(r"&ᓰ&", r'。')
    SpecialPeriod = Rule(r"&ᓱ&", r'．')
    FullWidthExclamation = Rule(r"&ᓳ&", r'！')
    ExclamationPoint = Rule(r"&ᓴ&", r'!')
    QuestionMark = Rule(r"&ᓷ&", r'?')
    FullWidthQuestionMark = Rule(r"&ᓸ&", r'？')
    MixedDoubleQE = Rule(r"☉", r'?!')
    MixedDoubleQQ = Rule(r"☇", r'??')
    MixedDoubleEQ = Rule(r"☈", r'!?')
    MixedDoubleEE = Rule(r"☄", r'!!')
    LeftParens = Rule(r"&✂&", r'(')
    RightParens = Rule(r"&⌬&", r')')
    TemporaryEndingPunctutation = Rule('ȸ', '')
    Newline = Rule(r"ȹ", r"\n")

    All = [ Period, ArabicComma,
            SemiColon, FullWidthPeriod,
            SpecialPeriod, FullWidthExclamation,
            ExclamationPoint, QuestionMark,
            FullWidthQuestionMark, MixedDoubleQE,
            MixedDoubleQQ, MixedDoubleEQ,
            MixedDoubleEE, LeftParens,
            RightParens, TemporaryEndingPunctutation,
            Newline ]

class ReinsertEllipsisRules:
    SubThreeConsecutivePeriod = Rule(r"ƪ", r'...')
    SubThreeSpacePeriod = Rule(r"♟", r' . . . ')
    SubFourSpacePeriod = Rule(r"♝", r'. . . .')
    SubTwoConsecutivePeriod = Rule(r"☏", r'..')
    SubOnePeriod = Rule(r"∮", r'.')

    All = [ SubThreeConsecutivePeriod, SubThreeSpacePeriod,
            SubFourSpacePeriod, SubTwoConsecutivePeriod,
            SubOnePeriod ]

ExtraWhiteSpaceRule = Rule(r"\s{3,}", ' ')

SubSingleQuoteRule = Rule(r"&⎋&", "'")

class AbbreviationReplacer():
  SENTENCE_STARTERS = "A Being Did For He How However I In It Millions More She That The There They We What When Where Who Why".split(' ')

SENTENCE_BOUNDARY_REGEX = r"""
（(?:[^）])*）(?=\s?[A-Z])|「(?:[^」])*」(?=\s[A-Z])|\((?:[^\)]){2,}\)(?=\s[A-Z])|'(?:[^'])*[^,]'(?=\s[A-Z])|"(?:[^"])*[^,]"(?=\s[A-Z])|“(?:[^”])*[^,]”(?=\s[A-Z])|\S.*?[。．.！!?？ȸȹ☉☈☇☄]
""".strip() # HACK: find a better way to write this regex that's not stripping newlines

# Rubular: http://rubular.com/r/NqCqv372Ix
QUOTATION_AT_END_OF_SENTENCE_REGEX = r'[!?\.-][\"\'”“]\s{1}[A-Z]'

# Rubular: http://rubular.com/r/6flGnUMEVl
PARENS_BETWEEN_DOUBLE_QUOTES_REGEX = r'["”]\s\(.*\)\s["“]'

# Rubular: http://rubular.com/r/TYzr4qOW1Q
BETWEEN_DOUBLE_QUOTES_REGEX = r'"(?:[^"])*[^,]"|“(?:[^”])*[^,]”'

# Rubular: http://rubular.com/r/JMjlZHAT4g
SPLIT_SPACE_QUOTATION_AT_END_OF_SENTENCE_REGEX = r'(?<=[!?\.-][\"\'”“])\s{1}(?=[A-Z])'

# Rubular: http://rubular.com/r/mQ8Es9bxtk
CONTINUOUS_PUNCTUATION_REGEX = r'(?<=\S)(!|\?){3,}(?=(\s|\z|$))'

NUMBERED_REFERENCE_REGEX = r'(?<=[^\d\s])(\.|∯)((\[(\d{1,3},?\s?-?\s?)*\b\d{1,3}\])+|((\d{1,3}\s?)*\d{1,3}))(\s)(?=[A-Z])'

# Rubular: http://rubular.com/r/yqa4Rit8EY
PossessiveAbbreviationRule = Rule(r"\.(?='s\s)|\.(?='s$)|\.(?='s\z)", '∯')

# Rubular: http://rubular.com/r/NEv265G2X2
KommanditgesellschaftRule = Rule(r"(?<=Co)\.(?=\sKG)", '∯')

# Rubular: http://rubular.com/r/xDkpFZ0EgH
MULTI_PERIOD_ABBREVIATION_REGEX = r"\b[a-z](?:\.[a-z])+[.](?i)"

class AmPmRules:
    # Rubular: http://rubular.com/r/Vnx3m4Spc8
    UpperCasePmRule = Rule(r"(?<=P∯M)∯(?=\s[A-Z])", '.')

    # Rubular: http://rubular.com/r/AJMCotJVbW
    UpperCaseAmRule = Rule(r"(?<=A∯M)∯(?=\s[A-Z])", '.')

    # Rubular: http://rubular.com/r/13q7SnOhgA
    LowerCasePmRule = Rule(r"(?<=p∯m)∯(?=\s[A-Z])", '.')

    # Rubular: http://rubular.com/r/DgUDq4mLz5
    LowerCaseAmRule = Rule(r"(?<=a∯m)∯(?=\s[A-Z])", '.')

    All = [UpperCasePmRule, UpperCaseAmRule, LowerCasePmRule, LowerCaseAmRule]

# This class searches for periods within an abbreviation and
# replaces the periods.
class SingleLetterAbbreviationRules:
    # Rubular: http://rubular.com/r/e3H6kwnr6H
    SingleUpperCaseLetterAtStartOfLineRule = Rule(r"(?<=^[A-Z])\.(?=,?\s)", '∯')

    # Rubular: http://rubular.com/r/gitvf0YWH4
    SingleUpperCaseLetterRule = Rule(r"(?<=\s[A-Z])\.(?=,?\s)", '∯')

    All = [
    SingleUpperCaseLetterAtStartOfLineRule,
    SingleUpperCaseLetterRule
    ]

# TODO: bring the next two classes to another file somehow
class EllipsisRules:
    # Rubular: http://rubular.com/r/i60hCK81fz
    ThreeConsecutiveRule = Rule(r"\.\.\.(?=\s+[A-Z])", '☏.')

    # Rubular: http://rubular.com/r/Hdqpd90owl
    FourConsecutiveRule = Rule(r"(?<=\S)\.{3}(?=\.\s[A-Z])", 'ƪ')

    # Rubular: http://rubular.com/r/YBG1dIHTRu
    ThreeSpaceRule = Rule(r"(\s\.){3}\s", '♟')

    # Rubular: http://rubular.com/r/2VvZ8wRbd8
    FourSpaceRule = Rule(r"(?<=[a-z])(\.\s){3}\.(\z|$|\n)", '♝')

    OtherThreePeriodRule = Rule(r"\.\.\.", 'ƪ')

    All = [
      ThreeSpaceRule,
      FourSpaceRule,
      FourConsecutiveRule,
      ThreeConsecutiveRule,
      OtherThreePeriodRule
    ]

class Numbers:
    # Rubular: http://rubular.com/r/oNyxBOqbyy
    PeriodBeforeNumberRule = Rule(r"\.(?=\d)", '∯')

    # Rubular: http://rubular.com/r/EMk5MpiUzt
    NumberAfterPeriodBeforeLetterRule = Rule(r"(?<=\d)\.(?=\S)", '∯')

    # Rubular: http://rubular.com/r/rf4l1HjtjG
    NewLineNumberPeriodSpaceLetterRule = Rule(r"(?<=\r\d)\.(?=(\s\S)|\))", '∯')

    # Rubular: http://rubular.com/r/HPa4sdc6b9
    StartLineNumberPeriodRule = Rule(r"(?<=^\d)\.(?=(\s\S)|\))", '∯')

    # Rubular: http://rubular.com/r/NuvWnKleFl
    StartLineTwoDigitNumberPeriodRule = Rule(r"(?<=^\d\d)\.(?=(\s\S)|\))", '∯')

    All = [
      PeriodBeforeNumberRule,
      NumberAfterPeriodBeforeLetterRule,
      NewLineNumberPeriodSpaceLetterRule,
      StartLineNumberPeriodRule,
      StartLineTwoDigitNumberPeriodRule
    ]