import random
#https://docs.python.org/3/tutorial/datastructures.html data structures documentation

#lower(), upper
name = "CrisTIAno RONALdo"
n = name.lower(); print(n)
nn = name.upper(); print(nn)

#len()
x = len('helloworld'); print(x)

#random library
random.randint(1, 3) #first - import random. random int numbers from 1 to 3
random.random() * 5 #random float number till from 0 to 5 (because divide to 5), other wise 0-1.0

#lists
fruits = ["banana", "cherry", "pineapple"]; print(fruits)
vegetables = ["tomato", "potato", "spinach"]
mix = [fruits + vegetables]; print(mix)
#add to existing list "apple"
fruits.append("apple"); print(fruits)

#for loop
for number in range (0, 10): #from 0 to 9 (not include 10)
    print(number) #0-9
for number in range (0, 10, 2): #3th number it's a step: +2
    print(number) #0,2,4,6,8
#for item in list_of_items:     method 1
    #do something
#for number in range(a, b)      method 2
    #print(number)

#while loop
#while something_is_true:
    #do something repeatedly
a = 2
while a != 5: #or while not 5:
    print("hi")
    a += 1

#shuffle
x = [1, 2, 3, 4, 5]
random.shuffle(x)
print(x)

#function def
def name_of_function(var1, var2):
    summary = var1 + var2
    print(summary)
name_of_function(5,2)


print ("hellO worlD")

message = "hellO worlD"
print (message.title())

message = "hellO worlD"
print (message.upper())

message = "hellO worlD"
print (message.lower())