# Basic reading operations
# Read entire file at once
content = open('/workspaces/python_with_vit/6.files/bookstore_manager/data/inventory.txt').read()

# Read file line by line
for line in open('/workspaces/python_with_vit/6.files/bookstore_manager/data/inventory.txt'):
    print(line.strip())

# Read all lines into a list
lines = open('/workspaces/python_with_vit/6.files/bookstore_manager/data/review.txt').readlines()

# Basic writing operations
# Write string to file (overwrites existing content)

open('/workspaces/python_with_vit/6.files/bookstore_manager/temp/test.txt', 'w').write('Hello, World!')

# Append string to a file
open('/workspaces/python_with_vit/6.files/bookstore_manager/temp/test.txt', 'a').write('New log entry\n')

# Write multiple lines at once
open('/workspaces/python_with_vit/6.files/bookstore_manager/temp/test.txt', 'w').writelines(['Line1\n', 'Line2\n'])

# Create a simple text file for testing
# Read and print the contents
test_file = '/workspaces/python_with_vit/6.files/bookstore_manager/temp/sample.txt'
# open(test_file, 'w').write('First line\nSecond Line\nThird Line')
# print(open(test_file, 'r').read())

# Using context manager (better practice):
with open(test_file, 'r') as file:
    print("File contents:")
    print(file.read())


# Create a numbered list file
number_file = '/workspaces/python_with_vit/6.files/bookstore_manager/temp/numbers.txt'
open(number_file, 'w').write('1\n2\n3\n4\n5\n')

# Create a CSV-style file
data_file = '/workspaces/python_with_vit/6.files/bookstore_manager/temp/data.csv'
open(data_file, 'w').write('name,age\nJohn,30\nJane,25\n')

# Reading specific number of characters
first_10 = open(test_file).read(10)

# More explicit version of the same opereation
file_object = open(test_file)
content = file_object.read(10)
file_object.close()

# Better practice using 'with' statement (auto closes the file)
with open(test_file) as file_object:
    content_10 = file_object.read(10)
    content_20 = file_object.read(20)

# Reading specific line
specific_line = open(test_file).readlines()[1]
