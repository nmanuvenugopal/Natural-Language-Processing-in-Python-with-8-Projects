Stemming and Lemmatization does the same job, mapping the words to its root word. In the case of stemming the stemmed ouput won't be a meaniingful one or output word is not always part of english dictionary but in case of lemmatization it will be always a meaningful one or it retuns a words which is part of the english dictionary.

Consider the following example, "Play", "Playing", "Played" all the 3 words have root words as "Play". Stemming can be classified into two categories:
1. Porter Stemmer
   We can see the how the porterstemmer have stemmed word "Fairly" and "Easily". It is not not meaningful word that can be found on dictionary:

   ![image](https://github.com/nmanuvenugopal/Natural-Language-Processing-in-Python-with-8-Projects/assets/99719105/d0ba4351-d41e-463f-b12e-f64111d90f97)

3. Snowball Stemmer
   In case of Snowball stemmer, it classify the fairly to meaningful word but in case of easily it failed. All over we can say that some of issue in porter stemmer is solved in snowball stemmer.

   ![image](https://github.com/nmanuvenugopal/Natural-Language-Processing-in-Python-with-8-Projects/assets/99719105/b754ddf8-1713-40ce-9e74-5fe363fae48e)

So we can conclude that Snowball stemmer is more efficient and agressive than Porter stemmer.
