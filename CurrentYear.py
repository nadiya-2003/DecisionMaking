
birth_year_last_two = int(input("Enter the last two digits of your birth year: "))
current_year_last_two = int(input("Enter the last two digits of the current year: "))
if current_year_last_two >= birth_year_last_two:
    age = current_year_last_two - birth_year_last_two
else:
    age = (100 + current_year_last_two) - birth_year_last_two

print(age)
