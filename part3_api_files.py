#Task 1 File Read & Write Basics
print("\n" + "=" * 50)
print("Task 1 - File Read & Write Basics")
print("=" * 50)
#part A - Writing file
#initial comment given in question Q3

# File name that will be used in this task
file_name = "python_notes.txt"

#five lines in the file using write mode ('w'). Including encoding="utf-8".

# These are the five given lines from the assignment
notes = [
    "Topic 1: Variables store data. Python is dynamically typed.\n",
    "Topic 2: Lists are ordered and mutable.\n",
    "Topic 3: Dictionaries store key-value pairs.\n",
    "Topic 4: Loops automate repetitive tasks.\n",
    "Topic 5: Exception handling prevents crashes.\n"
]

# Writing the given lines using write mode ('w')
# using w mode here, so it will write fresh content
with open(file_name, "w", encoding="utf-8") as file:
    file.writelines(notes)

print("File written successfully.")

# These are two extra lines added by me as asked in the assignment
extra_notes = [
    "Topic 6: Functions improve code resuability.\n",
    "Topic 7: APIs allow communication between systems.\n"
]

# adding the extra lines in the same file
with open(file_name, "a", encoding="utf-8") as file:
    file.writelines(extra_notes)

print("Lines appended successfully.")


#Part B — Read:
#Read the file back and print each line numbered, stripping the trailing newline character (\n) from each line:
with open(file_name, "r", encoding="utf-8") as file:
    lines = file.readlines()  # Reads all lines into a list
    
#Count and print the total number of lines in the file.
    total_lines = len(lines)
print(f"Total number of lines: {total_lines}")

print("File Contents")

for index, line in enumerate(lines, start=1):
    # strip() removes newline character \n
    print(f"{index}. {line.strip()}")
    
#Ask the user for a keyword and print all lines that contain that keyword (case-insensitive). If no match is found, print a helpful message.

keyword = input("\nEnter keyword to search: ").lower() #put this so that it asks keyword only once.

found = False
print("\Search Results")

# Loop through lines AFTER getting input
for line in lines:
 if keyword in line.lower():
  print(line.strip())
  found = True
#after loop  
if not found:
  print("No lines found containing the keyword, try another keyword.")
    
    
#Task 2 — API Integration
print("\n" + "=" * 50)
print("TASK 2 - API INTEGRATION")
print("=" * 50)

import requests
from datetime import datetime

# Fetch and Display Products

# Base URL for the DummyJSON products API
base_url = "https://dummyjson.com/products"

print("\nStep 1: Fetching 20 products from the API...")
products = []

try:
    # getting 20 products from the API
    response = requests.get(f"{base_url}?limit=20", timeout=5)

    # checking if the request worked properly
    response.raise_for_status()

    # converting response into json format
    data = response.json()

    # taking the products list from the response
    products = data.get("products", [])

    print(f"{'ID':<4} | {'Title':<30} | {'Category':<15} | {'Price':<10} | {'Rating':<6}")
    print("-" * 80)

    for product in products:
        print(
            f"{product['id']:<4} | "
            f"{product['title'][:30]:<30} | "
            f"{product['category'][:15]:<15} | "
            f"{product['price']:<10} | "
            f"{product['rating']:<6}"
        )

except requests.exceptions.RequestException as e:
    print(f"Error while fetching products: {e}")
    products = []
        
# Filter and sort
print("\n" + "-" * 80)
print("Step 2: Filtering products with rating >= 4.5 and sorting by price (high to low)...")

# Only proceed if products were successfully fetched
if len(products) > 0:
    # Filtering products with rating >= 4.5
    filtered_products = []

    for product in products:
        if product.get("rating", 0) >= 4.5:
            filtered_products.append(product)

    # sorting the filtered products by price from high to low
    filtered_products = sorted(filtered_products, key=lambda item: item.get("price", 0), reverse=True)

    if len(filtered_products) > 0:
        print("\nFiltered and Sorted Products:\n")
        print(f"{'ID':<4} | {'Title':<30} | {'Category':<15} | {'Price':<10} | {'Rating':<6}")
        print("-" * 80)

        for product in filtered_products:
            product_id = product.get("id", "N/A")
            title = product.get("title", "N/A")
            category = product.get("category", "N/A")
            price = product.get("price", "N/A")
            rating = product.get("rating", "N/A")

            print(f"{product_id:<4} | {title[:30]:<30} | {category[:15]:<15} | ${price:<9} | {rating:<6}")
    else:
        print("No products found with rating greater than or equal to 4.5.")

