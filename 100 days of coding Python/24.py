# Work with files: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# Reading methods:
# 1 method working with files
file = open("readme.txt")  # set up to read always "r"
contents = file.read()
print(contents)
file.close()  # close when don't need it
# 2 method
with open("readme.txt") as file:  # when we finish work with file, it will close automatically
    content = file.read()
    print(content)

# Write, edit methods
# #method 1
# with open("readme.txt", "w") as file:  # delete all info in file and replace what u need
#     file.write("New text")
# #method 2
# with open("new_readme.txt", "w") as file:  # if file doesn't exist, it will create for u
#     file.write("New text")

