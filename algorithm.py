import string
import sys
import urllib.request
import ssl
import split_to_sentence as split
import get_text
import re
import find_string

def run(url):
    article = get_text.text_from_html(url)

    if len(article) == 0:
        sys.exit(0)

    split_text = split.remove_word(article).split(" ")
    word_dict = {}

    # print(article)
    # print(split_text)

    for word in split_text:
        new_str = word.strip(string.punctuation).lower()
        if len(new_str) != 0:
            word_dict[new_str] = word_dict.get(new_str, 0) + 1

    # print(word_dict)

    sentences = split.split_into_sentences(article)
    all_sentences = []
    highest_rated_sentences = []
    # print(len(sentences))

    for index in range(len(sentences)):
        text_value = 0

        for word in split.get_lemma_sentence(sentences[index]).split():
            if word in word_dict:
                text_value += word_dict[word]

        text_value = text_value
        all_sentences.append([sentences[index], text_value, index])
        find_string.check_value(highest_rated_sentences, [sentences[index], text_value, index])

    # print(highest_rated_sentences)

    ordered_sentences = [highest_rated_sentences[0]]
    inserted = False
    for index in range(1, len(highest_rated_sentences)):
        inserted = False
        for i in range(len(ordered_sentences)):
            if highest_rated_sentences[index][2] < ordered_sentences[i][2]:
                ordered_sentences.insert(i, highest_rated_sentences[index])
                inserted = True
                break

        if not inserted:
            ordered_sentences.append(highest_rated_sentences[index])


    # print()
    # print()
    # print()
    # print("the 5 highest rated sentences in order:")
    # print()
    #
    # for i in range(len(ordered_sentences)):
    #     print(ordered_sentences[i][0])

    return ordered_sentences
