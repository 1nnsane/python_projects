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