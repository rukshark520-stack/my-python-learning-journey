import random
chars="abcdefghilmnopqrstuvwxy234567890"
password=""
for i in range(8):
    password+=random.choice(chars)
print("password is=",password)
