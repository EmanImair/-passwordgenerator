import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


password_list=[]

print("Welcome to the PyPassword Generator!")
n_letters= int(input("how many letters would you like to have in your password : "))
n_numbers=int(input("how many numbers would you like to have in your password :"))
n_symbols=int(input("how many numbers would you like to have in your password :"))


for char in range(0,n_letters):
  password_list.append(random.choice(letters))

for char in range(0,n_numbers):
  password_list.append(random.choice(numbers))

for char in range(0,n_symbols):
  password_list.appened(random.choice(symbols))

random.shuffle(password_list)

password=""

for char in password_list:
  password+=char


print(f"password {password}")
