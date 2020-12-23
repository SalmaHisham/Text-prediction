# Text prediction


## Description
it's a simple text prediction project which predicts the next word based on a specific corpus.
we chose "book corpora" from "NLTK library" as a training corpus in our algorithm.
and to avoid "Zero probability N-gram" we used the Laplace Smoothing algorithm,
the output is a list of predicted words and the one having the highest probability.

## Table of Contents

### Normalization
Normalization is a series of steps, called normal forms, used to ensure that data anomalies are not created when information is
inserted, updated, or deleted. Without normalizing, changes made to the database to reflect changes, in reality, will create inconsistencies
in the data, effectively making the data useless, we remove :
- stopwords_list
- punctuation
- upperCases

### Pre_processing
The next step was building our unigram, bigram dictionary with the Possibilities for each word after normalization 
to build our Laplace smoothed probabilities list.

### Main
Using the "Laplace smoothed probabilities list" we take the last word written by the user, set the possibilities of predicted words into a list, and return it.

## languages
python 3



