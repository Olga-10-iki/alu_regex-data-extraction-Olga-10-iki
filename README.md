"""
regex_extractor_with_explanation.py

This script demonstrates how to use Regular Expressions (regex) in Python to extract
structured data from unstructured text. It extracts the following:
1. Email addresses
2. URLs (http/https)
3. Phone numbers in common formats
4. Credit card numbers

Author: IKIREZI Olga

==========================
📘 What This Script Does
==========================
This Python script demonstrates how to use **Regular Expressions (regex)** to extract useful data from a block of unstructured text. It simulates processing raw data from an API or scraped webpage and focuses on **identifying and extracting four key types of information**:

1. **Email Addresses** – such as `user@example.com`
2. **URLs** – web links starting with `http://` or `https://`
3. **Phone Numbers** – in formats like `(123) 456-7890` or `123-456-7890`
4. **Credit Card Numbers** – formatted with spaces, dashes, or as one long number

📥 Input
-------
The script contains a sample block of text with both **valid** and **invalid** examples for each data type, to test how accurately the regular expressions identify the correct formats.

📤 Output
--------
When you run the script, it will print out lists of all valid matches found in the sample text, grouped by data type. Invalid formats will be ignored.

✅ What You Can Expect
----------------------
- The script filters out incorrect formats automatically using regex.
- It’s easy to expand if you want to add more data types like:
  - Time formats (e.g., `14:30` or `2:30 PM`)
  - Hashtags (e.g., `#MyTag`)
  - HTML tags (e.g., `<div>`)
  - Currency (e.g., `$19.99`)
"""

# Sample text simulating what might be returned from an API response or scraped data

Emails:
user@example.com
firstname.lastname@company.co.uk

URLs:
https://www.example.com
http:/broken.url.com

Phones:
(123) 456-7890
123-456-7890

Credit Cards:
1234 5678 9012 3456
abcd-efgh-ijkl-mnop


