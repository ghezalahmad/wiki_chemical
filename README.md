# wiki_chemical
We used the wikipedia API to find the chemical entities and extract the summaries. 

Further, we give structure to the output based our needs, so we stored the information in a table. The first column of the table will have the name of the entity we searched, the second column will have the first sentence, the thrid column will have the sentence1 + sentence 2, and the last sentence will have all the summary output. For doing this, we used the 'spacy' to detect the sentence boundary.


# Requirements:
```
 pip install wikipedia-api 
 pip install pandas 
```
and for the spacy:
```
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm

```
