#!/usr/bin/python
# -*- coding: latin-1 -*-
import MySQLdb
def XXX():

    x='Bönisch,shash#HGünter'
    a=unicode(x,'latin1')
    print a.encode('latin1')+'#'+'AGSHGAGHA'
XXX()
"""
#!/usr/bin/python
bytes = 'Bun\xc4\x83-diminea\xc8\x9ba, lume'
bytes = 'Bun\xc4\x83-diminea\xc8\x9ba, lume'
unicode_strg = bytes.decode('utf-8')
print unicode_strg.encode('iso-8859-1', 'replace')
import locale
language, output_encoding = locale.getdefaultlocale()

print txt.encode(output_encoding)
"""
#text = '\xe9'.decode('latin-1')
#print text
