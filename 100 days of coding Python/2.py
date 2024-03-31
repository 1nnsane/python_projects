#DAY 2 COURSE
#= 19 lesson ==================================================

#Data Types
#Boolean: True(1), False (0)
print("Number of letters: ", len("word i use")) #string
int_numbers = 123456 #integer
float_numbers = 3.1454325 #float
arrays_example = "Abbey Road" #for example with arrays [4]+[7] = yo

sum_big_integers = 123_456_789 + 876_543_211 # "_" just a human readable format, dont affect to code
float_sum = 3.1454 + 0.8546
print("Sum of integer numbers: ", sum_big_integers)
print("Sum of float numbers: ", float_sum)
print("Sum of indexes in arrays: ", arrays_example[4] + arrays_example[7])
print("Examples with '_' for numbers: ", 734_529.678 + 100.5) #its 734529.678+100.5

#= 20 lesson ==================================================
num_char = len(input("what is your name?:\n"))
print("Method 1 - Your name has an:", num_char, "characters") #works because of ","

#print("ur name has an:" + num_char + "characters") #giver error, because
#we trying to use - string (name) + ing (len charasters of name) = we cant sum integers with strings
print("Type of num_char (len of name):", type(num_char))
new_num_char = str(num_char)
print("==================================================")
print("Type of new_num_char (len of name):", type(new_num_char))
print("Method 2 - Your name has an: " + new_num_char + " characters") #giver error, because

#= 21 lesson project ==========================================
#input 39 -> output 12(3+9) || input 43 -> output 7(4+3)
two_digit_numbers = input() #get string -> 39,42
#Method 1
print(type(two_digit_numbers)) #39 or 42 = str
print(two_digit_numbers[0] + two_digit_numbers[1])
print("Method 1: ", int(two_digit_numbers[0]) + (int(two_digit_numbers[1])))

#Method 2 (more readable)
first_digit = int(two_digit_numbers[0])
second_digit = int(two_digit_numbers[1])
print("Method 2: ", first_digit + second_digit)

#= 22 Mathematical Operations =================================
#priority -> first "()", second "**", thirth "*" or "/", forth "+" or "-"
print(3 * 3 + 3 / 3 - 3) #7.0
print(3 * (3 + 3) / 3 - 3) #3.0

#= 23 BMI Calculator ==========================================
height = float(input("ur height: ")) #1.75(metres)
weight = int(input("ur weight: ")) #80(kg)
bmi = (weight/height**2)
print(bmi) #print float number
print(int(bmi)) #print int number

#= 24 Number Manipulation and F Strings =======================
print(8/3) #gives float number 2.6666666666666665
print(8//3) #chop numbers after "." = 2
print(round(8/3)) #round to bigger or smaller number = 3
print(round(8/3,3)) #round number, and gives 3 numbers and "." = 2.667

name = "Diko"
isWinning = True
height = 1.8
score = 0
score += 2 # or (-=, *=, /=)
print(score)
#to print 2 and more data types, its neccesary to give them one data type - which is not comfortable
#then we using f-string
print(f"Ur score is {score}, ur name is {name}, u are winning is {isWinning}, and ur height is {height}")

#= 25 Life in Weeks calculator =======================
age = int(input("Ur age?: "))
weeks_in_year = 365//7
total_weeks = 90 * weeks_in_year
left_weeks = (total_weeks - (age * weeks_in_year))

print(f"U got a totally: {total_weeks} weeks")
print(f"U have left: {left_weeks} weeks")

#= 26 Project Tip Calculator =======================
print("You using a tip Calculator")
total_bill = float(input("What was your total bill?: "))
tips_total = float(input("What the procent of tips u want left?: "))
amount_people = float(input("for many people eat?: "))
tips_per_each = ((total_bill/100) * tips_total)

#Method 1, answer =  33.6 b
total_for_each = round(((total_bill+tips_per_each)/amount_people), 2)
print("Method 1: Each have to pay:", total_for_each)

#Method 2, answer = 33.60 by using - "{:.2f}".format()
total_for_each = "{:.2f}".format(((total_bill+tips_per_each)/amount_people))
print("Method 2: Each have to pay:", total_for_each)