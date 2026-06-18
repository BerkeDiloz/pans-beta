import random

N=16
characters = ["a","b","c","d","ğ","h","1","2","3","4","X","Y","Z","$"]
password=""

for i in range(N):
    password += random.choice(characters)
print(password)
