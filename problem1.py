import datetime

current_date = datetime.date.today()
print("current date is:" + str(current_date))
year = current_date.year
print("current year is:" + str(year))

name = input("Give me your name: ")
print("Your name is " + name)
age = int(input("Enter your age: "))
print("Your age is " + str(age))

new_age=100-age
print("Your new age is " + str(new_age))

hun_year = year + new_age
print("hundered year is:" + str(hun_year))

number = int(input("Give me a number: "))
print("Your number is \n " * number )


