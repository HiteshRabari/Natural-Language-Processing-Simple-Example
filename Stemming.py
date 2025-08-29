# STEMMING
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Word Tokenize
text = "This is simple Stemming Program"
words = word_tokenize(text)

#Use Stemming algorithm (Porter Stemmer) and apply it to your words.
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]
print(stemmed_words)
