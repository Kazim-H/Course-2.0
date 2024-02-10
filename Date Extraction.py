import re
sample_string = "- Today is 2024-02-05. - Tomorrow's date is 05/02/2024. - The event will take place on 2024-02-10 at 10:00 AM. - Another date: 02-05-24. - Don't forget the meeting on 2024-02-06!"
pattern = '(?:\d{4}|\d{2})[-/]\d{2}[-/](?:\d{4}|\d{2})'
dates = re.findall(pattern, sample_string)
print(dates)
