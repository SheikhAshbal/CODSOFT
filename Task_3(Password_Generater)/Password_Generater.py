import random
import string
import pyperclip
def main(): 
    print("------------>PASSWORD GENERATOR<------------\n")
    password_generator_menu()
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password=""
    for _ in range(length):
        password_letter=characters[random.randint(0,93)]
        password+=password_letter   
    return password
def Password_length():
    while True:
        try:
            global length
            length= int(input("Enter the desired length of the password: "))
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            break
        except ValueError as e:
            print(f"Error: {e}")
    return length
def password_generator_menu():
    password = generate_password(Password_length())
    print(f"\nGenerated Password: {password}\n")
    while True:
            user_ask=input("""Choose an option(1/2/3/4)---->
                       1.Regenerate Password
                       2.Change Length then Generate
                       3.Copy the Password
                       4.Exit  :""")
            if user_ask=="1":
                password = generate_password(length)
                print(f"\nNew Generated Password: {password}\n")
            elif user_ask=="2":
                New_length=Password_length()
                password = generate_password(New_length)
                print(f"\nNew Generated Password: {password}")
            elif user_ask=="3":
                pyperclip.copy(password)
                print("\nPassword copied to clipboard.\n")
            elif user_ask=="4":
                print("\nExiting...")
                break
            else:
                print("Invalid Input")

if __name__ == "__main__":
    main()
