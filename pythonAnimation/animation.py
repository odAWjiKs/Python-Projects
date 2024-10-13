import time
import os
clear = lambda: os.system('cls')
clear()

paths = []
ilosc = int(input("Ile zdjęć zawiera animacja? "))

for i in range(ilosc):
    a = input("Podaj ścieżkę (bez rozszerzenia .txt): ")
    paths.append(a)

for j in range(len(paths)):
    f = open(f'{paths[j]}.txt', 'r')
    file_contents = f.read()
    print (file_contents)
    time.sleep(0.08)
    f.close()
    clear = lambda: os.system('cls')
    clear()

