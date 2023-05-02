import pyperclip
import random
char = int(input("Enter the number of characters password should have? "))
sample_space = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@!#$%^&*()_+"
password = "".join(random.sample(sample_space,char))
print(password)
pyperclip.copy(password)