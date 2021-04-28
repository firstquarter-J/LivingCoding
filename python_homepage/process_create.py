#!python
import sys
import codecs
import cgi

form = cgi.FieldStorage()
title = form["title"].value
description = form['description'].value

opend_file = open('data/'+title, 'w')
opend_file.write(description)
opend_file.close()

# Redirection
print("Location: index.py?id="+title)
print()
