import nltk
from nltk.stem.porter import PorterStemmer
import spacy

p_stemmer = PorterStemmer()
nlp = spacy.load('en_core_web_sm')

sentence = "The striped bats are hanging on their feet for best"

doc1 = nlp(sentence)
for token in doc1:
    print("Lemmatization")
    print(f"{token} =======> {token.lemma_}")

print("\n")

for word in sentence.split():
    print("Stemming")
    print(f"{word} =======> {p_stemmer.stem(word)}")
