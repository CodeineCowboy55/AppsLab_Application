import datetime
my_projectdict ={
    1:  {
        "Request Date": "02/02/2024",
        "Date Required": "06/04/2024",
        "User": "Mia",
        "Customer Number": 2546984,
        "Project Number": 5648795,
        "Fragrance Number": 25698547,
        "Dosage": 0.5,
        "Product Type": "EDT",
        "Base": True,
    },

    2:  {
        "Request Date": "10/01/2024",
        "Date Required": "08/02/2024",
        "User": "Bruce",
        "Customer Number": 4569825,
        "Project Number": 125478,
        "Fragrance Number": 69854751,
        "Dosage": 1.6,
        "Product Type": "Room Spray",
        "Base": False,
    },

    3:  {
        "Request Date": "15/03/2024",
        "Date Required": "25/04/2024",
        "User": "Lindsey",
        "Customer Number": 452168,
        "Project Number": 395216,
        "Fragrance Number": 4698215,
        "Dosage": 4.6,
        "Product Type": "candle",
        "Base": True,
    },

    4:  {
        "Request Date": "12/02/2024",
        "Date Required": "19/03/2024",
        "User": "Mia",
        "Customer Number": 162548,
        "Project Number": 974216,
        "Fragrance Number": 7563219,
        "Dosage": 6.5,
        "Product Type": "wax melt",
        "Base": 0.5,
    },

    5:  {
        "Request Date": "13/01/2024",
        "Date Required": "18/04/2024",
        "User": "Harry",
        "Customer Number": 165289,
        "Project Number": 652158,
        "Fragrance Number": 1247854,
        "Dosage": 8.9,
        "Product Type": "conditioner",
        "Base": False,
    },

    6:  {
        "Request Date": "05/02/2024",
        "Date Required": "15/02/2024",
        "User": "Sam",
        "Customer Number": 147528,
        "Project Number": 942357,
        "Fragrance Number": 1254239,
        "Dosage": 12,
        "Product Type": "Polish",
        "Base": False,
    },

    7: {
        "Request Date": "12/02/2024",
        "Date Required": "28/02/2024",
        "User": "Bruce",
        "Customer Number": 489279,
        "Project Number": 164852,
        "Fragrance Number": 7159349,
        "Dosage": 2.6,
        "Product Type": "EDP",
        "Base": True,
    },

    8:  {
        "Request Date": "04/03/2024",
        "Date Required": "15/03/2024",
        "User": "Sam",
        "Customer Number": 456852,
        "Project Number": 951458,
        "Fragrance Number": 4815974,
        "Dosage": 10,
        "Product Type": "Candle",
        "Base": False,
    },

    9:  {
        "Request Date": "25/04/2024",
        "Date Required": "12/05/2024",
        "User": "Mia",
        "Customer Number": 584965,
        "Project Number": 136548,
        "Fragrance Number": 2089064,
        "Dosage": 0.9,
        "Product Type": "Room spray",
        "Base": True,
    },

    10: {
        "Request Date": "30/01/2024",
        "Date Required": "18/02/2024",
        "User": "Sam",
        "Customer Number": 102654,
        "Project Number": 603254,
        "Fragrance Number": 2040856,
        "Dosage": 1.8,
        "Product Type": "EDT",
        "Base": True,
    }
}


def add_record():
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
            print("Invalid input. Please enter a valid number.")

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
        if base == 'yes':
            base = True
            break
        elif base == 'no':
            base = False
            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

    index_to_add = max(my_projectdict.keys()) + 1
    my_projectdict[index_to_add] = {
        "Request Date": request_date_str,
        "Date Required": date_required_str,
        "User": user,
        "Customer Number": customer_number,
        "Project Number": project_number,
        "Fragrance Number": fragrance_number,
        "Dosage": dosage,
        "Product Type": product_type,
        "Base": base
    }

    print(f'Added id {index_to_add}: {my_projectdict[index_to_add]}')
    return my_projectdict[index_to_add]


def get_record():
    try:
        id_tofetch = int(input("Enter the ID to fetch record: "))
        # check the id exists
        print(my_projectdict[id_tofetch])
    except ValueError: # this will be a different error IndexError
        print(" ")


def delete_record():
    try:
        id_tofetch = int(input("Enter the ID to fetch record: "))
        # check the id exists
        del my_projectdict[id_tofetch]
        print(f'DELETED {id_tofetch}')
    except KeyError: # this will be a different error IndexError
        print(" ")

#make sur change has been applied