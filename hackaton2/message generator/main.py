import csv


# names = input("Enter names separated by commas: ").title().split(",")
# tasks = input("Enter task counts separated by commas: ").split(",")
# grades = input("Enter grades separated by commas: ").split(",")


def name_surname():
    o = []
    try:
        with open("students.csv", "r", encoding="utf-8") as cs_f:
            csv_reader = csv.reader(cs_f)
            for line in csv_reader:
                o.append(line[1] + " " + line[2])




    except FileNotFoundError:
        print("Nie ma takiego pliku")

    return o


def tasks():
    t = []
    try:
        with open("students.csv", "r", encoding="utf-8") as cs_f:
            csv_reader = csv.reader(cs_f)
            for line in csv_reader:
                t.append(line[3])



    except FileNotFoundError:
        print("Nie ma takiego pliku")

    return t


def rating():
    r = []
    try:
        with open("students.csv", "r", encoding="utf-8") as cs_f:
            csv_reader = csv.reader(cs_f)
            for line in csv_reader:
                r.append(line[4])

    except FileNotFoundError:
        print("Nie ma takiego pliku")

    return r


#
# m = f"Hi {a},\n\nThis is a reminder that you have {b} tasks left to \
# submit before you can graduate. You're current grade is {c} and can increase \
# to {d} if you submit all assignments before the due date.\n\n"


if __name__ == "__main__":
    for x, y, b in zip(name_surname(), rating(), tasks()):
        u = 20
        print(f"Hi {x},\n\nThis is a reminder that you have {b} tasks left to \
     submit before you can graduate. You're current grade is {y} and can increase \
      if you submit all assignments before the due date.\n\n")



