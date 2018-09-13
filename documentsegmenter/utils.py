# coding: utf-8
import regex


EMPTYLINE = regex.compile(ur'(?V1p)[\s--\n]+\n', flags=regex.M|regex.U)
NNPARAGRAPH = regex.compile(ur'(?V1p)(\n\n)', flags=regex.M|regex.U)
LINEBREAK = regex.compile(ur'(?V1p)\n', flags=regex.M|regex.U)
STRIP_RE = regex.compile(ur'(?V1p)(^[\s]|[\s]+$)', flags=regex.M|regex.U)
