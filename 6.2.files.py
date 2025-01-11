# Part 1: Basic File Operations and Data Structures in Python
# This demonstration shows how to work with files and various data types in a bookstore management system

# First, let's import the required modules
import os
from datetime import datetime

# File paths using relative paths - This helps maintain portability of our code
# Updated paths with the correct structure
# The paths should match your exact directory structure
# File paths using absolute paths for GitHub Codespaces
INVENTORY_FILE = "/workspaces/python_with_vit/6.files/bookstore_manager/data/inventory.txt"
SALES_FILE = "/workspaces/python_with_vit/6.files/bookstore_manager/data/sales.csv"
REVIEWS_FILE = "/workspaces/python_with_vit/6.files/bookstore_manager/data/reviews.txt"
BACKUP_DIR = "/workspaces/python_with_vit/6.files/bookstore_manager/data/backup"
REPORTS_DIR = "/workspaces/python_with_vit/6.files/bookstore_manager/reports"
TEMP_DIR = "/workspaces/python_with_vit/6.files/bookstore_manager/temp"


# Let's start by checking if our files exist
print("\n1. Basic File and Directory Operations")
print("-" * 40)

# The os.path module helps us work with file paths
for file_path in [INVENTORY_FILE, SALES_FILE, REVIEWS_FILE]:
    if os.path.exists(file_path):
        # Get file information
        file_size = os.path.getsize(file_path)  # Size in bytes
        file_modified = os.path.getmtime(file_path)  # Modification time as timestamp
        modified_date = datetime.fromtimestamp(file_modified).strftime('%Y-%m-%d %H:%M:%S')
        
        print(f"File: {file_path}")
        print(f"Size: {file_size} bytes")
        print(f"Last modified: {modified_date}")
        print("-" * 40)

# Basic file reading operations
print("\n2. Reading Files - Different Methods")
print("-" * 40)

# Method 1: Reading entire file at once
print("Method 1: Reading entire file")
with open(INVENTORY_FILE, 'r') as file:
    content = file.read()
    print("First 150 characters of inventory:")
    print(content[:150])
    print("-" * 40)

# Method 2: Reading line by line
print("\nMethod 2: Reading line by line")
with open(INVENTORY_FILE, 'r') as file:
    # Skip header line
    header = file.readline()
    # Read first 3 lines
    for _ in range(3):
        line = file.readline().strip()
        print(f"Book record: {line}")
print("-" * 40)

# Method 3: Reading all lines at once into a list
print("\nMethod 3: Reading all lines into a list")
with open(INVENTORY_FILE, 'r') as file:
    lines = file.readlines()
    print(f"Total number of lines: {len(lines)}")
    print(f"Header: {lines[0].strip()}")
print("-" * 40)

# Let's create a simple data structure to store our inventory
print("\n3. Creating Data Structures from File Data")
print("-" * 40)

# Dictionary to store inventory (ISBN as key)
inventory_dict = {}
# List to store all books
inventory_list = []
# Set to store unique genres
genres_set = set()
# Tuple to store price range (min_price, max_price)
price_range = (float('inf'), float('-inf'))

# Reading and processing inventory data
with open(INVENTORY_FILE, 'r') as file:
    # Skip header
    header = file.readline().strip().split('|')
    
    # Process each line
    for line in file:
        # Split the line by delimiter and create a dictionary for each book
        data = line.strip().split('|')
        book = dict(zip(header, data))
        
        # Convert price and quantity to appropriate types
        book['Price'] = float(book['Price'])
        book['Quantity'] = int(book['Quantity'])
        
        # Update our data structures
        inventory_dict[book['ISBN']] = book
        inventory_list.append(book)
        genres_set.add(book['Genre'])
        
        # Update price range tuple
        price_range = (min(price_range[0], book['Price']), 
                      max(price_range[1], book['Price']))

# Display our data structures
print("Dictionary Example (First ISBN):")
first_isbn = list(inventory_dict.keys())[0]
print(inventory_dict[first_isbn])

print("\nList Example (First 2 books):")
print(inventory_list[:2])

print("\nUnique Genres (Set):")
print(genres_set)

print("\nPrice Range (Tuple):")
print(f"Minimum Price: ${price_range[0]:.2f}")
print(f"Maximum Price: ${price_range[1]:.2f}")

# Basic file writing demonstration
print("\n4. Writing to Files")
print("-" * 40)

# Create a simple report
report_file = os.path.join(REPORTS_DIR, "inventory_summary.txt")
with open(report_file, 'w') as file:
    file.write("Inventory Summary Report\n")
    file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write("-" * 40 + "\n")
    file.write(f"Total number of books: {len(inventory_list)}\n")
    file.write(f"Number of genres: {len(genres_set)}\n")
    file.write(f"Price range: ${price_range[0]:.2f} - ${price_range[1]:.2f}\n")
    
print(f"Report generated: {report_file}")

# File appending demonstration
print("\n5. Appending to Files")
print("-" * 40)

# Create a log file in the temp directory
log_file = f"{TEMP_DIR}/operation_log.txt"
with open(log_file, 'a') as file:
    log_entry = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Processed {len(inventory_list)} inventory items\n"
    file.write(log_entry)

print(f"Log updated: {log_file}")