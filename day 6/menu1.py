import sys

def create():
    print('Row created')

def read():
    print('Row retrieved')

def update():
    print('Row updated')

def delete():
    print('Row deleted')

def list_all():
    print('Rows listed')

def exit_program():
    sys.exit('End of program')

def invalid_choice():
    print('Invalid choice entered')

def get_menu():
    menu = {
        1 : create,
        2 : read,
        3 : update,
        4 : delete,
        5 : list_all,
        6 : exit_program
    }
    return menu

def start_app():
    while True:
        print('1:Create 2:Read 3:Update 4:Delete 5:List All 6:Exit')
        choice = int(input('Your choice please: '))
        get_menu().get(choice, invalid_choice)()
        #menu = get_menu()
        #menu.get(choice)()

l1 = [2, 3, 6, 88, 1, 33, 2]
l1.sort()
#start_app()

# Method chaining: 'bengaluru'.capitalize().find('benga')