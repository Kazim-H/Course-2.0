import re
input_string = "123-456-7890 (234)567-8901 3456789012 456.789.0123 567-890-1234 (678)901-2345 7890123456 890-123-4567 901.234.5678 0123456789"
numbers = re.findall('\(?\d{3}\)?[-\.]?\d{3}[-\.]?\d{4}', input_string)
print(numbers)
