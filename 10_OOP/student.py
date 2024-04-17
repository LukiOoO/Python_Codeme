
class Student(): #klasa
    univeristy = 'UAM'

    def __init__(self, firstname, lastname, subject):
        self.firstname = firstname
        self.lastname = lastname
        self.subject = subject


    def email(self):
        return f'{self.lastname}.{self.firstname}@{self.univeristy}.pl'.lower()


#stworz obiekt instancję klasu Student

obj_anna = Student('Anna','Kowalska','Informatyka')
print(obj_anna.firstname)
print(obj_anna.email())

obj_jan = Student('Jan', 'Nowak', 'Biologia')
print(obj_jan.email())

print(obj_jan.__dict__)
print(Student.__dict__)

print(Student.email(obj_anna))