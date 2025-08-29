# FILTERING OF STOP WORDS
import nltk

nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "Hello, this is simple a Stop Words Program"
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(text)

filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

filtered_sentence = []

for w in word_tokens:
  if not w in stop_words:
    filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)
