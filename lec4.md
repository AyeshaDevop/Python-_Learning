#Dictionary
# Create a dictionary
student = {
    "name": "Ayesha",
    "age": 19,
    "grade": "12",
    "subjects": ["Math", "phy", "che"]
}

print(student["name"])  # Output: Ayesha

# Update a value
student["grade"] = "13"

# Delete a key-value pair
del student["age"]

# Print the updated dictionary
print(student)
