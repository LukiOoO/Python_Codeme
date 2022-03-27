# 2▹ Utwórz dowolną krotkę zawierającą kilka wartości np. 10. Pozwól użytkownikowi podać dowolny index oraz wartość. Spróbuj w krotce podmienić wartość na zadanym indeksie. Obsłuż błąd


tuple1 = (10,22,"tekst",range(1,4),[],{1,"cos"},"8",4,[1,2,3])

def main():
    try:
        index = int(input("Podaj index: "))
        print(tuple1[index])
        x = tuple1[index] = input("Podaj cos do podnieniea: ")
    except TypeError:
        print("Wystąpił błąd")


if __name__ == "__main__":
    main()