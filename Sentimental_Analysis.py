
def word(sentence):
    badwords = open('badwords.txt').read().split('\n')
    sentence = sentence.split()
    for i in badwords:
        for words in sentence:
            if i in words:
                pos = sentence.index(words)
                sentence.remove(words)
                sentence.insert(pos, '*' * len(i))
    clean = ' '.join(sentence)
    x = []
    y = set()
    for k in clean.split():
        if k not in y:
            x.append(k)
            y.add(k)
    a = ' '.join(x)
    print(a)

while True:
    sentence = input()
    word(sentence)
