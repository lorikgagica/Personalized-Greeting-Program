# Personalized Greeting Program

# Step 1: Ask for user details
""" name = input("What is your name? ")
age = int(input("How old are you? "))
color = input("What is your favorite color? ")

# Step 2: Generate a personalized greeting message
print("\n---- Personalized Greeting ----")
print(f"Hello, {name}! 👋")
print(f"You are {age} years old and {color} is a beautiful color!")
print("You're now ready to start your Python adventure 🚀🐍") """


# ------------------------------------------------

from datetime import datetime

# Step 1: Ask for user details
name = input("What is your name? ")
color = input("What is your favorite color? ")

# Ask for user birthday to calculate age
birthday_input = input("When is your birthday? (DD-MM-YYYY) ")
try:
    birthday = datetime.strptime(birthday_input, "%d-%m-%Y")
    today = datetime.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
except:
    age = None

# Nickname generator (simple: first 3 letters + last letter, all lowercase, or fallback)
def generate_nickname(name):
    name = name.strip()
    if len(name) <= 3:
        return name.lower() + "ster"
    return name[:3].lower() + name[-1].lower() + "y"

nickname = generate_nickname(name)

# Step 2: Generate a personalized greeting message
print("\n---- Personalized Greeting ----")
print(f"Hello, {name}! 👋 (a.k.a {nickname})")
if age is not None:
    print(f"You are {age} years old and {color} is a beautiful color!")
else:
    print(f"{color} is a beautiful color!")
print("You're now ready to start your Python adventure 🚀🐍")