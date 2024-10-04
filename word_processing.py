import re
import string
import pymorphy3
from nltk.corpus import wordnet
from deep_translator import GoogleTranslator
from pathlib import Path

mat_words_path = Path("data/mat.txt")

with open(mat_words_path, "r", encoding="utf-8") as f:
    mat_words_set = {line.strip() for line in f}

morph = pymorphy3.MorphAnalyzer()
translator = GoogleTranslator(source='auto', target='ru')

def socroshalka(w1):
    if wordnet.synsets(w1):
        w1 = translator.translate(w1)
    if w1 not in mat_words_set and all(len(word) > 3 for word in w1.split()):
        lemma = morph.parse(w1)[0].normal_form
        if len(lemma) > 3:
            return lemma
    return ''

def process_word(word):
    try:
        word = word.lower().strip()
        if word.strip(string.whitespace) == word and ' ' in word:
            return ' '.join(socroshalka(i) for i in word.split())
        return socroshalka(word)
    except:
        return False
