# ask user for name
name = input('What is your name?: ')
print(name)
# ask user for age # imput default set as string
age = input('What is your age?: ')
print(age)
# ask user for city
city = input('what city are you from?: ')
print(city)
# ask user what they enjoy
love = input('What do you love doing?: ')
print(love)
# create output text
string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name,age,city,love)
# print output to screen
print(output)