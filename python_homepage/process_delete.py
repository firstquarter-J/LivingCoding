#!python
import sys
import codecs
import cgi, os

import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value

os.remove('data/'+pageId)

#Redirection
print("Location: index.py")
print()
