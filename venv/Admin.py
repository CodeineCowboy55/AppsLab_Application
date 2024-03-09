#This definition allows the Lab manager to enter the admin password and delete record provided the ID exsists
from Data import my_projectdict

def delete_record():
    try:
        # Enter the password to allow deletion Manually coded password
        password = input("Enter the password to delete records: ")

        # Check if the password is correct
        if password == "Gabagoo13!":  #This is the password to enter be able to delete a record, only the admin should know password
            id_tofetch = int(input("Enter the ID to fetch record: "))
            #This part if the Definition will fetch the ID from Project dictionary, then check if it exsists, if its does it will delete the selected ID and all data connected to it.
            # Checks if the ID user is trying to load
            if id_tofetch in my_projectdict:
                del my_projectdict[id_tofetch]
                print(f'DELETED {id_tofetch}')
            else:
                print("ID not found.")
        else:
            print("Incorrect password. Deletion denied.")
    except ValueError:
        print("Invalid input. Please enter a valid ID.")
