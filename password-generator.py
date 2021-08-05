import random

# define the set of characters we want to use
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
special = ['@', '#', '$', '%', '=', ':', '?', '.', '/',
           '|', '~', '>', '*', '(', ')', '<', '•', 'α', 'ß', 'γ']
collection = digits + uppercase + lowercase + special

# User input for number of characters
print('Enter the number of characters (12-100): ')
strn = int(input())

# limit the number of characters between 12 to 100
if strn < 12:
    strn = 12

elif strn > 100:
    strn = 100

# Take at least one letter from each character set randomly
dig = random.choice(digits)
low = random.choice(lowercase)
up = random.choice(uppercase)
sym = random.choice(special)

# append the above characters in an empty list
rnd_char = []
rnd_char.append(dig)
rnd_char.append(low)
rnd_char.append(up)
rnd_char.append(sym)

# apart from above 4 characters fill rest randomly and append to list
for i in range(strn-4):
    rnd_char.append(random.choice(collection))

# shuffle the final list of characters
random.shuffle(rnd_char)

# generate the password as a string
password = ""
for j in rnd_char:
    password = password + j

# print the password
print(password)
