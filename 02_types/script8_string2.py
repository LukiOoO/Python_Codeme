#Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.


s1 = "hello world"
s2 = "banana"
s3 = "hello {} world".format(s2)
print(s3)