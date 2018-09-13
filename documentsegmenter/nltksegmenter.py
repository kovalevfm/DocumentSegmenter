# coding: utf-8
import cPickle as pickle
import nltk.data
from documentsegmenter.utils import EMPTYLINE, NNPARAGRAPH, STRIP_RE, LINEBREAK

class Segmenter(object):
    def __init__(self, model=None):
        if not model:
            self.st = nltk.data.load('tokenizers/punkt/english.pickle')
        else:
            self.st = pickle.load(open(model))

    def segment(self, doc, eliminate_line_breaks=False):
        doc = EMPTYLINE.sub(u'\n', doc)
        docs = NNPARAGRAPH.split(doc)
        result = []
        for d in docs:
            if STRIP_RE.match(d):
                result.append(d)
                continue
            last_pos = 0
            for seg in self.st.tokenize(d):
                first_symbol_pos = d.find(seg, last_pos)
                last_symbol_pos = first_symbol_pos + len(seg)
                if first_symbol_pos > last_pos:
                    result.append(d[last_pos:first_symbol_pos])
                if eliminate_line_breaks:
                    result.append(LINEBREAK.sub(u' ', seg))
                else:
                    result.append(seg)
                last_pos = last_symbol_pos
            if len(d) > last_pos:
                result.append(d[last_pos:len(d)])
        return result
