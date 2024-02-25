import os

admin = os.environ["admin"]
user = os.environ["user"]
admin_password = os.environ["admin_password"]
user_password = os.environ["user_password"]

usernameInput = input("Enter your username: > ")
passwordInput = input("Enter the password: > ")

if usernameInput == admin and passwordInput == admin_password:
    print(f"Welcome {admin}")
elif usernameInput == user and passwordInput == user_password:
    print(f"Welcome {user}")
else:
    print("User or password incorrect")
