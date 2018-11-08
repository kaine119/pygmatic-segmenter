from pygmatic_segmenter.types import Rules

class EllipsisRules:
    # Rubular: http://rubular.com/r/i60hCK81fz
    ThreeConsecutiveRule = Rule(r"\.\.\.(?=\s+[A-Z])", '☏.')

    # Rubular: http://rubular.com/r/Hdqpd90owl
    FourConsecutiveRule = Rule(r"(?<=\S)\.{3}(?=\.\s[A-Z])", 'ƪ')

    # Rubular: http://rubular.com/r/YBG1dIHTRu
    ThreeSpaceRule = Rule(r"(\s\.){3}\s", '♟')

    # HACK: this works even with \Z?
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