import random

ilosc = int(input("Podaj liczbę symboli w wierszu(2-10 i tylko parzyste): "))
while(ilosc%2 != 0):
    ilosc = int(input("Podaj liczbę symboli w wierszu(2-10 i tylko parzyste): "))
iloscznakow = ilosc + 2
forCount = ilosc//2
pole = '| # '
emojis = ['😀', '😃', '😄', '😁', '😆', '😅', '😂', '🤣', '🥲', '🥹', '😊', '😇', '👽', '🙃', '😉','😌', '😍', '🥰', '😘', '😗', '😙', '😚', '😋', '😛', '😝', '😜', '🤪', '🤨', '🧐', '🤓','😎', '🥸', '🤩', '🥳', '👾', '😏', '😒', '😞', '😔', '😟', '😕', '🙁', '☹️', '😣', '😖','😫', '😩', '🥺', '😈', '🤔']
emojiArr = []
emojiArrCopy = []

for i in range(forCount):
    row = []
    for j in range(ilosc):
        row.append(random.choice(emojis))
    emojiArr.append(row)
    emojiArrCopy.append(row)
for row in emojiArr:
    print(" ".join(row))
for row in emojiArrCopy:
    print(" ".join(row))

print('___'*iloscznakow)
for i in range(ilosc):
    print(pole * ilosc, '|')
print('---'*iloscznakow)

random.shuffle(emojiArr)