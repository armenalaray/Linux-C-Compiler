import re

# Validate number
is_alphanumeric = r"[a-zA-Z_]\w+"
is_numeric = r"\d+"

is_not = r"\d+[a-zA-Z]"

np = r"\s+"

a = re.match(is_not, '42dasa_AZ()') # Returns Match object
b = re.match(is_not, '43notanumber43') # Returns None

print(a)
print(b)

# Extract number from a string
number_extract_pattern = "\\d+"
re.findall(number_extract_pattern, 'Your message was viewed 203 times.') # returns ['203']