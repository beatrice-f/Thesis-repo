# -*- coding: utf-8 -*-
"""corpus_info.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VuPisiTBV3WHUuvXpjCL0mK5iYAXkHOt
"""

from google.colab import drive
drive.mount('/content/drive')

import nltk
import os
import pandas as pd 
import string
import re

from pandas.io.common import file_exists
from google.colab import files
from collections import defaultdict
from nltk.tokenize import word_tokenize

nltk.download("punkt")
punctuation = list(string.punctuation) + ["''", "``", "--"]

path = 'path'
ds = pd.read_csv(path)
dataset_dict = ds.to_dict('list')
pattern = r'(?<!\w)vinyl.*?'

yearly_texts = {y: [f"{r['title']}.\n {r['text']}" for i,r in ds.iterrows() if r['year'] == y] for y in set(ds['year'].tolist())}

txt_count = {y: len(t) for y,t in yearly_texts.items()} #text counter
word_count = {y: sum(len(t.split()) for t in l) for y,l in yearly_texts.items()} #word counter
token_count = {y: sum(len(word_tokenize(t)) for t in l) for y,l in yearly_texts.items()} #token counter
no_punkt_count = {y: len(list(ele for t in l for ele in word_tokenize(t) if ele not in punctuation)) for y,l in yearly_texts.items()} #tokens without punctuation counter
char_count = {y: sum(len(t) for t in l) for y,l in yearly_texts.items()} #character counter
v_freq = {y: sum(len(re.findall(pattern, t.lower())) for t in l) for y,l in yearly_texts.items()} #'vinyl' frequency per year
key_list_vinyl = {y: [s for sent in l for s in sent if re.search(pattern, s.lower())] for y,l in tokenised_texts.items()} #key sentences per year

print('texts: ', txt_count)
print('words: ', word_count)
print('char.: ', char_count)
print('frequency: ', v_freq)



#normalized frequency x 1000 words.
nf = {}
for y,l in yearly_texts.items():
  occ = 0
  txt_len = 0
  for t in l:
    occ += len(re.findall(r'(?<!\w)vinyl.*?', t.lower()))
    txt_len += len(t.split())
  nf[y] =  round(occ/txt_len*10000, 2)

print(nf)
