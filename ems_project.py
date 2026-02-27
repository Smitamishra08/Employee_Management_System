# Employee Management System (EMS)

employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}
}

# Function: Add Employee

def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))

        # Check if ID already exists.
        if emp_id in employees:
            print("Employee ID already exists! Please try another ID.")
            return
        
        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        department = input("Enter Employee Department: ")
        salary = float(input("Enter Employee Salary: "))

        # Add to dictionary
        employees[emp_id] = {
            'name': name,
            'age': age,
            'department': department,
            'salary': salary
        }

        print("Employee added successfully!")

    except ValueError:
        print("Invalid input! Please enter correct data type.")

# Function: View All Employees

def view_employees():
    if not employees:
        print("No employees available.")
        return
    
    print("\n==========Employee List==========")
    print("ID\tName\tAge\tDepartment\tSalary")
    print("-----------------------------------------")

    for emp_id, details in employees.items():
        print(f"{emp_id}\t{details['name']}\t{details['age']}\t{details['department']}\t{details['salary']}")


# Function : Search Employee.

def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))

        if emp_id in employees:
            emp = employees[emp_id]
            print("\nEmployee Found:")
            print("-----------------------")
            print("Name:", emp['name'])
            print("Age:", emp['age'])
            print("Department:", emp['department'])
            print("Salary:", emp['salary'])
        else:
            print("Employee not found.")

    except ValueError:
        print("Invalid ID entered.")

# Function: Main Menu
def main_menu():
    while True:
        print("\n=====Employee Management System ==================")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank you for using Employee Management System!")
            break
        else:
            print("Invalid choice! Please select between 1 to 4.")


# Run the Program.

if __name__ == "__main__":
    main_menu()






    