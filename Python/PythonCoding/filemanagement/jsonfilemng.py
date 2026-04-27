import json
import os

# Step 1: Create a new JSON file and write data
filename = "example.json"

# Data to write
data = [
    {"Name": "Alice", "Age": 30, "City": "New York"},
    {"Name": "Bob", "Age": 25, "City": "London"},
    {"Name": "Charlie", "Age": 35, "City": "Paris"}
]

# Write data to JSON file
with open(filename, "w") as f:
    json.dump(data, f, indent=4)

print(f"{filename} created and data written.")

# Step 2: Read from the JSON file
with open(filename, "r") as f:
    loaded_data = json.load(f)

print("Reading data from JSON:")
for person in loaded_data:
    print(person)

# Step 3: Delete the JSON file
# if os.path.exists(filename):
#     os.remove(filename)
#     print(f"{filename} has been deleted.")
# else:
#     print("File does not exist.")
