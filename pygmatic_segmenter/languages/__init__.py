from pygmatic_segmenter.languages import English
from pygmatic_segmenter.languages import Common

LANGUAGE_CODES = {
	"en": English
}

def get_language_by_code(code):
    return LANGUAGE_CODES.get(code) or Common