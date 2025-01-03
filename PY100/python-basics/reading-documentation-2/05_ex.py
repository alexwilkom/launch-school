# The Python documentation for the datetime module provides two attributes to 
# retrieve the year from a date or datetime object: year and isocalendar.

from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()[0]

# What is the difference between the year attribute and the isocalendar method?

print(today)
print(today_year)
print(list(today.isocalendar()))
print(iso_year)

# The year attribute returns just the year.

# The isocalendar method returns a named tuple object with three components: 
# year, week and weekday.