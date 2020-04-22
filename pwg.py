import random
chars = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 ! @ $ %"

split_chars = chars.split()
password = [] 

print("How many characters would you like this password to be?")
limit = input() 
x = 0

while x < int(limit):
    password.append(random.choice(split_chars))
    x = x + 1 

f_password = ''.join(password)
print(f_password)