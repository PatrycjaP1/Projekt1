plik_zapis = open('bmi2', 'wt', encoding='utf-8')
i = 0
c = input("jednostki imperialne(cale,funty) naciśnij 'i', jednostki  metryczne(cm,kg) naciśnij 'm'")

print("imie"",""wzrost"",""waga"",""bmi"",""kategoria",file=plik_zapis)


def BMI(wzrost, waga):
    if c == "m":
        bmi = waga / ((wzrost / 100) ** 2)
    elif c == "i":
        bmi = waga/(wzrost**2) * 703

    if bmi <= 16:

        return "wygłodzenie", bmi
    elif (bmi >= 16 and bmi < 16.99):

        return "wychudzenie",bmi

    elif (bmi >= 17 and bmi < 18.49):

        return "niedowaga",bmi

    elif (bmi >= 18.5 and bmi < 24.99):

        return "pożądana masa ciała",bmi

    elif (bmi >= 25 and bmi < 29.99):

        return "nadwaga",bmi
    elif (bmi >= 30 and bmi < 34.99):

        return "otyłość pierwszego stopnia",bmi
    elif (bmi >= 35 and bmi < 39.99):

        return "otyłość drugiego stopnia", bmi
    elif (bmi >= 40):

        return "otyłość trzeciego stopnia", bmi


koniec = False
while not koniec:
    a = int(input("Podaj ilość obserwacji, które chcesz wykonać:"))
    for i in range(0, a):
        imie = str(input("podaj imie:"))
        wzrost = float(input("Podaj swój wzrost :"))
        waga = float(input("Podaj swoją wagę :"))

        kategoria,bmi = BMI(wzrost, waga)
        print(bmi, kategoria)

        print (imie,wzrost,waga,bmi,kategoria,file=plik_zapis, sep=",")
    print("Czy chcesz dodać kolejne obserwacje:(odpowiedz tak lub nie)")
    kolejne = input()
    if kolejne == "nie":
        koniec = True
    elif kolejne != 'tak':
        break
plik_zapis.close()


