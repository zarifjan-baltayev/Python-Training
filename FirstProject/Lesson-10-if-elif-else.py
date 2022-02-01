

age = 4
gender = "male"

if (age > 4) and (age < 9):
    if gender == "female":
        print("This is HATIJE!")
    else:
        print("Not HATIJE!")
else:
    print("This is not HATIJE!")


age1 = 103

if (age1 > 0) and (age1 < 12):
    print("You are kid!")
elif (age1 >= 12) and (age1 < 19):
    print("You are teenager!")
elif (age1 >= 19) and (age1 < 102):
    print("You are adult!")
else:
    print("You are out of age range!")


cars = ['Chrysler', 'Honda', 'Bugatti', 'BMW', 'Mercedes', 'Audi', 'Renault',
         'Ford', 'Seat', 'Kia', 'Dacia']
german_cars = ['BMW', 'Mercedes', 'Audi']

car = "toyota"
if car in cars:
    print("Yes " + car.upper() + " is in the cars list!")
else:
    print("The "  + car.upper() + " not found in the list!")


for x in cars:
    if x in german_cars:
        print(x + " is German car!")
    else:
        print(x + " is NOT German car!")
