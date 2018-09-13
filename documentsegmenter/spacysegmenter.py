# coding: utf-8
import spacy
from documentsegmenter.utils import EMPTYLINE, NNPARAGRAPH, STRIP_RE, LINEBREAK


class Segmenter(object):
    def __init__(self, language='en'):
        self.sp = spacy.load(language)


    def segment(self, doc, eliminate_line_breaks=False):
        doc = EMPTYLINE.sub(u'\n', doc)
        docs = NNPARAGRAPH.split(doc)
        result = []
        for d in docs:
            for seg in self.sp(d).sents:
                seg = seg.string
                for sub_seg in STRIP_RE.split(seg):
                    if STRIP_RE.match(sub_seg):
                        result.append(sub_seg)
                        continue
                    if eliminate_line_breaks:
                        result.append(LINEBREAK.sub(u' ', sub_seg))
                    else:
                        result.append(sub_seg)
        return result
