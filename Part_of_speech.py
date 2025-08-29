# PARTS OF SPEECH (POS) TAGGING

import nltk

# Required downloads
nltk.download('punkt')
nltk.download('punkt_tab')  # new dependency for tokenizer
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')  # new name in latest NLTK

from nltk.tokenize import word_tokenize
from nltk import pos_tag

text = "This is simple Parts of speech tagging program"
words = word_tokenize(text)

pos_tags = pos_tag(words)
for word, tag in pos_tags:
    print(f"{word}: {tag}")
