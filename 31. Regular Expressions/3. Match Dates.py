import re

pattern = r"\b(?P<Day>\d{2})([\./-])(?P<Month>[A-Z][a-z][a-z])\2(?P<Year>\d{4})\b"
dates = input()


matches = re.finditer(pattern, dates)

for date in matches:
    date_data = date.groupdict()
    print(f"Day: {date_data['Day']}, Month: {date_data['Month']}, Year: {date_data['Year']}")
