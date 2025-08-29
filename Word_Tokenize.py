# TOKENIZATION
import nltk

nltk.download('punkt')

from nltk.tokenize import word_tokenize

text = "Hello, this is simple Word tokenize Program"
tokens = word_tokenize(text)
print(tokens)
