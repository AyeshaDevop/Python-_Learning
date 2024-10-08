#Dictionary
# Create a dictionary
# student = {
#     "name": "Ayesha",
#     "age": 19,
#     "subjects": ["che","phy","eng"]}

# # Access a value by its key
# print(student["name"])  # Output: Ayesha


# # Add a new key-value pair
# student["school"] = "Peak school"

# # Update a value
# student["grade"] = "13"

# # Delete a key-value pair
# del student["age"]

# # Print the updated dictionary
# print(student)
 
 #Set in python
# Using curly braces
# set1 = {1, 2, 3, 4, 5}
# print(set1)

# Using the set() function
# set2 = set([2, 4, 6, 8])
# print(set2)

# print(type(set1))

# Creating sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Add an element
set_a.add(6)
print("After adding 6 to set_a:", set_a)

# Remove an element
set_a.remove(1)
print("After removing 1 from set_a:", set_a)

# Union of sets (all unique elements from both sets)
union_set = set_a.union(set_b)
print("Union of set_a and set_b:", union_set)

# Intersection of sets (common elements)
intersection_set = set_a.intersection(set_b)
print("Intersection of set_a and set_b:", intersection_set)

# Difference of sets (elements in set_a but not in set_b)
difference_set = set_a.difference(set_b)
print("Difference of set_a and set_b:", difference_set)


