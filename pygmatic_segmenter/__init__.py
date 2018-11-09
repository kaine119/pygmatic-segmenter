from pygmatic_segmenter.languages import get_language_by_code

from pygmatic_segmenter.Processor import Processor
from pygmatic_segmenter.Cleaner import Cleaner

class Segmenter:
    def __init__(self, text, language = None, doc_type = None, clean = True):
        if not text:
            raise ValueError("Text must not be empty")
        
        self.language = language
        self.language_module = languages.get_language_by_code(language)
        self.doc_type = doc_type

        if clean:
            self.text = Cleaner(text = text, doc_type = self.doc_type, language = self.language_module).clean()
        else:
            self.text = text
    
    def segment(self):
        if not self.text:
            return []
        return Processor(self.language_module).process(self.text)