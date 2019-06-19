#!/usr/bin/python3

import random
import string

print("How difficult password you want? \n 1- Easy \n 2- Medium \n 3- Fucking difficult \n Choose b/w 1,2 and 3 \n")
user=input("Enter Difficulty level:"  )
user=int(user)
alphabets=list(string.ascii_letters)
numbers=list(string.digits)
specialChar=list(string.punctuation)
pwd=[]

if user==1:
    for i in range(8):
        pwd1=random.choice(alphabets)
        pwd.append(pwd1)
    print("Your Password is:","".join(pwd))

elif user==2:
    for i in range(12):
        pwd1=random.choice(alphabets+numbers)
        pwd.append(pwd1)
    print("Your Password is:","".join(pwd))
 
else:
    for i in range(15):
        pwd1=random.choice(alphabets+numbers+specialChar)
        pwd.append(pwd1)
    print("Your Password is:","".join(pwd))
 
