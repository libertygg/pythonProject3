words = []

word = 0
while word != ' ':
    word = input('Введите слово: ')
    words.append(word)

words.pop()
TT1 = iter(words)

FL = []
for i in range(len(words)):
    TT2 = next(TT1)
    FL.append(TT2[0])

FL2 = ''.join(FL)
print(FL2)





