#!/usr/bin/python3.6

import webbrowser
import spacy


MODEL = 'pl_core_news_md'


def main():
    nlp = spacy.load(MODEL)
    while True:
        doc = nlp(input('Wprowadź zdanie: '))
        webbrowser.open_new_tab('http://0.0.0.0:5000')
        print('Naciśnij Ctrl+C, żeby wprowadzić kolejne zdanie')
        spacy.displacy.serve(doc, style='dep')


if __name__ == '__main__':
    main()
