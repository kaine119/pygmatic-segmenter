import pygmatic_segmenter.languages.English
import pygmatic_segmenter.languages.Common

LANGUAGE_CODES = {
	"en": English
}

def get_language_by_code(code):
    return LANGUAGE_CODES.get(code) or Common