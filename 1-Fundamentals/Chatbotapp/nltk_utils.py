import nltk
import numpy as np
# nltk.download('punkt') - you need to download this for popular data sets.
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()


def tokenize(sentance):
    return nltk.word_tokenize(sentance)


def stem(word):
    return stemmer.stem(word.lower())


def list_of_words(sentence_tokenized, all_words):
    sentence_tokenized = [stem(w) for w in sentence_tokenized]

    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in sentence_tokenized:
            bag[idx] = 1.0
    return bag


"""---Test 1---- 
#This is the test of the tokenization
a = "how are you ?"
print(a)
a = tokenize(a)
print(a)"""

""" # ----Test 2----
Testing the word stemmer
words = ["organize", "Organizes", "organizing"]
stem_words = [stem(w) for w in words]
print(stem_words) """

""" #----Test 3-----
This is to test that training array works
sentence = ["hello", "how", "are", "you"]
words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
bog = list_of_words(sentence, words)
print(bog) """
