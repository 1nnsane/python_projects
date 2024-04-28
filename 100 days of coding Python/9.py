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

#93
# Dictionary with student scores
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# Create an empty dictionary student_grades.
student_grades = {}
# Add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)

#94 Nesting Lists and Dictionaries
#Nesting
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}
print(capitals)

#Nesting a List in a Dictionary
travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}
print(travel_log)

#Nesting Dictionary in a Dictionary
travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}
print(travel_log)

#Nesting Dictionaries in Lists
travel_log = [
{
  "country": "France",
  "cities_visited": ["Paris", "Lille", "Dijon"],
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]
print(travel_log)


#95
country = input()  # Add country name: (Brazil)
visits = int(input())  # Number of visits: (2)
list_of_cities = eval(input())  # create list from formatted string: (["Sao Paulo", "Rio de Janeiro"])

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# Do NOT change the code above 👆
# TO_DO: Write the function that will allow new countries to be added to the travel_log.
def add_new_country(names, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = names
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)
# Do not change the code below 👇

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")

#97 Project