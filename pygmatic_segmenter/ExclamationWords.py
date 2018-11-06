import re
from pygmatic_segmenter.PunctuationReplacer import PunctuationReplacer

EXCLAMATION_WORDS = "!Xũ !Kung ǃʼOǃKung !Xuun !Kung-Ekoka ǃHu ǃKhung ǃKu ǃung ǃXo ǃXû ǃXung ǃXũ !Xun Yahoo! Y!J Yum!".split(" ")

REGEXP = r"{}".format("|".join(map(re.escape, EXCLAMATION_WORDS)))

def apply_rules(text):
    return PunctuationReplacer(
        matches_array = re.findall(REGEXP, text),
        text = text
    ).replace()
