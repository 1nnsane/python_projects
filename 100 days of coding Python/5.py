#51 for loop
fruits = ["apple", "cherry", "strawberry"]
for fruit in fruits:
    print(fruit)

#52
# Input a Python list of student heights
student_heights = input().split() #195 154 184 in one line
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
#code 👇

totalheight = 0
for i in range(0, len(student_heights)):
    totalheight += student_heights[i]
    # print(totalheight)

totalstudent = 0
for i in range(0, len(student_heights)):
    totalstudent += 1
    # print(totalstudent)

averageheight = round(totalheight / totalstudent)

print(f"total height = {totalheight}")
print(f"number of students = {totalstudent}")
print(f"average height = {averageheight}")