from unittest import result


website = 'http://www.google.com'
course = 'Python Programming 101'

# 1-) How many characters are in the 'course' variable?

length = len(course)  # len() is a function that returns the length of a string
print('The length of the course variable is:', length)

# 2-) Get the 'www' from the 'website' variable.
result = website[7:10]  # [start:end]
print('The result of the website variable is:', result)

# 3-) Get the 'com' from the 'website' variable.
result = website[-3:]  # [-3:] is the last 3 characters
print('The result of the website variable is:', result)

# 4-) Get the first 15 and last 15 characters from the 'course' variable.

# [:15] is the first 15 characters, [-15:] is the last 15 characters
result = course[:15]+course[-15:]
print('The result of the course variable is:', result)

# 5-) Reverse the 'course' variable.
result = course[::-1]  # [::-1] is the reverse of the string
print('The result of the course variable is:', result)

name, surname, age, job = 'Joe', 'Down', 32, 'Teacher'
# 6- Create a text using defined variables.
print(f'My name is {name} {surname}, I am {age} years old and I am a {job}.')

# 7-) print 'abc' expression 3 times.
result = 'abc' * 3
print('The result of the expression is:', result)
