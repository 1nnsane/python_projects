#31 lesson
height = int(input("What is your height?: "))
if height < 120:
    print("Ur height is under 120, you can't drive")
else:
    print("Ur height is more than 120, you can drive")

#32 lesson odd or even
num = int(input("I can say if ur number is odd or even. Put number: "))
if num % 2 == 0:
    print("odd")
else:
    print("even")

height = int(input("What is your height?: "))
if height >= 120:
    print("You can drive")
    age = int(input("What is your age? We have a discounts: "))
    if age >= 18:
        print("Price for you is: 12$")
    elif age < 12:
        print("Price for you is: 5$")
    else:
        print("Price for you is: 7$")
else:
    print("Ur height is under 120, you can't drive")

#33 bmi 2.0
height = float(input("I'm calculating BMI. Put ur height(format = 1.75m): ")) #1.75(metres)
weight = int(input("Put ur weight: ")) #80(kg)
bmi = (weight/height**2)
#print(f"Ur bmi is {round(bmi, 2)}") #print int number

if bmi <= 18.28678:
    print(f"Ur bmi is {round(bmi, 2)}. you are underweight")
elif bmi <= 22.0:
    print(f"Ur bmi is {round(bmi, 2)}. you have a normal weight")
elif bmi <= 28.50752:
    print(f"Ur bmi is {round(bmi, 2)}. you are slightly overweight")
elif bmi <= 32.56189:
    print(f"Ur bmi is {round(bmi, 2)}. you are obese")
else:
    print(f"Ur bmi is {round(bmi, 2)}. you are clinically obese")

#34 LEAP YEAR COUNTER
year = int(input("Leap year counter. Put year: "))
if year % 100 == 0:
    print("Not leap year")
elif year % 4 == 0 or year % 400 == 0:
    print("Leap year")
else:
    print("Not leap year")

#35 program (U can drive, age, total bill with photo)
height = int(input("What is your height?: "))
bill = 0
if height >= 120:
    age = int(input("You can drive, what is your age? We have a discounts: "))
    if age >= 18:
        print("Adult ticket is: 12$.")
        bill += 12
    elif age < 12:
        print("Child ticket is: 5$")
        bill += 5
    else:
        print("Youth ticket is: 7$")
        bill += 7

    print("Do u want add a photo?(yes/no): ")
    want_photo = input()
    if want_photo == 'yes':
        bill += 3
    print(f"Ur total bill is: ${bill}")
else:
    print("Ur height is under 120, you can't drive")

#36 Pizza order
print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25

if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    elif size == 'M' or 'L':
        bill += 3

if extra_cheese == 'Y':
    bill += 1
print(f"Your final bill is: ${bill}.")

# 37 Logical Operators
height = int(input("What is your height?: "))
bill = 0
if height >= 120:
    age = int(input("You can drive, what is your age? We have a discounts: "))
    if age < 12:
        print("Child ticket is: 5$")
        bill = 5
    elif age <= 18:
        print("Youth ticket is: 7$.")
        bill = 7
    elif age >= 45 & age <= 55:  # problem = even is older than 56 its getting for free, must be free only for 45-55 y.o.
        print("Free")
    else:
        print("Adult ticket is: 12$.")
        bill = 12

    print("Do u want add a photo?(yes/no): ")
    want_photo = input()
    if want_photo == 'yes':
        bill += 3
    print(f"Ur total bill is: ${bill}")
else:
    print("Ur height is under 120, you can't drive")

#lesson 38 (LOVE CALCULATOR) NEED TO MAKE MORE READABLE!!!
print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
lowname1 = name1.lower()
lowname2 = name2.lower()
# print(lowname1)
# print(lowname2)

# print(list(lowname1))
# print(list(lowname2))
count_t = lowname1.count('t') + lowname2.count('t')
count_r = lowname1.count('r') + lowname2.count('r')
count_u = lowname1.count('u') + lowname2.count('u')
count_e = lowname1.count('e') + lowname2.count('e')
count_l = lowname1.count('l') + lowname2.count('l')
count_o = lowname1.count('o') + lowname2.count('o')
count_v = lowname1.count('v') + lowname2.count('v')
count_e = lowname1.count('e') + lowname2.count('e')

# print(f"t = {count_t}, r = {count_r}, u = {count_u}, e = {count_e}")
# print(f"T = {count_t}, R = {count_r}, U = {count_u}, E = {count_e}")
# print(f"L = {count_l}, O = {count_o}, V = {count_v}, E = {count_e}")

sumtrue = count_t + count_r + count_u + count_e
sumlove = count_l + count_o + count_v + count_e
final = str(sumtrue) + str(sumlove)
# print(int(final))

# something works wrong with if statements (my version)
# how to implement do 2 statement only if (>40 and <50)
# how to iplement and
if int(final) < 10 and int(final) > 90:
    print(f"Your score is {final}, you go together like coke and mentos.")
elif int(final) > 40 and int(final) < 50:
    print(f"Your score is {final}, you are alright together.")
else:
    print(f"Your score is {final}.")

# true version from udemy:
# if int(final) < 10 or int(final) > 90:
#   print(f"Your score is {final}, you go together like coke and mentos.")
# elif int(final) >= 40 and int(final) <= 50:
#   print(f"Your score is {final}, you are alright together.")
# else:
#   print(f"Your score is {final}.")


#39 FINAL PROJECT 3 BOORING PROJECT WITH IF ELSE STATEMENTS GAME (IF U GO RIGHT U DIE, LEFT U OPEN NEW LVL...
