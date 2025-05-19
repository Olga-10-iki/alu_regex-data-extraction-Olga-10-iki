import re

regex_patterns = {
    "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    "url": r"https?:\/\/(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\/\S*)?",
    "phone": r"(?:\(\d{3}\)\s?|\d{3}[-.])\d{3}[-.]\d{4}",
    "creditCard": r"\b(?:\d{4}[- ]?){3}\d{4}\b"
}

def extract_matches(text, pattern):
    return re.findall(pattern, text)

# Read text from test_strings.txt
with open('test_strings.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Extract and print matches for each pattern
for key, pattern in regex_patterns.items():
    matches = extract_matches(text, pattern)
    print(f"{key} matches: {matches}")