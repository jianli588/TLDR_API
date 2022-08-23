
def check_value(sentences, new_sentence):

    if len(sentences) == 0:
        sentences.append(new_sentence)

    for index in range(len(sentences)):
        if new_sentence[1] > sentences[index][1]:
            sentences.insert(index, new_sentence)
            break

    if len(sentences) > 5:
        sentences.pop()
