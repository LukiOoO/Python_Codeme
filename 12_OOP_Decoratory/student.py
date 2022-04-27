import datetime
from holidays import Poland

class Student:
    university = 'university'
    min_avg = 4.7

    def __init__(self, name, last, grades):
        self.name = name
        self.last = last
        self.grades = grades

    def __repr__(self):
        return self.name.capitalize() + " " + self.last.capitalize()

    def email(self):
        return f'{self.last}.{self.name}@{self.university}.com'

    @property
    def nickname(self):
        return self.name + '***'

    @property
    def fullname(self):
        return f'{self.name.capitalize()} {self.last.capitalize()}'

    @fullname.setter
    def fullname(self, name_last):
       self.name, self.last = name_last.split()

    @fullname.deleter
    def fullname(self):
        self.name, self.last = None, None

    # def del_fullname(self):
    #     self.name = None
    #     self.last = None


    def grand_scholarship(self):
        if self.grades > self.min_avg:
            print("You get scholarship")
        else:
            print("Not this time")

    @classmethod
    def set_new_avg(cls, new_value):
        cls.min_avg = new_value

    @classmethod
    def set_university_name(cls, new_name):
        cls.university = new_name

    @staticmethod
    def get_salary_net_under_26(salary_gross):
        """returns salary netto annually"""
        if salary_gross < 85000:    # PIT 0%
            return salary_gross
        else:                       # wejście w próg podatkowy
            return 85000 + (salary_gross - 85000) * 0.83

    @staticmethod
    def is_academic_day(day):
        is_weekend = day.weekday() in [5, 6]

        free_days_pl = Poland()
        is_free_day = day in free_days_pl

        return not is_weekend and not is_free_day




def main():
    obj_anna = Student('anna', 'kowalska', 4.72)
    obj_michal = Student('michal', 'nowak', 4.69)
    #
    # eg_date = datetime.datetime.strptime('2022-01-06', '%Y-%m-%d')
    # print('Czy dzisiaj idziemy na uczelnię?', obj_michal.is_academic_day(eg_date))

    obj_ann = Student('anna', 'smith', 4.0)
    # print(obj_ann.nickname)
    # print(obj_ann.last)
    # print(obj_ann.nickname)
    # print(obj_ann)
    # print(obj_ann.email())
    obj_ann.name = 'ann'

    print(obj_ann.fullname)

    print('Zmiana stanu cywilnego')
    obj_ann.fullname = 'Anna Snow'
    print(obj_ann.name)
    print(obj_ann.last)

    print('USUWAM BO RODO!!!')
    # obj_ann.del_fullname()
    # print(obj_ann.name)
    # print(obj_ann.last)

    del obj_ann.fullname
    print(obj_ann.name)
    print(obj_ann.last)


if __name__ == '__main__':
    main()














