print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
lowname1 = name1.lower()
lowname2 = name2.lower()
#print(lowname1)
#print(lowname2)

#print(list(lowname1))
#print(list(lowname2))
count_t = lowname1.count('t') + lowname2.count('t')
count_r = lowname1.count('r') + lowname2.count('r')
count_u = lowname1.count('u') + lowname2.count('u')
count_e = lowname1.count('e') + lowname2.count('e')
count_l = lowname1.count('l') + lowname2.count('l')
count_o = lowname1.count('o') + lowname2.count('o')
count_v = lowname1.count('v') + lowname2.count('v')
count_e = lowname1.count('e') + lowname2.count('e')

#print(f"t = {count_t}, r = {count_r}, u = {count_u}, e = {count_e}")
#print(f"T = {count_t}, R = {count_r}, U = {count_u}, E = {count_e}")
#print(f"L = {count_l}, O = {count_o}, V = {count_v}, E = {count_e}")

sumtrue = count_t + count_r + count_u + count_e
sumlove = count_l + count_o + count_v + count_e
final = str(sumtrue) + str(sumlove)
#print(int(final))

#something works wrong with if statements (my version)
#how to implement do 2 statement only if (>40 and <50)
#how to iplement and
if int(final) < 10 and int(final) > 90:
  print(f"Your score is {final}, you go together like coke and mentos.")
elif int(final) > 40 and int(final) < 50:
  print(f"Your score is {final}, you are alright together.")
else:
  print(f"Your score is {final}.")

#true version from udemy:
# if int(final) < 10 or int(final) > 90:
#   print(f"Your score is {final}, you go together like coke and mentos.")
# elif int(final) >= 40 and int(final) <= 50:
#   print(f"Your score is {final}, you are alright together.")
# else:
#   print(f"Your score is {final}.")
