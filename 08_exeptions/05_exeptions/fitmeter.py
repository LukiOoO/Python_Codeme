# 1▹ Stwórz moduł, który będzie przechowywał funkcję obliczającą bmi.py. Zaimportuj module do pliku fitmeter.py.
# Nowy plik będzie informował użytkownika o jego aktualnym BMI i na podstawie wyniku (niedowaga, nadwaga, otyłość) sugerował zmiany w stylu życia pobierane z odpowiedniego pliku.
#
# Utwórz plik bmi.py zawierający metodę obliczania bmi. Metoda zwraca wartości: niedowaga, waga normalna, nadwaga, otyłość.
#
# Utwórz 4 pliki .txt zawierające porady.
#
# Utwórz plik fitmeter.py, który zaimportuje moduł bmi.
#
# fitmeter.py pobierze wagę i wzrost pacjenta i przekaże do odpowiedniej funkcji z modułu bmi.
#
# Na podstawie zwróconej wartości fitmeter.py wyświetli odpowiednie porady dla pacjenta.
#
#
# 5▹ W kodzie BMI ufamy, że użytkownik podaje wartość w kilogramach lub w metrach i rzutujemy do float.
# Co jeśli użytkownik poda wartość 60 kg ? Zmodyfikuj kod z ostatnich zajęć tak, aby wykluczyć powyższy przypadek.






import bmi

def show_advice(state):
    filename = state + '.txt'
    with open(filename,encoding="utf-8") as fopen:
        content = fopen.read()

    print('----Twoja porada:')
    print(content)


def get_user_data():
    while True:
        try:
            w = float(input('Podaj swoją wagę [kg]: '))
            h = float(input('Podaj swoj wzrost [m]: '))
            if w > 597 or h > 2.8 :
                raise ValueError('Nie prawdopodobne')
            break
        except Exception as e:
            print("Wartość nie prawidłowa spróbuj jeszcze raz", e)
    return w, h



def main():
    w, h = get_user_data()
    resutl = bmi.get_bmi_value(w, h)
    show_advice(resutl)


if __name__ == '__main__':
    main()

