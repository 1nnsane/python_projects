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
