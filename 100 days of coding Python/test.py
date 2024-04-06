import random
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
