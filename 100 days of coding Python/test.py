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

#my version is totally failed:
# number_of_list = str(position[0]) #b3
# if (position > 'A1' or 'B1' or 'C1'):
#   line1[number_of_list-1] = 'X'
# elif (position > 'A2' or 'B2' or 'C2'):
#   line2[number_of_list-1] = 'X'
# elif (position > 'A3' or 'B3' or 'C3'):
#   line3[number_of_list-1] = 'X'