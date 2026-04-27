import csv
import os


import csv
import os

# Step 1: Create and write to a CSV file
filename = "example.csv"

with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(["Name", "Age", "City"])
    # Write some rows
    writer.writerow(["Alice", 30, "New York"])
    writer.writerow(["Bob", 25, "London"])
    writer.writerow(["Charlie", 35, "Paris"])

print(f"{filename} created and data written.")

# Step 2: Read from the CSV file
with open(filename, mode="r") as file:
    reader = csv.reader(file)
    print("Reading data from CSV:")
    for row in reader:
        print(row)

# Step 3: Delete the CSV file
if os.path.exists(filename):
    os.remove(filename)
    print(f"{filename} has been deleted.")
else:
    print("File does not exist.")
