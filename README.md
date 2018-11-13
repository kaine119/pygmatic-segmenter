# pygmatic_segmenter

Pygmatic Segmenter is a work-in-progress rule-based sentence-boundary detector, ported to python from [pragmatic_segmenter](https://github.com/diasks2/pragmatic_segmenter). It follows the design choices chosen from there, particularly in [ambiguous segments](https://github.com/diasks2/pragmatic_segmenter#background).

## Usage

This package hasn't been pushed to pip yet, but if you'd like to try it out, just clone the repository, `cd` into its directory and run a `python3` REPL.

Eventually, you'll be able to specify other languages with the `language` parameter; currently only English is supported. If a language is not specified, the segmenter will default to English.

```python3
$ python3

>>> import pygmatic_segmenter
>>> segmenter = pygmatic_segmenter.Segmenter("Hello world. My name is Mr. Smith. I work for the U.S. Government and I live in the U.S. I live in New York.", language="en")
>>> segmenter.segment()
# => ['Hello world.', 'My name is Mr. Smith.', 'I work for the U.S. Government and I live in the U.S.', 'I live in New York.']
```

## TODO
* Test the rest of the [golden rules](https://github.com/diasks2/pragmatic_segmenter#the-golden-rules)
* Port other languages supported by pragmatic_segmenter