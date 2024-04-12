#92 Dictionary
programming_dictionary = {
    "Bug": "It is bug #404",
    "Function": "Some Function",
    "Loop": "Repeating "
}

print(programming_dictionary)
programming_dictionary ["Hello"] = "Adding: Hello" #add KEY
print(programming_dictionary)

for i in programming_dictionary: #gives just KEYs of example_dictionary
    print(i) #Bug, Function, Loop, New
for key in programming_dictionary:
    print(key) #print KEY
    print(programming_dictionary[key]) #print VALUE of KEY (Bug: "It is bug #404")

programming_dictionary = {} #empty dictionary
print(programming_dictionary)