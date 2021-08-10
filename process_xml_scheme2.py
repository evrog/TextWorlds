# -*- coding: utf-8 -*-

# This is a parser for XML-files from the folder 'pretty_xml_Text_Worlds'.
# The XML-data were prettified with 'minidom.parseString(ET.tostring(root)).toprettyxml(encoding='utf-8')'
# for a clearer presentation of tags.
# Why not use an existing parser?--Text alignment, in the first place: to keep the order of tokens
# so that across files with the same text the same tokens have the same ID (number). And there are
# some more minor issues..
# Download the folder 'pretty_xml_Text_Worlds' and 'list_of_xml_scheme2_files.txt' in the same folder
# with this file and run it. Make sure you have nltk installed.


import csv
import re
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize


# A ready list of files from the folder 'pretty_xml_Text_Worlds'.
with open('./list_of_xml_scheme2_files.txt', 'r') as data:
  list_of_files=data.read().splitlines()


# open_xml:
# Function: To get annotated text from any of the files in the folder 'pretty_xml_Text_Worlds':
# the text split into lines, its title, marker of the annotator and type of mark-up (elments or shifts).
# Input: file address in 'pretty_xml_Text_Worlds'.
# Output: split text, title, marker of the annotator, type of mark-up.

def open_xml(f):
  with open(f, 'r') as xml_data:
    text=xml_data.read().splitlines()
  text=[' '.join(t.split()) for t in text]
  text=[t for t in text if len(t)>0][1:]
  filename=f.split('/')[-1][:-4]
  print(filename)
  text_meta=filename.split('_')
  text_name=text_meta[0]
  annotator_name=text_meta[1]
  scheme_level=text_meta[2]
  return text, text_name, annotator_name, scheme_level


# A dictionary for data from the XML-files.
dict_of_texts={}


# dispatcher:
# Function: splits text lines into tokens, while counting their consecutive order in the text
# in the 'count_words' variable, then adds data (token, tag, marker of the annotator and type of mark-up)
# to 'dict_of_texts' and passes 'count_words' to the processor of the next file in the loop.
# Input: split text, 'count_words', title, marker of the annotator, type of mark-up, tags.
# Output: 'count_words'.

def dispatcher(some_text, count_words, text_name, annotator_name, scheme_level, save_tags):
  
  global dict_of_texts
  
  list_of_tokens=[]

  some_text=some_text.replace('-', ' ')
  some_text=some_text.replace('—', ' ')
  some_text=some_text.replace('…', '.')

  tokens=word_tokenize(some_text)

  for token in tokens:
    
    if count_words not in dict_of_texts[text_name]:
      dict_of_texts[text_name][count_words]=[]
      
    if len(save_tags)>1:
      
      tags=save_tags[1:]
      for tag in tags:
        dict_of_texts[text_name][count_words].append((token, tag, annotator_name, scheme_level))
        
    else:
      dict_of_texts[text_name][count_words].append((token, 'None', annotator_name, scheme_level))
      
    count_words+=1
    
  return count_words


# file_processor:
# Function: gathers data about the text in the file, separates tags and stores them in a list
# so that tokens with multiple tags are kept separate, but have the same ID number.
# Input: file name from 'list_of_files'.
# Output: None. (During the processing, 'dispatcher' adds data to 'dict_of_texts'.)

def file_processor(filename):

  global dict_of_texts

  text, text_name, annotator_name, scheme_level=open_xml(f)
  
  if text_name not in dict_of_texts:
    dict_of_texts[text_name]={}

  save_tags=[]
  count_words=0

  for line in text:
    
    open_tag=re.match(r'<[^/.]+?>', line)
    close_tag=re.search(r'</.+?>', line)
    if not open_tag:
      lonely_close_tag=re.search(r'</.+?>', line)
    
    if open_tag:
      
      tag_name=open_tag.group(0)[1:-1]
      save_tags.append(tag_name)
      ine=line[len(tag_name)+2:]
      
      if len(ine)>0:
        find_text=re.search(r'[^<]+', ine)

        if find_text:
          count_words=dispatcher(find_text.group(0), count_words, text_name, annotator_name, scheme_level, save_tags)

      if close_tag:
        save_tags=save_tags[:-1]

    elif lonely_close_tag:

      tag_name=lonely_close_tag.group(0)
      find_text=line[:line.find(tag_name)]
      count_words=dispatcher(find_text, count_words, text_name, annotator_name, scheme_level, save_tags)
      save_tags=save_tags[:-1]

    else:
      count_words=dispatcher(line, count_words, text_name, annotator_name, scheme_level, save_tags)

if __name__=='__main__':
  for f in list_of_files:
    file_processor(f)

  print(open_xml(list_of_files[5]))
  print(dict_of_texts['Лисичка'])
