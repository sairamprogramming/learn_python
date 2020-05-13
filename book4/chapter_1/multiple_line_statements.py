# Program that demonstrates multiple line statements in python.

first_item = 10
second_item = 20
third_item = 30

# Using line continuation character (\)
grand_total = first_item + \
        second_item + \
        third_item

print(grand_total)

# Statements contained in [], {} , () do not need line continuation character.
months = ['Jan', 'Feb', 'Mar', 'Apr',
        'May', 'Jun', 'Jul', 'Aug',
        'Sep', 'Oct', 'Nov', 'Dec']

print(months)
