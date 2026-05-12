word = input("Введите слово: ")
col = len(word)
shifr = '*' * col
mistake = 0

def guess(word, shifr):
    while True:
        choise = input("Введи символ ")
        nottruc = 0
        rasshifr = ""
        if choise == "stop":
            print("стопнулось")
            break
        elif len(choise) == 1:
            for i in range(len(word)):
                if word[i] == choise:
                    rasshifr += word[i]
                    print(rasshifr)
                elif nottruc == len(word):
                    if mistake == 4:
                        vis(mistake)
                        break
                else:
                    rasshifr += shifr[i]
                    nottruc += 1
        else:
            print("Вы ввели больше одного символа!")

def vis(mistake):
    if mistake == 0:
        print("___________\n|\n|\n|\n|\n|__________| \n")
        mistake += 1
        print(f"Ошибка номер {mistake}")
        guess(word, shifr)
    elif mistake == 1:
        print("___________\n| /\n| ( )\n|\n|\n|__________| \n")
        mistake += 1
        print(f"Ошибка номер {mistake}")
        guess(word, shifr)
    elif mistake == 2:
        print("___________\n| / |\n| ( )\n|\n|\n|__________| \n")
        mistake += 1
        print(f"Ошибка номер {mistake}")
        guess(word, shifr)
    elif mistake == 3:
        print("___________\n| / |\n| ( )\n|\n|\n|__________| \n")
        mistake += 1
        print(f"Ошибка номер {mistake}")
        guess(word, shifr)
    elif mistake == 4:
        print("___________\n| / |\n| ( )\n|\n|\n|__________| \n")
        print(f"Ошибка номер {mistake}")
        print("Ты проиграл!!!!!")

guess(word, shifr)