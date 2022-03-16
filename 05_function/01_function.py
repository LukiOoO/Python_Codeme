# 1▹ Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję obliczającą bmi na podstawie danych użytkownika oraz zwracającą odpowiednią wartość (niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.

def calculate_BMI(weight, height):
    return weight / (height**2)



def ged_state(bmi):
    if bmi < 18:
        return "Niedowaga"
    elif bmi < 25:
        return "bmi w normie"
    elif bmi < 30:
        return "nadwaga"
    else:
        return "Otyłość"


def cheack_health(w,h):
    bmi_result = calculate_BMI(w,h)
    bmi_status = ged_state(bmi_result)
    return bmi_status



# glowan czesc skryptu




x = float(input("Podaj wage: "))
y = float(input("Podaj wzrost (m): "))

result = cheack_health(x,y)
print("Status BMI: ",result)
