from pygmatic_segmenter.languages import get_language_by_code

from pygmatic_segmenter.Processor import Processor

class Segmenter:
    def __init__(self, text, language = None, doc_type = None):
        if not text:
            raise ValueError("Text must not be empty")
        
        self.language = language
        self.language_module = languages.get_language_by_code(language)
        self.doc_type = doc_type

        # TODO: implement cleaner
        self.text = text
    
    def segment(self):
        if not self.text:
            return []
        return Processor(self.language_module).process(self.text)