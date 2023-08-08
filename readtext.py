import numpy as numpy
import pandas as pd
import xml.etree.ElementTree as ET
import io
fil=open("DUC2007_Summarization_Documents/2007 SCU-marked corpus/D0701.scu")
xml_data=fil.read()


"""
fil=open("DUC2007_Summarization_Documents/2007 SCU-marked corpus/D0701.scu")
txt=fil.read()
#print(txt)
import xml.etree.ElementTree as ET
root = ET.parse("DUC2007_Summarization_Documents/2007 SCU-marked corpus/D0701.scu")
print(root)
for type_tag in root.findall('line'):
    #value = type_tag.get('')
    print(type_tag)

from xml.dom import minidom
xmldoc = minidom.parse("DUC2007_Summarization_Documents/2007 SCU-marked corpus/D0701.scu")
itemlist = xmldoc.getElementsByTagName('line')
print(len(itemlist))
#print(itemlist[0].attributes['name'].value)
for s in itemlist:
    print(s.line)
"""
