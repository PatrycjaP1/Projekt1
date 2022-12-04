import pandas as pd

tabela = pd.read_excel('c:/Users/Natalia/BMI.xlsx')

print(tabela)

pomiary = tabela.iloc
for osoba in pomiary:
    x = osoba['Osoba']
    wzrost = osoba['Wzrost'] / 100
    waga = osoba['Waga']

    BMI = (waga/(wzrost*wzrost))

    print("Osoba", x + " Ma BMI rowne", BMI)
