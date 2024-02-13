#This is where the admin  password and delete code is

from Data import my_projectdict, add_record, get_record, edit_record



def delete_record():
    try:
        id_tofetch = int(input("Enter the ID to fetch record: "))
        # check the id exists
        del my_projectdict[id_tofetch]
        print(f'DELETED {id_tofetch}')
    except KeyError: # this will be a different error IndexError
        print(" ")