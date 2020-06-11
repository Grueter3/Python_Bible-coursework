# get user email address
email = input('What is your email address:? ').strip()
#slice out user name
user = email[:email.index('@')]
#slice domain name
domain = email[email.index('@')+1:]
#format messagepyth
output = (f'Your username is {user} and your doamain name is {domain}')
#display output message
print(output)
