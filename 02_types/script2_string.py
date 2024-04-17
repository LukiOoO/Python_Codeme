#1 Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.

txt = "-bananan-"
center_txt = len(txt) // 2
prev_center = center_txt - 1
next_center = center_txt + 1

print(txt[prev_center:next_center + 1])















