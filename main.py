import random

password_symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

ask_length_of_password = int(input('какой длинны хотите пароль(введите число) ?'))

password = ""

for i in range(ask_length_of_password):
    password += random.choice(password_symbols)

print(password)