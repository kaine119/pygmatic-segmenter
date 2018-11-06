from pygmatic_segmenter.types import Rule

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