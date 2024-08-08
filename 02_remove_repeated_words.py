#remove words occcuring more than once

def remRep(sent):
    words = sent.split()
    wordCount = {}

    for word in words:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1

    answer = [word for word in words if wordCount[word] == 1]
    return " ".join(answer)

sentence = input()
print(remRep(sentence))