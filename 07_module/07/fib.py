# F1 = 1
# F2 = 1
# Fn = F(n-1) + F(n-2)
#
# 0 ->0
# 1 ->1
# 2 ->1
# 3 ->2
# 4 ->3
# 5 ->5
# 6 ->8
# 7 ->13
# 8 ->21

def generate_fibbonaci_se(n):
    result = [0, 1, 1]

    for i in range(2, n):
        current_result = result[-1] + result[-2]
        result.append(current_result)

    for v in range(len(result)):
        print(f"Fib od {v} --> {result[v]}")