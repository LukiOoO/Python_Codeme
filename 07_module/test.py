# import sys
#
# print(sys.path)
#
# ['X:\\programowanie\\PythonKurs\\07_module', 'X:\\programowanie\\PythonKurs', 'X:\\programowanie\\Projekty',
#  'X:\\programowanie\\PythonKurs\\04_dict_list_sets_tuple',
#  'X:\\programowanie\\python\\python310.zip', 'X:\\programowanie\\python\\DLLs',
#  'X:\\programowanie\\python\\lib',
#  'X:\\programowanie\\python',
#  'C:\\Users\\Łuaksz\\AppData\\Roaming\\Python\\Python310\\site-packages',
#  'X:\\programowanie\\python\\lib\\site-packages']
# maxofthree.py
def max_of_2(x, y):
  return x if x > y else y


def maximum_of(num1, num2, num3):
    return max_of_2(max_of_2(num1, num2), num3)


if __name__ == "__main__":
  a, b, c = (4, 12, 7)
  v = maximum_of(a, b, c)
  print("Moja wieksza liczba to: ", v)
