import datetime

def get_record():
    # Request Date - the day the request is submitted
    while True:
        try:
            request_date_str = input("Enter Request Date (dd/mm/yyyy): ")
            request_date = datetime.datetime.strptime(request_date_str, "%d/%m/%Y")
            break
        except ValueError:
            print("Invalid date format. Please enter a date in the format dd/mm/yyyy.")

    # Date Required
    while True:
        try:
            date_required_str = input("Enter Date Required (dd/mm/yyyy): ")
            date_required = datetime.datetime.strptime(date_required_str, "%d/%m/%Y")
            break
        except ValueError:
            print("Invalid date format. Please enter a date in the format dd/mm/yyyy.")

    # User - no validation required just a name of person entering; this is a string input
    while True:
        user = input("Enter User Name: ")
        if user:
            break
        else:
            print("Invalid input. User name cannot be empty.")

    # Customer Number - Must be a 6 digit number
    while True:
        try:
            customer_number = input("Enter Customer Number: ")
            if len(customer_number) == 6 and customer_number.isdigit():
                customer_number = int(customer_number)
                break
            else:
                print("Invalid input. Please enter a 6-digit number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Project Number
    while True:
        try:
            project_number = int(input("Enter Project Number: "))
            if 100000 <= project_number <= 999999:
                break
            else:
                print("Invalid input. Please enter a 6-digit number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Fragrance Number - Must be a 6 digit number
    while True:
        try:
            fragrance_number = int(input("Enter Fragrance Number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Dosage
    while True:
        try:
            dosage = float(input("Enter Fragrance Percentage: "))
            if 0 <= dosage <= 100:
                break
            else:
                print("Invalid input. Please enter a percentage between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Product Type is string so can be the name of the product that needs to be made.
    product_type = input("Enter Product Type: ")

    # Base - Must be yes or no to define if it's a base for another product or its the product's fragrance
    while True:
        base = input("Enter Base (Yes/No): ").strip().lower()
        if base == 'yes' or base == 'no':
            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

    return {
        "Request Date": request_date,
        "Date Required": date_required,
        "User": user,
        "Customer Number": customer_number,
        "Project Number": project_number,
        "Fragrance Number": fragrance_number,
        "Dosage": dosage,
        "Product Type": product_type,
        "Base": base
    }
def go_back_to_home_screen():
    input("\nPress Enter to go back to the home screen...\n")
def main():
    while True:
        print("APPLICATION LAB OIL LIBRARY\n")
        print("Please select an option:")
        print("1. Add record")
        print("2. Search Record")
        print("3. Delete record")
        print("4. Exit")

        user_input = input()

        if user_input == "1":
            print("You selected Option 1.")
            record = get_record()
            print(record)
            go_back_to_home_screen()
        elif user_input == "2":
            print("You selected Option 2.")
            # Add your code for Option 2 here
            go_back_to_home_screen()
        elif user_input == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
