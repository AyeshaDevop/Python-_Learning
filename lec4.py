#Dictionary
# Create a dictionary
student = {
"name": "Ayesha",
"age": 19,
"subjects": ["che","phy","eng"]}

print(student["name"])  # Output: Ayesha


# # Add a new key-value pair
student["school"] = "Peak school"

# # Update a value
student["grade"] = "13"

# # Delete a key-value pair
del student["age"]

# # Print the updated dictionary
print(student)
 
 #Set in python
# Using curly braces
set1 = {1, 2, 3, 4, 5}
print(set1)

# Using the set() function
set2 = set([2, 4, 6, 8])
print(set2)

# print(type(set1))

# #  sets
set_1 = {1, 2, 3, 4, 5}
set_2 = {3, 4, 5, 6, 7}

set_1.add(6)
print("After adding 6 to set_1:", set_1)

set_1.remove(1)
print("After removing 1 from set_1:", set_1)

union_set = set_1.union(set_2)
print("Union of set_1 and set_2:", union_set)

intersection_set = set_1.intersection(set_2)
print("Intersection of set_1 and set_2:", intersection_set)

difference_set = set_1.difference(set_2)
print("Difference of set_1 and set_2:", difference_set)


