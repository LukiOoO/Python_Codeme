from student import Student
from salary_info import get_salary_net_under_26

ana = Student('Anna', 'Smith', 4.5)

a = Student.get_salary_net_under_26(70_000)
print(a)
s = get_salary_net_under_26(70000)
print(s)