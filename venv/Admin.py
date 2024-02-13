#This is where the admin  password and delete record definition is kept
from Data import my_projectdict


def delete_record():
    try:
        # Enter the password to allow deletion
        password = input("Enter the password to delete records: ")

        # Check if the password is correct
        if password == "your_password_here":  # Replace "your_password_here" with your actual password
            id_tofetch = int(input("Enter the ID to fetch record: "))

            # Check if the ID exists
            if id_tofetch in my_projectdict:
                del my_projectdict[id_tofetch]
                print(f'DELETED {id_tofetch}')
            else:
                print("ID not found.")
        else:
            print("Incorrect password. Deletion denied.")
    except ValueError:
        print("Invalid input. Please enter a valid ID.")