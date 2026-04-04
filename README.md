Part 3 - Product Explorer & Error-Resilient Logger 

Overview

This project focuses on working with real-world programming concepts like file handling, API integration, and exception handling.
The goal was to build a small system that interacts with an external API, processes data, and handles errors properly without crashing.



Tasks Implemented

Task 1 — File Read & Write
* Created a file `python_notes.txt` and wrote basic Python notes using write mode
* Appended additional custom notes using append mode
* Read the file and displayed:
  * Numbered lines
  * Total line count
* Implemented keyword search (case-insensitive) within the file



Task 2 — API Integration

* Used the DummyJSON API to work with real product data.
* Fetched and displayed 20 products in a formatted table
* Filtered products with high ratings (≥ 4.5)
* Sorted filtered products by price (descending)
* Retrieved products from a specific category (laptops)
* Sent a POST request to simulate adding a product
* Displayed API responses clearly



Task 3 — Exception Handling

Safe Calculator-
* Created a function to safely divide two numbers
* Handled:
  * Division by zero
  * Invalid data types

Safe File Reader-
* Read file content safely
* Handled missing files without crashing
* Used a `finally` block to confirm execution

Robust API Handling-
* Wrapped all API calls in try-except blocks
* Handled:
  * Connection errors
  * Timeout errors
  * Unexpected exceptions

Input Validation Loop-
* Built a loop to fetch product details by ID
* Ensured:
  * Only valid inputs (1–100) are accepted
  * No API calls are made for invalid inputs
* Handled 404 responses properly



Task 4 — Logging System
* Created an `error_log.txt` file to track errors
* Logged errors with timestamps using `datetime`
* Logged:
  * Connection errors
  * HTTP errors (like 404)
* Ensured logs are appended, not overwritten
* Printed the log file contents at the end


Concepts Used

* File handling (`open`, read/write/append modes)
* API requests using `requests`
* JSON parsing
* Exception handling (`try-except-finally`)
* Input validation
* Loops and conditionals
* Logging with timestamps



File Structure-
id="file-structure"
part3_product_explorer.py
python_notes.txt
error_log.txt
README.md


Notes
* The program is designed to handle errors gracefully instead of crashing
* Logging helps track issues for debugging
* DummyJSON API is used for testing, so POST requests do not actually store data


Submission
* Code is pushed to a public GitHub repository
* Repository access verified using incognito mode
