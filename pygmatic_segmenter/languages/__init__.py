from pygmatic_segmenter.languages import English
from pygmatic_segmenter.languages import Common
from pygmatic_segmenter.languages import Armenian

LANGUAGE_CODES = {
	"en": English,
    "hy": Armenian
}

def get_language_by_code(code):
    return LANGUAGE_CODES.get(code) or Common