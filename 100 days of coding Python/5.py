import random

#51 for loop
fruits = ["apple", "cherry", "strawberry"]
for fruit in fruits:
    print(fruit)

#52
# Input a Python list of student heights:
student_heights = input().split() #195 154 184 in one line
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

#Source code:
totalheight = 0
totalstudent = 0

for i in range(0, len(student_heights)):
    totalheight += student_heights[i]
    # print(totalheight)
for i in range(0, len(student_heights)):
    totalstudent += 1
    # print(totalstudent)

averageheight = round(totalheight / totalstudent)
print(f"total height = {totalheight}")
print(f"number of students = {totalstudent}")
print(f"average height = {averageheight}")

#53
# Input a list of student scores:
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

#Source code:
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"The highest score in the class is: {highest_score}")

# 54
total = 0
for i in range(1, 101): #Gauss (1+2+3+4+...+96+97+98+99+100)
    total += i
    print(f"{i}: total: {total}")

# 55
target = int(input()) # Enter a number between 0 and 1000
#Source code (Method 1):
even_sum = 0
for number in range (2, target + 1, 2):
  even_sum += number
print(even_sum)
##Source code (Method 2):
alternative_sum = 0
for number in range(1, target + 1):
  if number % 2 == 0:
    alternative_sum += number
print(alternative_sum)

#56
for i in range (1, 101):
    if i % 15 == 0: #if start from 3 or 5 code will not print FizzBuzz
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

# 57 Final project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for i in range(0, nr_letters):
    password_list.append(random.choice(letters))
    # random_letter = random.choice(letters)
    # password_list += random_letter
for i in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
    # nr_symbols = random.choice(symbols)
    # password_list += nr_symbols
for i in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
    # nr_numbers = random.choice(numbers)
    # password_list += nr_numbers

print(password_list) #before random chars
random.shuffle(password_list) #random chars
print(password_list) #result of randam password inside list

password = "" #to delete [] and convert to one string
for i in password_list:
    password += i
print(password) #result of randam string password

