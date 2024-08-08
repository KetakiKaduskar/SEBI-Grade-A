#remove duplicate words from a sentence

def removeDup(sent):
    words = sent.split()
    uniqueWords = []
    checked = set()

    for word in words:
        if word not in checked:
            uniqueWords.append(word)
            checked.add(word)

    return " ".join(uniqueWords)

sentence = input()
print(removeDup(sentence))