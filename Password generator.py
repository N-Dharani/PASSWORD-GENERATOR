

import random
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
symbols = "-+=!@#$%^&*"
letter=int(input("How many letters do you want in your password?"))
num=int(input("How many numbers do you want in your password?"))
symbol=int(input("How many symbols do you want in your password?"))
r=""
for i in range(0,letter):
  r+=random.choice(letters)
for j in range(0,num):
  r+=random.choice(nums)
for k in range(0,symbol):
  r+=random.choice(symbols)
print(r)
password=list(r)
random.shuffle(password)
print(password)
new_password="".join(password)
print(f"Your password is: {new_password}")                            

