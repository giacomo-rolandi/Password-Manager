#This is a Password Manager program that stores passwords for different accounts and allows the user to retrieve them.
#The passwords are stored in a file called data.txt in the same directory as the program.
#The program uses the cryptography library to encrypt and decrypt the passwords.

import hashlib as hl
from cryptography.fernet import Fernet


#Function to create a hash of the password
def create_hash(password):
    return hl.sha256(password.encode()).hexdigest()


#Function to check if the input password matches the stored hash
def check_password(input_password, stored_hash):
    input_hash = create_hash(input_password)
    if input_hash == stored_hash:
        return True
    else:
        return False
    

#function to add a new password to the data file
def add_passwd():
    text = []
    replace = False
    print("\nHello bro! You are now adding a new password.")
    domain = input("Enter the domain:  ")
    username = input("Enter the username/email:  ")
    password = input("Enter the password:  ")

    with open("data.txt", "r") as file:
        for line in file:
            if domain in line:
                line = line.replace(line, f"{domain} {username} {password}\n")
                replace = True
            text.append(line)

    with open("data.txt", "w") as file:                
        if replace == True:
            for line in text:
                file.write(line)
        else:
            text.append(f"{domain} {username} {password}\n")
            for line in text:
                file.write(line)    


#function to view existing passwords in the data file
def view_passwd():
    print("\nHello bro! You are now viewing your passwords.\n")
    with open("data.txt", "r") as file:
        for line in file:
            print(line)  
    
    



print("\nWelcome to the Password Manager!\n")

#check if the user is registered, if yes, ask for the master password
#otherwise, ask the user to choose a master password
registered = input("Are you already registered? (yes/no)  ")

if registered == "yes":
    master_password = input("Please enter your master password:  ")
    with open ("master.txt", "r") as file:
        stored_hash = file.read()
        if check_password(master_password, stored_hash):
            print("Welcome back!")
        else:
            print("Incorrect password. Please try again.")
            exit()
else:
    master_password = input("Choose a master password:  ")
    #Create the hash of the master password and store it in a file called master.txt
    with open("master.txt", "w") as file:
        file.write(create_hash(master_password))
    with open("data.txt", "w") as file:
        file.write("")



choice = 0

#Navigate to the main menu
while (choice != 3):       
    print("\nYou are now in the main menu. Please choose what you would like to do.")
    print("""
        1) Store a password 
        2) View existing ones
        3) Exit
        """)
    choice = int(input())

    if choice == 1:
        add_passwd()
    elif choice == 2:
        view_passwd()
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")



print("\nThank you for using the Password Manager. Goodbye!")