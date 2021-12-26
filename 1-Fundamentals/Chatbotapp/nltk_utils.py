import nltk
#nltk.download('punkt') - you need to download this for popular data sets.
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentance):
    return nltk.word_tokenize(sentance)


def stem(word):
    return stemmer.stem(word.lower())

def list_of_words(sentence_tokenized, all_words):
    pass

"""#This is the test of the tokenization
a = "how are you ?"
print(a)
a = tokenize(a)
print(a)"""

""" # Testting the word stemmer
words = ["organize", "Organizes", "organizing"]
stem_words = [stem(w) for w in words]
print(stem_words) """
