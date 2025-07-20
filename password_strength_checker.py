import string

password = input("Enter your password: ")
password_strength = 0

if len(password) >= 8:
    password_strength += 1

if any(char.islower() for char in password):
    password_strength += 1
    
if any(char.isupper() for char in password):
    password_strength += 1
    
if any(char.isdigit() for char in password):
    password_strength += 1
    
if any(char in string.punctuation for char in password):
    password_strength += 1
    
if password_strength == 5:
    print("Your password is strong. Includes uppercase, lowercase and symbols.")
    
elif password_strength >=3:
    print("Your password is moderate. Consider adding more symbols.")
    
else:
    print("Your password is weak. Try to add uppercase, lowercase and symbols.")