#DAY 1 COURSE
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
