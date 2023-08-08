#!/usr/bin/env python
# coding: utf-8


import numpy as np
import pandas as pd
from googletrans import Translator
from os import listdir
import re
import time

translator = Translator()
basepath='DUC2001_Summarization_Documents/data/duc2002testtraining/'
folder_level_1=listdir(basepath)

# In[25]:

def find_doc_abs_name(filenames):
	for y in filenames:
	    p2=y.split(".")
	    if p2[1]=="abs":
	    	abst=y
	    elif p2[1]=="body":
	      	txt=y
	return (abst,txt)

def get_sentences_list(name):
	doc=open(name).read()
	list_sentences=doc.split('.')
	cleaned_sentences=[]
	ur_sentences=[]
	for y in list_sentences:
		c_sen=re.sub(r'[^A-Za-z0-9@]+', ' ', y)
		cleaned_sentences.append(c_sen)
		t_txt = translator.translate(c_sen, dest='ur')
		ur_sentences.append(t_txt.text)
		time.sleep(15)





	return ( ". ".join(cleaned_sentences), ". ".join(ur_sentences))






# In[26]:





# In[22]:


df=pd.DataFrame(columns=["SummaryEng","SummaryUr","TextEng","TextUr"])



for f in folder_level_1:
    sub_folders=listdir(basepath+str(f))
    
    for x in sub_folders:
        #abst=open(basepath+str(f)+"/"+x+"/"+x+".abs").read()
        #txt=open(basepath+str(f)+"/"+x+"/"+x+".txt").read()

        filenames=listdir(basepath+str(f)+"/"+x+"/")
       
        abs_name,doc_name=find_doc_abs_name(filenames)
        abst_eng,abst_urdu=get_sentences_list(basepath+str(f)+"/"+x+"/"+abs_name)
        doc_eng,doc_urdu=get_sentences_list(basepath+str(f)+"/"+x+"/"+doc_name)
        print (abst_urdu)
        print (doc_urdu)
        #=open(basepath+str(f)+"/"+x+"/"+y).read()
        #=open(basepath+str(f)+"/"+x+"/"+y).read()

        #t_abst = translator.translate('I love dogs', dest='ur')
        #t_txt = translator.translate(txt, dest='ur') 
        df=df.append({"SummaryEng":abst_eng,"SummaryUr":abst_urdu,"TextEng":doc_eng,"TextUr":doc_urdu},ignore_index=True)
        break
    break    
    

# In[ ]:


df.to_csv("output.csv")#,sheet_name="Data",encoding="UTF-16")


# In[ ]:




