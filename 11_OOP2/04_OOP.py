# 4▹ Utwórz klasę zegaro-kalendarza. Zegaro-kalendarza łączy cechy zegara oraz kalendarza. Zaimplementuj dziedziczenie wielokrotne.
# Nasz zegaro-kalendarza powinen móc podawać aktualną datę oraz wyświetlać ile dni ma dany miesiąc.
# Dodatkowo utwórz sposób wyświetlania tak, aby zegaro-kalendarz zawierał datę, godzinę oraz widok dni ułożonych tygodniowo.
# Dla uproszczenia przyjmij 7 dni w tygodniu zawsze zaczyna się od pierwszego dnia.

import datetime
from calendar import weekheader, monthrange , firstweekday, month


class clock():
    def time(self):
        x = datetime.datetime.now()
        print("Obecna godzina to ---->", x.strftime("%H:%M:%S"))


class calender():
    def data(self):
        x = datetime.datetime.now()
        print("Dzisiejsza data to ----> ", x.strftime("%d-%m-%y"))

    def days_number(self):
        now = datetime.datetime.now()
        print("Liczba dni w tym miesiącu to -----> ", *monthrange(now.year, now.month))

    def month(self):
        now = datetime.datetime.now()
        print(month(now.year, now.month,))



class clockcalendar(clock, calender):
    def __init__(self):
        clock.time(self)
        calender.data(self)
        calender.days_number(self)
        calender.month(self)


clockcalendar = clockcalendar()