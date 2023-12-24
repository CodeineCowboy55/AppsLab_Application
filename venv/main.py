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
            break1
        except ValueError:
            print("Invalid date format. Please enter a date in the format dd/mm/yyyy.")

    # User - no validation required just a name of person entering
    while True:
        user = input("Enter User Name: ")
        if user:
            break
        else:
            print("Invalid input. User name cannot be empty.")

    # Customer Number- Must be a 6 digit nubmer
    while True:
        try:
            customer_number = int(input("Enter Customer Number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Project Number
    while True:
        try:
            project_number = int(input("Enter Project Number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Fragrance Number
    while True:
        try:
            fragrance_number = int(input("Enter Fragrance Number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Dosage
    while True:
        try:
            dosage = float(input("Enter Dosage: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Product Type
    product_type = input("Enter Product Type: ")

    # Base
    base = input("Enter Base (Yes/No): ").lower() == 'yes'

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


def main():
    while True:
        print("APPLICATION LAB OIL LIBARY\n")
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
        elif user_input == "2":
            print("You selected Option 2.")
            # Add your code for Option 2 here
        elif user_input == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()