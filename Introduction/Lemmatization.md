We have already seen that stemming is converting or mapping a word to its root word, problem with stemming is that it is more like removing the siffix of that word and the resulting word might not be always meaningful one.

Lemmatization is also process oof converting a word to its root word but in lemmatization word will be mapped to its root word and the resulting word will be meaningful one.

Let's compare the result of Stemming and Lemmatization result for the following sentence (Here we will be considering snowball stemming since it was giving more meaningful results):
Since there we load the dictionary while loading the spacy it will able to classify he word to its root word more accurately.

From the below example, we can see that Lemmatization is able to undertand the meaning of the word and then classify it to its corresponding root word. "Best" is mapped to "Good" and "Feet" is mapped to "Foot". 

![image](https://github.com/nmanuvenugopal/Natural-Language-Processing-in-Python-with-8-Projects/assets/99719105/860ac74d-6859-4b8e-8eb1-6976329c4a14)

![image](https://github.com/nmanuvenugopal/Natural-Language-Processing-in-Python-with-8-Projects/assets/99719105/ba557009-01ba-4ec9-a03c-c65bf82868ae)

We can say that Lemmatization is more accurate and efficient way of mapping a word to it root word.
