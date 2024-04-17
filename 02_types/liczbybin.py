#Dla podanej liczby w systemie dwójkowym bin_num = 1001111 oblicz wartość w systemie dziesiętnym. Zamianę z systemu binarnego na dziesiętny napisz samodzielnie (nie korzystaj z metody wbudowanej).

#1   0    0  1  1  1  1
#64  32  16  8  4  2  1

bin_num = 1001111

decimal_sys = 1 + 2 + 4 + 8 + 64

print("The number 1001111 in the decimal sytestem is: ", decimal_sys)


#można też inaczej

#1       0         0        1        1      1      1
#2**6    2**5      2**4     2**3     2**2   2**1   2**0



decimal_sys2 = (1 * 2 **6) + (0 * 2 **5) + (0 * 2**4) + (1 * 2**3) + (1 * 2**2) + (1 * 2**1) + (1 * 2**0)

print("The number 1001111 in the decimal sytestem is: ", decimal_sys2)