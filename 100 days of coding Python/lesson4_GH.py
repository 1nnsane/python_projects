# 4.3.1 Sum an array
array1 = [1, 2, 3, 4, 5]
array2 = [6, 7, 8, 9, 10]
array1_and_2 = array1 + array2  # just adding list of array1 and array2
print(array1_and_2)

sum_of_array = 0
for i in range(0, len(array1)):
    # adding items of: array1[0] + array2[0] = 7, array1[1] + array2[2] = 9 ...
    sum_of_array = array1[i] + array2[i]
    print(sum_of_array)
print("==========================================================")

# 4.3.2 Reverse an array
array1 = [1, 3, 5, 4, 2]
print(array1)

reverse_array = array1[::-1]
print(reverse_array)

# 4.3.3 Check if array is palindromic
polin = False
if array1 == array1[::-1]:
    polin = True
else:
    polin = False
print(f"array: {array1} is palindromic: {polin}")

# 4.3.4 Remove duplicates from a sorted array
# Don't working if duplicates in the middle of list
array_sorted = [1, 2, 3, 4, 5, 5]
print(f"Current list {array_sorted}")
answer = False

for i in range(0, len(array_sorted)):  # len = 0-5 (6)
    if array_sorted[i] == len(array_sorted):
        break
    else:
        if array_sorted[i] == array_sorted[i-1]:
            answer = True
            array_sorted.pop()
        else:
            answer = False

print(f"Find duplicate: {answer}")
print(f"This List {array_sorted} with no duplicates")

