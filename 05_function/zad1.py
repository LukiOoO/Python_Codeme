

books = {}

#1.    Napisz funkcję, która pyta użytkownika o pary książka + ocena i zapisuje je w programie.
def save_book():
    book_title = input("Podaj tytul ksiazki: ")
    book_rate = input("Podaj ocene ksiazki 1-10: ")
    books[book_title] = book_rate

#2.    Napisz funkcję, która zapyta tytuł książki i wyświetli tytuł wraz z oceną.
def show_book(title):
    print(f'Książka {title} ma ocenę --> { books[title] }')

# ------ główna część programu

for i in range(3):
    save_book()
    print('-----')

print(books)

# -------
while(True):
    given_title = input('Podaj tytuł do sprawdzenia oceny: ')
    if given_title in books.keys():
        break

    print('Takie tytułu nie mamy!')

# --- metoda pokazuja ocene książki
show_book(given_title)
