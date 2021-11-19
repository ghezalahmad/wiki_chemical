import spacy
import pandas as pd
import wikipediaapi
import csv
from IPython.display import display
from tabulate import tabulate

wiki_wiki = wikipediaapi.Wikipedia('en')
while True:
    try:
        chemical = input("Write the name of entity: \n")
        page_py = wiki_wiki.page(chemical)
        sumary = page_py.summary[0:]

        nlp = spacy.load('en_core_web_sm')

        sent_list = [sent.text for sent in nlp(sumary).sents]
        cumul_sent_list = [sent_list[0], ' '.join(sent_list[:2]), ' '.join(sent_list)]

        df = pd.DataFrame({'Entity': chemical, 'Description': cumul_sent_list})
        df["Sentences"] = pd.Series([f"Sentence1-{i+1}" for i in range(len(cumul_sent_list))]) # replace "Sentence{i+1}" with "Sentence1-{i+1}" if cumulating
        df = df.pivot(index="Entity", columns="Sentences", values="Description")

          #for col1,col2 in zip(text1, text2):
        filename = 'out.csv'
        df.to_csv(filename, mode='a', header=False)
        print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
    except wikipedia.exception.PageError as e:
        print(e.message)
        if chemical == "":
            break
        else:
            print('Continue to the next entities...')
