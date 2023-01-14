## A NLP diachronic study of cultural artefacts and trends

###### Introduction

The aim of this study is to identify tools and methods to deal with diachronic data and explore the evolution of cultural artefacts, phenomena and trends through discourse and context. 
In particular, this repository collects code, data and documents generated during an exploratory analysis on the history of vinyl records — from the death of this format to its revival in the past few years — through a diachronic news corpus.

###### Process 

After building a corpus of news articles published between 1988 and 2021 by the music magazine Billboard, texts were cleaned and preprocessed (see [Data cleaning 1](https://github.com/beatrice-f/Thesis-repo/blob/main/datacleaning1.py) and [Data cleaning 2](https://github.com/beatrice-f/Thesis-repo/blob/main/datacleaning2.py)): article bodies, representing the key element of our analysis, were isolated and organised by title, author, month and — most importantly — year. This process allowed to discard non-relevant text content and resulted in the the creation of the [final dataset](https://github.com/beatrice-f/Thesis-repo/blob/main/dataset.csv).

Having cleaned the corpus, we first extracted relevant metadata and statistics about it (see the [corpus_info.py](https://github.com/beatrice-f/Thesis-repo/blob/main/corpus_info.py) file), such as number of texts, words, characters, and key-sentences (sentences containing our target word) per year (presented in [this table](https://github.com/beatrice-f/Thesis-repo/blob/main/corpus_statistics.png)). Meta-information about yearly subsets of texts proved fundamental in the following steps of our study. 

In order to understand the evolution of narratives revolving around the vinyl format and how the context surrounding the target word had changed over time, sentence embeddings were generated and compared ([here](https://github.com/beatrice-f/Thesis-repo/blob/main/cos_similarity.py)) by leveraging models and tools provided by the SentenceTransformers framework. 

Finally, to dig deeper into the results obtained by computing the semantic similarity among sentences, an analysis of lexical patterns and context was carried out with the aim of understanding how sentiments and meanings relating to our target word have evolved in time. 


<sub>Content in this repository is licensed under a CC BY 4.0 license.</sub>
