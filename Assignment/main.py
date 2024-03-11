import datetime
import msvcrt  # I have imported this moduel to allow me to include to take the user to the home screen
import sys  # Import the sys module
from Data import my_projectdict, add_record, get_record, edit_record   #calling all the fuctions from data file
from Admin import delete_record #allows the admin to delete the record

#This Definition prints the read me file for the user
def print_readme():
    readme_content = """
    READ ME

    Welcome to the first release of the Application Lab Fragrance Request Application.

    Select a number on the main menu screen to navigate to the page you desire.

    Please ensure to adhere to the validation rules for successful entry.

    Only the lab manager has access to delete entries in the system.

    For bug reporting, please contact Jean-Michel Ramar at Extension: 2051, Email: jean-michel.ramar@effgroup.com, or Phone: 07478079997.

    For feedback, please refer to Microsoft Teams for the App Feedback Form.

    APP Version 1.3
    """
    print(readme_content)

#calling this prints the project data
def print_projectdata():
    header = (
        f'{"ID":<5} | {"Date Requested":<15} | {"Date Required":<15} | {"User":<15} | '
        f'{"Customer Number":<15} | {"Project Number":<15} | {"Fragrance Number":<18} | '
        f'{"Dosage (%)":<10} | {"Product Type":<15} | {"Base":<10}'  # Updated header for 'Dosage'
    )
    print(header)
    print("-" * len(header))

    for key, value in my_projectdict.items():
        # Map 'Base' value to "Yes" or "No"
        base_display = "Yes" if value.get("Base", 0) > 0 else "No"
        # Convert 'Dosage' value to percentage
        dosage_percentage = "{:.2%}".format(value.get("Dosage", 0))
        temp_str = (
            f'{key:<5} | {value.get("Request Date", ""):<15} | {value.get("Date Required", ""):<15} | {value.get("User", ""):<15} | '
            f'{value.get("Customer Number", ""):<15} | {value.get("Project Number", ""):<15} | {value.get("Fragrance Number", ""):<18} | '
            f'{dosage_percentage:<10} | {value.get("Product Type", ""):<15} | {base_display:<10}'  # Display 'Base' as "Yes" or "No"
        )
        print(temp_str)



#The go back to home screen def allows the user at then end of adding an input to go back to the home screen
def go_back_to_home_screen():
    input("\nPress Enter to go back to the home screen...\n")
    print_projectdata()  # Refresh the project data display

#Purpose of Def confirm Exit is to make sure the user wants to exit the application
def confirm_exit():
    while True:
        choice = input("Do you really want to exit the application? (yes/no): ").strip().lower()
        if choice == 'yes':
            print("Exiting the program.")
            sys.exit()
        elif choice == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
#this def bellow allows the user no matter where they are in app to go back to the home screen
def is_home_pressed():
    return msvcrt.kbhit() and msvcrt.getch() == b'\x1b[H'

#Def main is the main menu that is at the start and controls the application here the user will select option to navigate
def main():
    print("APPLICATION LAB OIL LIBRARY- V1.3\n")
    print("________________________________________________________________________________________________________________________________________________________________\n")
    print_projectdata()  # This print project data out of the loop as I only need it to print once at the start as other fuctions do the same

    while True:
        print("\nPlease select an option:")
        print("1. Add record")
        print("2. Search Record")
        print("3. Edit Record")
        print("4. Delete record")
        print("5. Read me")
        print("6. Exit Application")

        try:
            user_input = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        except (KeyboardInterrupt, EOFError):
            confirm_exit()

        if is_escape_pressed():  # Check if Escape key is pressed if escape key is pressed return to the main menu
            print("Going back to the home screen...")
            continue
# Here are all the possible inputs the user can select
        if 1 <= user_input <= 6:
            if user_input == 1:
                print("You selected Option 1 - Add Record.")
                add_record()
                go_back_to_home_screen()
            elif user_input == 2:
                print("You selected Option 2 - Search Record.")
                record = get_record()
                print(record)
                go_back_to_home_screen()
            elif user_input == 3:
                print("You selected Option 3 - Edit Record.")
                edit_record()
                go_back_to_home_screen()
            elif user_input == 4:
                print("You selected Option 4 - Delete Record.")
                delete_record()
                go_back_to_home_screen()
            elif user_input == 5:
                print_readme()
                go_back_to_home_screen()  # Navigate back to the home screen after printing the README
            elif user_input == 6:
                confirm_exit()          # This will exit the application after confirming yes 
        else:
            print("Invalid input. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
#calls the main fuction and loads def main when the application starts