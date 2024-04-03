import random

#42
print(random.getrandbits(32)) # Get a random integer having 32 bits (2^32)
level = random.randint(1, 3)
print(level)
fl = random.random() * 5
print(fl)

#43
print("Tails or Heads?")
rand_side = random.randint(0, 1)
if rand_side == 0:
    print(f"It's tails {rand_side}")
else:
    print(f"It's heads {rand_side}")

#44 lists
fruits = ["cherry", "apple", "pear"]
states_of_america = ["Delaware", "Pennsylvania", "New Jersey",
                     "Georgia", "Connecticut", "Massachusetts"]
print(states_of_america) #shows whole list
print(states_of_america[1]) #shows [1]
states_of_america[1] = "Pencilvania" #change [1] to Pencilvania
print(states_of_america) #shows changed list
states_of_america.extend(["Lalalend", "Angelaland"])
print(states_of_america) #shows changed list with new added value

#45 who pay bill
names = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe', 'Dan']
whopay = random.randint(0, len(names)-1) #-1 because it might be overflow (len 6, but index 0-5)
print(f"{names[whopay]} is going to buy the meal today! number [{whopay}] in list")

#46 add one list to another
fruit_list = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetable_list = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dozen_dirty = [fruit_list + fruit_list]
print(dozen_dirty)

#quiz
#what will show in print(fruitss)?
fruitss = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruitss[-1] = "Melons" #-1 its last element in list -> replace by "Melons"
fruitss.append("Lemons") #and in the end of list "Lemons"
print(fruitss)
#what will be printed?
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][1]) #1 its second list(vegetables). 1 its second element in second list ("Kale")

#47 Treasure MAP
line1 = [" ", "️ ", "️️ "]
line2 = [" ", " ", "️ "]
line3 = [" ", " ", "️ "]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1])-1
map[number_index][letter_index] = "X"
print(f"{line1}\n{line2}\n{line3}")

#===my version is totally failed:=========
# number_of_list = str(position[0]) #b3
# if (position > 'A1' or 'B1' or 'C1'):
#   line1[number_of_list-1] = 'X'
# elif (position > 'A2' or 'B2' or 'C2'):
#   line2[number_of_list-1] = 'X'
# elif (position > 'A3' or 'B3' or 'C3'):
#   line3[number_of_list-1] = 'X'
# =========================================

#48 Project Rock, Paper, Scissors (didn't finished yet)
