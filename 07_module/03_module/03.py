# 3▹ Stwórz moduł, który zajmuje się jedynie otwieraniem plików - oferuje bezpieczny sposób odczytu oraz bezpieczny zapis.
# Funkcja czytająca pliki sprawdza najpierw czy dany plik istnieje oraz czy jest niepusty. Funkcja zapisująca do pliku chroni przed nadpisaniem istniejącego pliku.
import os


def open_file(filename):
    with open(filename,"r" ,encoding="utf-8") as f:
        print("Wiadomości zapisane w pliku --->" ,*f.readlines())




def write_to_file(filename):
    with open(filename, mode="a+",encoding="utf-8") as r:
        user = input("Czy chcesz coś zapisać do pliku [tak - nie]: ")
        if user == "tak":
            user_txt = input("podaj co chcesz dodać do pliku: ")
            r.write(user_txt)
            print("Dopisałeś do pliku", user_txt)
        else:
            print("Nic nie dodajesz do pliku ")



def empty_file(filename):
    if os.stat(filename).st_size == 0:
        print("Plik jest pusty")
    else:
        print("Plik nie jest pusty")


def file_exist(filename):
    if True == os.path.exists(filename):
        print("Plik istnieje")





def main():
    try:
        filename = input("Podaj nazwę pliku do otworzenia: ")
        file_exist(filename)
        empty_file(filename)
        open_file(filename)
        write_to_file(filename)


    except FileNotFoundError:
        print("Taki plik nie istnieje")




if __name__ == "__main__":
    main()