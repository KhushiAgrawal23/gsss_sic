from flask import Flask, jsonify, request
from db_operations import EmployeeOperations as EmpOprs, Employee

employees = EmpOprs()
employees.create_database()
employees.create_table()

app = Flask(__name__)

@app.route('/employees',methods=['POST'])
def employees_create():
    body = request.get_json()
    new_employee = Employee(body['name'], body['designation'], body['phone_number'], body['commission'], body['salary'], body['years_of_exp'], body['location'])
    print(new_employee)
    id = employees.insert_row(new_employee)
    employee = employees.search_row(id)
    employee_dict = {'id':employee[0], 'name':employee[1], 'designation':employee[2], 'phone_number':employee_dict[3], 'commission': employee[4], 'salary': employee[5], 'years_of_exp': employee[6], 'location': employee[7]}
    return jsonify(employee_dict)

@app.route('/employees/<id>',methods=['GET'])
def employees_read_by_id(id):
    employee = employees.search_row(id)
    if employee == None:
        return jsonify("Employee not found")
    employee_dict = {'id':employee[0], 'name':employee[1], 'designation':employee[2], 'phone_number':employee[3], 'commission':employee[4], 'salary':employee[5], 'years_of_exp':employee[6], 'location': employee[7]}
    return jsonify(employee_dict)

@app.route('/employees',methods=['GET'])
def employees_read_all():
    employees_list = employees.list_all_rows()
    employees_list = []
    for employee in employees_list:
        employees_list.append({'id':employee[0], 'name':employee[1], 'designation':employee[2], 'phone_number':employee[3], 'commission':employee[4], 'salary':employee[5], 'years_of_exp':employee[6], 'location': employee[7]})
    return jsonify(employees_list)

@app.route('/employees/<id>',methods=['PUT'])
def employees_update(id):
    body = request.get_json()
    old_employee_obj = employees.search_row(id)
    if not old_employee_obj:
        return jsonify({'message': 'Employee not found'})
    old_employee_obj = []
    old_employee_obj.append(body['name'])
    old_employee_obj.append(body['designation'])
    old_employee_obj.append(body['phone_number'])
    old_employee_obj.append(body['commission'])
    old_employee_obj.append(body['salary'])
    old_employee_obj.append(body['years_of_exp'])
    old_employee_obj.append(body['location'])
    old_employee_obj.append(id)
    old_employee_obj = tuple(old_employee_obj)
    employees.update_row(old_employee_obj)

    employee = employees.search_row(id)
    employee_dict = {'id':employee[0], 'name':employee[1], 'designation':employee[2], 'phone_number':employee[3], 'commission':employee[4], 'salary':employee[5], 'years_of_exp':employee[6], 'location': employee[7]}
    return jsonify(employee_dict)

@app.route('/employees/<id>',methods=['DELETE'])
def employees_delete(id):
    old_employee_obj = employees.search_row(id)
    if not old_employee_obj:
        return jsonify({'message': 'Employee not found', 'is_error': 1})
    employees.delete_row(id)
    return jsonify({'message': 'Employee is deleted', 'is_error': 0})

app.run(debug=True)