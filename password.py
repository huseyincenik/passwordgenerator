import string
import random

def gen():
    s1 = string.ascii_uppercase # uppercase
    s2 = string.ascii_lowercase # lower case
    s3 = string.digits # from 0 to 9 digits
    s4 = string.punctuation # sembol and special characters
    password_len = int(input("Enter the password lenght \n :")) # get password length from user
    s = [] # empty list
    s.extend(list(s1)) # add s1 to list
    s.extend(list(s2)) # add s2 to list
    s.extend(list(s3)) # add s3 to list
    s.extend(list(s4)) # add s4 to list
    random.shuffle(s) # mix s randomly
    pas =("".join(s[0:password_len])) # Generate random password of user desired length
    print(pas)
gen()