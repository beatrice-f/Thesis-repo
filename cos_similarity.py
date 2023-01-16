# -*- coding: utf-8 -*-
"""cos_similarity.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fe9s0Asm_6FGPp1A51EQ8_X0ihavg-3-
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import nltk 
import re 
nltk.download('punkt')
import torch
from collections import defaultdict

#extract sentences 
pattern = r'(?<!\w)vinyl.*?'

path = "path"
dataset = pd.read_csv(path) 
y_texts = {y: [f"{r['title']}.\n {r['text']}" for i,r in dataset.iterrows() if r['year'] == y] for y in set(dataset['year'].tolist())}
tokenised_texts = {y:[nltk.sent_tokenize(txt) for txt in t] for y,t in y_texts.items()} 
key_list_vinyl = {y: [s for sent in l for s in sent if re.search(pattern, s.lower())] for y,l in tokenised_texts.items()}
print({k:len(v) for k,v in key_list_vinyl.items()})

#model

!pip install -U sentence-transformers
from sentence_transformers import SentenceTransformer, util
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching
model = SentenceTransformer('all-MiniLM-L6-v2',device ='cuda')

"""# Similarity"""

def emb (k1,k2, sentences_1,sentences_2): 

  sentences = sorted([(len(sentences_1),sentences_1),(len(sentences_2),sentences_2)])  
  embeddings1 = model.encode(sentences[0][1], convert_to_tensor=True)
  embeddings2 = model.encode(sentences[1][1], convert_to_tensor=True)

  cosine_scores = util.cos_sim(embeddings1, embeddings2)
  sort_max = [sorted([(p,pos) for pos,p in enumerate(ele)],reverse=True)[0] for ele in cosine_scores]
  filter_max = [ele for ele in sort_max if ele[0] >= 0.5]
  
  max_dict = defaultdict(list)   
  for n in filter_max:
    max_dict[n[1]].append(n[0])

  max = {k:sorted(v)[-1] for k,v in max_dict.items()}
  pro = torch.mean(torch.tensor([ele for ele in max.values()]))
  
  #score
  w = 0.02
  score = w/(k1-k2) if k1 > k2 else w/(k2-k1)
  pro = pro + score
  return pro

#similarity
output_similarity = defaultdict(list)
for pos,(k,v) in enumerate(key_list_vinyl.items()):
  years2 = [y for y in key_list_vinyl.keys()][pos+1:]
  if len(years2) > 0:
    for y2 in years2:
      output_similarity[f"{k}-{y2}"].append(emb(k,y2,v,key_list_vinyl[y2]).tolist())
  print(pos)

#generate csv 
df = {'years':[ele for ele in output_similarity.keys()],'values':[ele[0] for ele in output_similarity.values()]}
pd.DataFrame(df).to_csv('output_similarity.csv',index=False)

print(max(df['values']), min(df['values']), np.mean(df['values']))
