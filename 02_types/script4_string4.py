#Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
#
#Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
#
#Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
#
#Połącz dane w jeden ciąg book za pomocą spacji
#
#Policz liczbę wszystkich znaków w napisie book



book_name = input("Give the title of the book: ")
authors_surname = input("give the author's surname: ")
number_of_pages = input("specify number of pages: ")

print("Does the title of the book consist of letters: ", book_name.isalnum())
print("Does the author's name consist of letters: ", authors_surname.isalnum())
print("Is the number of pages in the book made up of numbers: ", number_of_pages.isdigit())

print("Did you mean ", book_name.title())
print("Did you mean ", authors_surname.title())

book = book_name + " " + authors_surname + " " + number_of_pages
print(book)

print(len(book))