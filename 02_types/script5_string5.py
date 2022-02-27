#Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np.: Kobyła ma mały bok.
# Pozwól użytkownikowi wprowadzić dowolne zdanie. Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.
#





s = input("Enter the text: ")

reverse = s[::-1]

if (s == reverse):
    print("yes it is palindrome")
else:
    print("not it is not palindrome")