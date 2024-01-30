import datetime
import sys  # Import the sys module
from Data import my_projectdict, add_record, get_record, delete_record


def print_projectdata():
    print('ID | Date required | Date Rquested | User | Customer Number | Project Number | Fragrance Number | Dosage | Product type | Base')
    for key, value in my_projectdict.items():
        temp_str = f'{key} | '
        for k, v in value.items():
            temp_str += f'{v} | '
        print(temp_str[:-3])



#The go back to home screen def allows the user at then end of adding an input to go back to the home screen
def go_back_to_home_screen():
    input("\nPress Enter to go back to the home screen...\n")

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

#Def main is the main menu that is the start and control of the application here user will select option to navigate
def main():
    while True:




        print("APPLICATION LAB OIL LIBRARY- V1.3\n")
        print("_____________________________\n")
        print_projectdata()
        print("Please select an option:")
        print("1. Add record")
        print("2. Search Record")
        print("3. Delete record")
        print("4. Exit Application")

        try:
            user_input = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        except (KeyboardInterrupt, EOFError):
            confirm_exit()

        if 1 <= user_input <= 4:
            if user_input == 1:
                print("You selected Option 1.")
                record = get_record()
                print(record)
                go_back_to_home_screen()
            elif user_input == 2:
                print("You selected Option 2.")
                add_record()

                # Add add my option for searching record
                go_back_to_home_screen()
            elif user_input == 3:
                print("You selected Option 3.")
                delete_record()
                # add my code for deleting record later
                go_back_to_home_screen()
            elif user_input == 4:
                confirm_exit()
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