else:
    print("Skipping Step 2 because product data was not fetched successfully.")
    

# Task 3 — Exception Handling 
print("\n" + "=" * 50)
print("TASK 3 - EXCEPTION HANDLING")
print("=" * 50)   


# here I am checking some common errors using try-except
# if something goes wrong, it will show the error message properly
# this also matches the theme of the assignment

# Part A — Guarded Calculator

print("\nPart A: Guarded Calculator")


# function to divide 2 values safely
# if division by zero or wrong input comes, it will return an error message
def safe_divide(a, b):
    try:
        result = a / b
        return result

    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

    except TypeError:
        return "Error: Invalid input types"


# Testing the function with the values given in the assignment
print("safe_divide(10, 2) =", safe_divide(10, 2))
print("safe_divide(10, 0) =", safe_divide(10, 0))
print('safe_divide("ten", 2) =', safe_divide("ten", 2))



# Part B — Guarded File Reader

print("\n" + "-" * 80)
print("Part B: Guarded File Reader")


# function to read a file safely
# if file is not found, it will show an error message
# finally block will run in both cases
def read_file_safe(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            return content

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

    finally:
        print("File operation attempt complete.")


# Testing with the file created in Task 1
print("\nReading 'python_notes.txt':")
notes_content = read_file_safe("python_notes.txt")

# If content is returned successfully, print it
if notes_content is not None:
    print(notes_content)

# Testing with a file that does not exist
print("\nReading 'ghost_file.txt':")
ghost_content = read_file_safe("ghost_file.txt")

if ghost_content is not None:
    print(ghost_content)



# Part C - Robust API Calls

print("\n" + "-" * 80)
print("Part C: Robust API Calls")

# in this part I am doing the API calls again with better error handling
# here I am checking connection issue, timeout, and wrong status code separately
# timeout=5 is used so the request does not wait too long


# GET request - Fetch 20 products

print("\nFetching 20 products with better error handling...")

robust_products = []

try:
    response = requests.get(f"{base_url}?limit=20", timeout=5)

    # checking if the API returned success
    if response.status_code == 200:
        data = response.json()
        robust_products = data.get("products", [])
        print("Products fetched successfully.")
    else:
        print(f"Request failed with status code: {response.status_code}")

except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet.")

except requests.exceptions.Timeout:
    print("Request timed out. Try again later.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")



# GET request - Laptops category

print("\nFetching laptops category with better error handling...")

try:
    laptop_response = requests.get(f"{base_url}/category/laptops", timeout=5)

    # checking if the API returned success
    if laptop_response.status_code == 200:
        laptop_data = laptop_response.json()
        laptop_products = laptop_data.get("products", [])

        print("Laptops fetched successfully.")

        for laptop in laptop_products:
            laptop_name = laptop.get("title", "N/A")
            laptop_price = laptop.get("price", "N/A")
            print(f"Product Name: {laptop_name} | Price: ${laptop_price}")
    else:
        print(f"Request failed with status code: {laptop_response.status_code}")

except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet.")

except requests.exceptions.Timeout:
    print("Request timed out. Try again later.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")



# POST request - Simulated add product

print("\nSending POST request with better error handling...")

new_product = {
    "title": "My Custom Product",
    "price": 999,
    "category": "electronics",
    "description": "A product I created via API"
}

try:
    post_response = requests.post(f"{base_url}/add", json=new_product, timeout=5)

    # checking if the POST request was successful
    if post_response.status_code in [200, 201]:
        created_product = post_response.json()
        print("POST request successful.")
        print("Server response:")
        print(created_product)
    else:
        print(f"POST request failed with status code: {post_response.status_code}")

except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet.")

except requests.exceptions.Timeout:
    print("Request timed out. Try again later.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")



# Part D - Input Validation Loop

print("\n" + "-" * 80)
print("Part D: Input Validation Loop")

# here I am taking product ID from the user again and again until quit is entered
# first I am checking if the input is a valid number and in the correct range
# only after valid input, the API request will be sent

while True:
    user_input = input("\nEnter a product ID to look up (1–100), or 'quit' to exit: ").strip()

    # if user wants to stop the loop
    if user_input.lower() == "quit":
        print("Exiting product lookup.")
        break

    # checking if the input is a number
    if not user_input.isdigit():
        print("Invalid input. Please enter a whole number between 1 and 100.")
        continue

    # converting to integer after validation
    product_id = int(user_input)

    # checking if the number is in valid range
    if product_id < 1 or product_id > 100:
        print("Invalid product ID. Please enter a number between 1 and 100.")
        continue

    # if input is valid, then make the API call
    try:
        product_response = requests.get(f"{base_url}/{product_id}", timeout=5)

        # checking if product exists or not
        if product_response.status_code == 404:
            print("Product not found.")

        elif product_response.status_code == 200:
            product_data = product_response.json()
            product_title = product_data.get("title", "N/A")
            product_price = product_data.get("price", "N/A")

            print(f"Product Title: {product_title}")
            print(f"Product Price: ${product_price}")

        else:
            print(f"Request failed with status code: {product_response.status_code}")

    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")

    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        

# Task 4 — Logging to File
print("\n" + "=" * 50)
print("TASK 4 - LOGGING TO FILE")
print("=" * 50)           

# here I am saving errors in error_log.txt
# if something goes wrong, the error will be written in the file
# this will help to check the issue later
# Log file name
log_file = "error_log.txt"



# Logger function

# function to write error details in the log file
# using append so old logs also stay there
def log_error(function_name, error_type, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = f"[{timestamp}] ERROR in {function_name}: {error_type} — {message}\n"

    with open(log_file, "a", encoding="utf-8") as file:
        file.write(log_entry)


# Trigger 1 - ConnectionError
print("\nTriggering a ConnectionError intentionally...")

# using a wrong URL to trigger connection error
bad_url = "https://this-host-does-not-exist-xyz.com/api"

try:
    bad_response = requests.get(bad_url, timeout=5)

except requests.exceptions.ConnectionError as e:
    print("ConnectionError caught and logged.")
    log_error("fetch_products", "ConnectionError", "No connection could be made")

except requests.exceptions.Timeout as e:
    # handling timeout also
    print("Timeout caught and logged.")
    log_error("fetch_products", "Timeout", str(e))

except Exception as e:
    print("Unexpected error caught and logged.")
    log_error("fetch_products", type(e)._name_, str(e))



# Trigger 2 - Invalid Product ID
print("\nChecking an invalid product ID to trigger error...")

# checking the status code manually for invalid product ID
invalid_product_id = 999

try:
    invalid_response = requests.get(f"{base_url}/{invalid_product_id}", timeout=5)

    if invalid_response.status_code != 200:
        print("HTTP error response detected and logged.")
        log_error(
            "lookup_product",
            "HTTPError",
            f"{invalid_response.status_code} Not Found for product ID {invalid_product_id}"
        )
    else:
        # just in case the product is found
        print("Unexpectedly found product 999.")

except requests.exceptions.ConnectionError:
    print("Connection failed while checking invalid product.")
    log_error("lookup_product", "ConnectionError", "No connection could be made")

except requests.exceptions.Timeout:
    print("Request timed out while checking invalid product.")
    log_error("lookup_product", "Timeout", "Request timed out")

except Exception as e:
    print("Unexpected error caught and logged.")
    log_error("lookup_product", type(e)._name_, str(e))


# Read and display the full log file
print("\nReading full contents of error_log.txt...\n")

try:
    with open(log_file, "r", encoding="utf-8") as file:
        log_contents = file.read()
        print(log_contents)

except FileNotFoundError:
    print("Log file not found.")