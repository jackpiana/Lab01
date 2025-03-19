import random
import Quiz

quizzes = []

def loadQuizzes():
    with open("domande.txt", "r", encoding="utf-8") as file:
        input = []
        for row in file:
            if row == "\n":
                quiz = Quiz.Quiz(input)
                input = []
                quizzes.append(quiz)
            else:
                input.append(row)

def play():
    random.shuffle(quizzes)
    currentLevel = 0
    points = 0
    for quiz in quizzes:
        if int(quiz.livello) == currentLevel:
            print(quiz)
            risposta = input("RISPOSTA: ")
            if risposta != "a" and risposta != "b" and risposta != "c" and risposta != "d":
                print("formato risposta errato")
                continue
            if risposta == "a":
                if quiz.opzioni[0] == quiz.corretta:
                    print("RISPOSTA ESATTA!!!\n")
                    currentLevel += 1
                    points += 1
                else:
                    print("Risposta errata\nGAME OVER\n")
                    break
            if risposta == "b":
                if quiz.opzioni[1] == quiz.corretta:
                    print("RISPOSTA ESATTA!!!\n")
                    currentLevel += 1
                    points += 1
                else:
                    print("Risposta errata\nGAME OVER\n")
                    break
            if risposta == "c":
                if quiz.opzioni[2] == quiz.corretta:
                    print("RISPOSTA ESATTA!!!\n")
                    currentLevel += 1
                    points += 1
                else:
                    print("Risposta errata\nGAME OVER\n")
                    break
            if risposta == "d":
                if quiz.opzioni[3] == quiz.corretta:
                    print("RISPOSTA ESATTA!!!\n")
                    currentLevel += 1
                    points += 1
                else:
                    print("Risposta errata\nGAME OVER\n")
                    break
    print(f"punteggio finale: {points}")
    return [input("nickname: "), points]

def writeFilepunti(record):
    recordOrdinato = sorted(record, key=lambda x: x[1], reverse = True)
    with open("punti.txt", "w", encoding="utf-8") as file:
        for row in recordOrdinato:
            file.write(f"{row[0]} {row[1]}\n")

def main():
    loadQuizzes()
    random.shuffle(quizzes)
    gameStatus = True
    record = []
    while gameStatus:
        player = play()
        record.append(player)
        statoPartita = input("continuare partita? si/no: ")
        if statoPartita == "off":
            gameStatus = False
    writeFilepunti(record)


main()



