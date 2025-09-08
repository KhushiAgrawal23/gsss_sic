import sys

class Menu:
    def __init__(self):
        print('Welcome to Menu Program')

    def create(self):
        print('Row created')

    def read(self):
        
        print('Row retrieved')

    def update(self):
        self.ml_marks = 90
        print('Row updated')

    def delete(self):
        print('Row deleted')

    def list_all(self):
        print('Rows listed')

    def exit_program(self):
        sys.exit('End of program')

    def invalid_choice(self):
        print('Invalid choice entered')

    def run_menu(self, choice):
        match choice:
            case 1 : self.create()
            case 2 : self.read()
            case 3 : self.update()
            case 4 : self.delete()
            case 5 : self.list_all()
            case 6 : self.exit_program()
            case _ : self.invalid_choice()

def start_app():
    menu = Menu() # created an object of class Menu
    while True:
        print('1:Create 2:Read 3:Update 4:Delete 5:List All 6:Exit')
        choice = int(input('Your choice please: '))
        menu.run_menu(choice)

start_app()

# Method chaining: 'bengaluru'.capitalize().find('benga')