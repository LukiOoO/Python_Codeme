# 8▹ Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.
#
# Program zacznie ze stworzonym słownikiem o trzech kluczach:
# marka (str)
#
# model (str)
#
# rocznik (int)
#
# Wypisze ten słownik na ekran (bez żadnego formatowania)
#
# Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
# “Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
#
# Jeśli nie spełnia powyższego warunku, wypisze komunikat:
# “Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
#
# Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!), aby zobaczyć, czy progam również zmienia swoje zachowanie.


def dict_creator(brand,model,yeer):
    car_dict = {}
    car_dict["marka"] = brand
    car_dict["model"] = model
    car_dict["rocznik"] = yeer
    print(car_dict)

def yeer_check(model,yeer):
    current_year = 2022
    if current_year - yeer >= 25:
        print(f"Gratulacje twój samochód {model} może zostać zarejestorwany jako zabytek")
    else:
        print(f"Twój samochód {model} jest zbyt młody żeby zostać zabytkiem")

brand = str(input("Podaj marke: "))
model = str(input("Podaj model: "))
yeer = int(input("Podaj rocznik: "))

dict_creator(brand,model ,yeer)

yeer_check(model,yeer)