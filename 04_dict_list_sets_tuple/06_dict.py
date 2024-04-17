# 6▹ Utwórz listę zawierającą wartości poniższego słownika, bez duplikatów.

days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}
day_keys = days.keys()
day_values = days.values()


set_keys = set(day_keys)
set_values = set(day_values)


final_set = set_values.union(set_keys)




final_list = list(final_set)
print(final_list)

