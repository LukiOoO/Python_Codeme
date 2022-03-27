# 1▹ Stwórz listę składającą się z kilku elementów różnego typu np. [13, ‘string’, 2.45] itp.
# W pętli spróbuj wykonać dzielenie 10 przez wartość z listy. Złap wyjątki jakie mogą się przy tej okazji wydarzyć.


elements = [13,"string",("1","2"),[],{1,2},{"klucz":123},range(10),0]


for i in elements:
    try:
        result = 10 / i
    except (TypeError, ZeroDivisionError):
        print(f"{i}, nie może być dzielnikiem")


