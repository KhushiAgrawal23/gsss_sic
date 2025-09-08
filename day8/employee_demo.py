# from db_operations import EmployeeOperations as oprs, Employee as emp
import sys
from db_operations import EmployeeOperations as EmpOprs

class Menu:
    def __init__(self):
        print('Welcome to Employee CRUD Operations')

    def exit_program(self):
        sys.exit('End of program')

    def invalid_choice(self):
        print('Invalid choice entered')

    def run_menu(self, choice, employee_oprs):
        match choice:
            case 1 : employee_oprs.create_row()
            case 2 : employee_oprs.search_row()
            case 3 : employee_oprs.update_row()
            case 4 : employee_oprs.delete_row()
            case 5 : employee_oprs.list_all_rows()
            case 6 : self.exit_program()
            case _ : self.invalid_choice()

    def start_app(self):
        employee_oprs = EmpOprs()
        while True:
            print('1:Insert 2:Search 3:Update 4:Delete 5:ListAll 6:Exit')
            choice = int(input('Your choice please: '))
            self.run_menu(choice, employee_oprs)

menu = Menu()
menu.start_app()