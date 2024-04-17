# 9▹ Kolejnym warunkiem, aby dostać “żółte tablice”, jest to, aby samochód posiadał co najmniej 75% oryginalnych części. W naszym zadaniu zakładamy, że rzeczoznawca określił jego oryginalność w kategorii tak/nie.
#
# Poniżej stworzenia i wyświetlenia słownika w zadaniu powyżej:
# dopisz do słownika nowy klucz czy_oryginalny i ustaw jego wartość (typ: bool) wedle uznania.
#
# ponownie wyświetl zmieniony słownik
#
# Zmodyfikuj program tak, aby uwzględnił decyzję o możliwości zarejestrowania samochodu również od jego oryginalności. Dopisz odpowiednie komunikaty.



def dict_creator(brand,model,yeer,oryginal):
    car_dict = {}
    car_dict["marka"] = brand
    car_dict["model"] = model
    car_dict["rocznik"] = yeer
    car_dict["oryginal"] = oryginal
    print(car_dict)


def vintage_car(model,yeer,oryginal):
    current_year = 2022
    if current_year - yeer >= 25 and oryginal >= 75:
        print(f"Gratulacje twój samochód {model} może zostać zarejestorwany jako zabytek spełnia wszytskie warunki")

    elif current_year - yeer >= 25 and oryginal < 75:
        print(f"Twój samochód {model} ma odpowiedni wiek ale nieorginalne części")

    else:

        print(f"Twój samochód {model} jest zbyt młody żeby zostać zabytkiem")







brand = str(input("Podaj marke: "))
model = str(input("Podaj model: "))
yeer = int(input("Podaj rocznik: "))
oryginal = int(input("Podaj % orginalnośc rzeczoznawcy: "))

dict_creator(brand,model ,yeer,oryginal)
vintage_car(model,yeer,oryginal)