#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import string

def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    password = ''.join(random.choice(letters + digits + symbols) for _ in range(length))
    return password

if __name__ == '__main__':
    length = int(input('Enter the length of the password: '))
    password = generate_password(length)
    print(f'Your password is: {password}')


# In[ ]:




