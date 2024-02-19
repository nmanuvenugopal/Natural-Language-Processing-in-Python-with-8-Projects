import nltk

from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer

words = ['run', 'runner', 'running', 'runs', 'ran', 'easily', 'fairly']

# We need to create the object of both stemmer

porter_stem = PorterStemmer()
snowball_stem = SnowballStemmer(language='english')

for word in words:
    print(f"The Porter output for {word} is --------> {porter_stem.stem(word)}")

for word in words:
    print(f"The Snowball output for {word} is --------> {snowball_stem.stem(word)}")
