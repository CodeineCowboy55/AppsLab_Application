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
        "Dosage": 0.46,
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
        "Dosage": 0.36,
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
        "Dosage": 0.25,
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
        "Dosage": 0.8,
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
        "Dosage": 0.12,
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
        "Dosage": 0.04,
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
        "Dosage": 0.21,
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
        "Dosage": 0.4,
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
        "Dosage": 0.44,
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
            if date_required > request_date:  # Check if Date Required is after Request Date
                break
            else:
                print("Date Required must be after Request Date.")
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
        record = my_projectdict.get(id_tofetch)

        if record:
            print("\nRecord found:")
            print_projectdata_header()
            print_projectdata_row(id_tofetch, record)
        else:
            print(f"No record found for ID {id_tofetch}.")
    except ValueError:
        print("Invalid input. Please enter a valid ID.")

def print_projectdata_header():
    header = (
        f'{"ID":<5} | {"Date Required":<15} | {"Date Requested":<15} | {"User":<15} | '
        f'{"Customer Number":<15} | {"Project Number":<15} | {"Fragrance Number":<18} | '
        f'{"Dosage":<10} | {"Product Type":<15} | {"Base (%)":<10}'  # Updated header for 'Base' column
    )
    print(header)
    print("-" * len(header))


def print_projectdata_row(id_value, record):
    # Convert 'Base' value to "Yes" or "No" instead of percentage this is crucial as user needs to see it as a yes or no to understand the value
    base_value = "Yes" if record.get("Base") else "No"

    temp_str = (
        f'{id_value:<5} | {record.get("Date Required", ""):<15} | {record.get("Date Required", ""):<15} | {record.get("User", ""):<15} | '
        f'{record.get("Customer Number", ""):<15} | {record.get("Project Number", ""):<15} | {record.get("Fragrance Number", ""):<18} | '
        f'{record.get("Dosage", ""):<10} | {record.get("Product Type", ""):<15} | {base_value:<10}'
    # Display 'Base' as "Yes" or "No"
    )
    print(temp_str)

def edit_record():
    while True:
        try:
            id_to_edit = int(input("Enter the ID of the record you want to edit: "))
            record_to_edit = my_projectdict.get(id_to_edit)

            if record_to_edit:
                print("\nExisting Record:")
                print_projectdata_header()
                print_projectdata_row(id_to_edit, record_to_edit)
                print("\nEnter the new data:")

                # You can choose which fields you want to edit
                new_request_date_str = input("Enter new Request Date (dd/mm/yyyy) or press Enter to keep the existing value: ")
                new_date_required_str = input("Enter new Date Required (dd/mm/yyyy) or press Enter to keep the existing value: ")
                new_user = input("Enter new User Name or press Enter to keep the existing value: ")
                new_customer_number = input("Enter new Customer Number or press Enter to keep the existing value: ")
                new_project_number = input("Enter new Project Number or press Enter to keep the existing value: ")
                new_fragrance_number = input("Enter new Fragrance Number or press Enter to keep the existing value: ")
                new_dosage = input("Enter new Fragrance Percentage or press Enter to keep the existing value: ")
                new_product_type = input("Enter new Product Type or press Enter to keep the existing value: ")
                new_base = input("Enter new Base (Yes/No) or press Enter to keep the existing value: ")

                # Update the record with the new data
                if new_request_date_str:
                    record_to_edit["Request Date"] = new_request_date_str

                if new_date_required_str:
                    try:
                        new_date_required = datetime.datetime.strptime(new_date_required_str, "%d/%m/%Y")
                        request_date = datetime.datetime.strptime(record_to_edit["Request Date"], "%d/%m/%Y")
                        if new_date_required > request_date:  # Check if Date Required is after Request Date
                            record_to_edit["Date Required"] = new_date_required_str
                        else:
                            print("Date Required must be after Request Date.")
                    except ValueError:
                        print("Invalid date format. Please enter a date in the format dd/mm/yyyy.")

                if new_user:
                    record_to_edit["User"] = new_user
                if new_customer_number:
                    record_to_edit["Customer Number"] = int(new_customer_number)
                if new_project_number:
                    record_to_edit["Project Number"] = int(new_project_number)
                if new_fragrance_number:
                    record_to_edit["Fragrance Number"] = int(new_fragrance_number)
                if new_dosage:
                    record_to_edit["Dosage"] = float(new_dosage)
                if new_product_type:
                    record_to_edit["Product Type"] = new_product_type
                if new_base:
                    new_base_lower = new_base.strip().lower()
                    if new_base_lower == 'yes':
                        record_to_edit["Base"] = True
                    elif new_base_lower == 'no':
                        record_to_edit["Base"] = False
                    else:
                        print("Invalid input for 'Base'. Please enter 'Yes' or 'No'.")
                # Here update the user when record was updated sucessfully
                print("Record updated successfully.")
            else:
                print(f"No record found for ID {id_to_edit}. Please enter a valid ID.")
        except ValueError:
            print("Invalid input. Please enter a valid ID.")
            continue
        else:
            break  # Exit the loop if ID is valid and record exists
