# WORD FREQUENCY COUNTER
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
text = "Hello, this is simple Word tokenize Program Hello"
tokens = word_tokenize(text)
print(tokens)

from nltk.probability import FreqDist

freq_dist = FreqDist(text)

common_words = freq_dist.most_common()

for word,frequency in common_words:
  print(f"{word}: {frequency}")
