# Korzystając z dowolnej metody reprezentacji grafu zapisać istniejące połączenia pomiędzy budynkami.
#
# Wyświetl wszystkie krawędzie parami, podzielone za pomocą ---

list2 =['dom','szkoła','szpital','bar','kościół','kino','teatr']



list1 = {'dom':['bar','szkoła','kościół'],
         'szkołą':['dom','szpital','bar'],
         'szpital':['bar','szkoła','teatr'],
         'bar': ['szpital','kościół','dom'],
         'kościół':['dom','bar','kino'],
         'kino':['szpital','kościół','teatr'],
         'teatr': ['szpital','kino']

         }

