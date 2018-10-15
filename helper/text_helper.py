import logging
from collections import Counter

import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize


def count_word(str):
    words = str.split()
    counts = 0
    for word in words:
        counts += 1

    return counts


def count_pos(text):
    try:
        tokens = nltk.word_tokenize(text.lower())
        text = nltk.Text(tokens)
        tags = nltk.pos_tag(text)
        counts = Counter(tag for word, tag in tags)
        return counts
    except LookupError:
        logging.error(
            "Maybe you haven't installed averaged_perceptron_tagger and punkt library. Downloading now for you.")
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        return None


def stem_text(text):
    ps = PorterStemmer()
    sentences = sent_tokenize(text)
    list_of_sentences = []
    for sentence in sentences:
        words = word_tokenize(sentence)
        list_of_words = []
        for word in words:
            word = ps.stem(word)
            list_of_words.append(word)
        stemmed_sentence = " ".join(list_of_words)
        list_of_sentences.append(stemmed_sentence)
    return ". ".join(list_of_sentences)
