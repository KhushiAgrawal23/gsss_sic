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

def run_menu(choice):
    match choice:
       case 1 : create()
       case 2 : read()
       case 3 : update()
       case 4 : delete()
       case 5 : list_all()
       case 6 : exit_program()
       case _ : invalid_choice()

def start_app():
    while True:
        print('1:Create 2:Read 3:Update 4:Delete 5:List All 6:Exit')
        choice = int(input('Your choice please: '))
        run_menu(choice)

start_app()

# Method chaining: 'bengaluru'.capitalize().find('benga')