# Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową, która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.

#bmi dane z google 17 - 18.49 - niedowagę 18.5 - 24.99 - wagę prawidłową 25.0 - 29.9 - nadwagę 30.0 - 34.99 - I stopień otyłości.



masa = int(input("Podaj mase wtojego ciała (kg): "))
wzrost = float(input("Podaj twój wzrost (m): "))



bmi = (masa) / (wzrost)**2
print("twoje bmi to", bmi)

if bmi <= 17:
    print("niedowaga")
elif (bmi >= 18.5 ) and ( bmi <= 24.99):
    print("waga prawidłowa")

elif ( bmi >= 25.0 ) and ( bmi <= 29.9):
    print("nadwaga")

elif bmi >= 30.0:
    print("1 stopien nadwagi")

