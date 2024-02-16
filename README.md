# Natural-Language-Processing-in-Python-with-8-Projects

Some of the basic topic that we need to be aware before starting the project are :
1. Tokenization
2. Lemmatization
3. Stemming
4. Stop words
5. Part of Speech (POS)
6. Named entity recognization (NER)
7. Sentence Segmentation
8. Vocabulary matching

One of the imporrtant library that we will be dealing with is "spacy". Inorder to import spacy we need to do the following.
1. pip install spacy
   
2. python -m spacy download en_core_web_sm
   Here i am downloading small model of spacy, If we need need medium or large then there is slight difference in the step:
   python -m spacy download en_core_web_md
   python -m spacy download en_core_web_lg

3. After download next step is to import and using it.
   import spacy
   nlp = spacy.load('en_core_web_sm')

Spacy can be used to tokenize the input and the below screenshot describes how efficient the spacy is:
![image](https://github.com/nmanuvenugopal/Natural-Language-Processing-in-Python-with-8-Projects/assets/99719105/59a4aeaa-6086-44e1-b9af-23174a87776b)
![image](https://github.com/nmanuvenugopal/Natural-Language-Processing-in-Python-with-8-Projects/assets/99719105/9220d3e5-52f5-42a6-9d96-027669c5b227)

Spacy is smart enough to identify that given item is a email id or website and split token according to that.
![image](https://github.com/nmanuvenugopal/Natural-Language-Processing-in-Python-with-8-Projects/assets/99719105/0c42b68b-5b94-47e9-8967-5ef2e12a3e8d)
![image](https://github.com/nmanuvenugopal/Natural-Language-Processing-in-Python-with-8-Projects/assets/99719105/ad8fd47c-514e-4acb-b35a-2617d071e88e)






