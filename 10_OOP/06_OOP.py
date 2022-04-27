# # 6▹ Utwórz klasę Pracownik.
# Pracownik ma stanowisko, wynagrodzenie, imie, nazwisko, staz pracy.
#
# Pracownik powinen miec roczne podwyżki wg. dowolnie wymyślonego sposobu liczenia.
# Pracownik powinen odprowadzać podatek o wysokoci zależnej od swoich zarobków oraz minimalną składkę zdrowotną.
#
# Pracownik powinien mieć pole typu boolowskiego zawierające status studenta.
# Jeśli pracownik jest studentem jego składka zdrowotna wynosi 0%.
#
# Wszyscy pracownicy mają wspólną nazwę firmy.
# Spółgłoski imienia i nazwiska wraz z nazwą firmy .com tworzą adres mailowy. Np.
#
# Adam Kowalski Love Python Company
#
# email -> smkwlsk@lovepythoncompany.com


class employee():
    def __init__(self, position, salary, name, surname, seniority):
        self.position = position
        self.salary = salary
        self.name = name
        self.surname = surname
        self.seniority = seniority
        self.company_name = "BlueIT"

    def salary_increase(self):
        minimum_seniority = 360
        if (self.seniority >= minimum_seniority) and (self.seniority <= minimum_seniority * 2):
            salary_inc = self.salary * 0.20
            print(salary_inc)
            return salary_inc
        if self.seniority >= minimum_seniority * 2:
            salary_inc = self.salary * 0.30
            print(salary_inc)
            return salary_inc
        if self.seniority < minimum_seniority:
            print("you need 360 days of service to get a raise ")

    def healthcare_contribution(self, student=bool):
        if student:
            print("no healthcare contribution")
        if not student:
            h_c = self.salary * 0.10
            print(h_c)
            return h_c

    def tax(self):
        t = self.salary * 0.10
        print(t)
        return t

    def email(self):
        x = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        s = self.name + self.surname
        li = []
        for i in s:
            li.append(i)
        for i in li:
            if i in x:
                li.remove(i)
        y = ""
        for i in li:
            y += i
        return f"{y}@{self.company_name}.com".lower()


kris = employee("python_developer", 20000, "Krzysiu", "Aadamczyk", 900)
kris.salary_increase()
kris.healthcare_contribution(False)
kris.tax()
print(kris.email())
