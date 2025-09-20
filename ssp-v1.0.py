import random

# Laat de computer kiezen
options = ["schaar", "steen", "papier"]
computerkeuze = random.choice(options)

# Laat de gebruiker kiezen
def gebruikerkiest():
    global gebruikerkeuze
    gebruikerkeuze = input("Kies (schaar/steen/papier) : ")

    if gebruikerkeuze == "schaar":
        controle()

    elif gebruikerkeuze == "steen":
        controle()

    elif gebruikerkeuze == "papier":
        controle()

    else:
        print("Error 3659: Unexpected Input")
        print("Jouw input is incorrect")
        inputerrorhandeling = input("Opnieuw proberen? (y/n) : ")
        if inputerrorhandeling == "y" or inputerrorhandeling == "j" or inputerrorhandeling == "yes":
            gebruikerkiest()

        else:
            exit()

# Controleert wie gewonnen heeft
def controle():
    if gebruikerkeuze == computerkeuze:
        print("Geblijkspel")

    elif gebruikerkeuze == "schaar" and computerkeuze == "papier":
        print("Je hebt gewonnen!")

    elif gebruikerkeuze == "steen" and computerkeuze == "schaar":
        print("Je hebt gewonnen!")

    elif gebruikerkeuze == "papier" and computerkeuze == "steen":
        print("Je hebt gewonnen!")

    else:
        print("Je hebt verloren")

gebruikerkiest()
