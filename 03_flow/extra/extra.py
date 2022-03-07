print("Witamy w python pizza! ")

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1
#
# Example Input
# - size = "L"
# - add_pepperoni = "Y"
# - extra_cheese = "N"
#

# additional = input("")
bill = 0
pizza_size = input("Jaki rozmiar pizzy chcesz? S,M,L: ")
add_pepperoni = input("Czy chcesz dodatkowe pepperoni? Y czy N ")
ectra_cheese = input("Chcesz dodatkowy ser? Y czy N ")



if pizza_size == "S":
    bill += 15
elif pizza_size == "M":
    bill += 20
elif pizza_size == "L":
    bill += 25

if add_pepperoni == "Y":
    if pizza_size == "S":
        bill += 2
    else:
        bill += 3
if ectra_cheese == "Y":
    bill += 1
else:
    bill += 0
print("Twoja pizza kosztuje:", bill)