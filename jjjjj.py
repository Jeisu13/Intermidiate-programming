import datetime

print(f"GNCI Payroll System".center(75, "-"))
cy = datetime.datetime.now().year
print(f"Year: {cy} - {cy + 1}".center(75, " "))
print(f"Guagua, Pampanga".center(75, "-"))

employees = []

def get_tax_rate(civil_status, total_dependents):
    if civil_status == "M":
        return 0.08 if total_dependents <= 1 else 0.05 if total_dependents <= 3 else 0.03
    return 0.10

def input_dependents(civil_status):
    if civil_status == 'M':
        while True:
            try:
                num = int(input("Number of Dependents: "))
                if num >= 0:
                    return num
                print("Number of dependents cannot be negative.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return 0

def add_record():
    print("-" * 76 + "\nAdding Records".center(75) + "\n" + "-" * 76)
    name = input("Name: ").upper()
    address = input("Address: ").upper()
    
    while (civil_status := input("Civil Status [M]-Married / [S]-Single: ").upper()) not in ('M', 'S'):
        print("Invalid input! Please enter 'M' or 'S'.")

    num_dependents = input_dependents(civil_status)
    tax_rate = get_tax_rate(civil_status, num_dependents)
    employee_number = len(employees) + 1
    employees.append((employee_number, name, address, "MARRIED" if civil_status == 'M' else "SINGLE", num_dependents, tax_rate))

    print(f"\nEmployee Number: {employee_number}\nName: {name}\nAddress: {address}\nCivil Status: {'MARRIED' if civil_status == 'M' else 'SINGLE'}\nNumber of Dependents: {num_dependents}\nTax Rate: {tax_rate:.2f}\nRecord added successfully!")

def display_record():
    if not employees:
        print("No records to display.")
        return
    print("-" * 76 + "\nDisplay Records".center(75) + "\n" + "-" * 76)
    for emp in employees:
        print(f"Employee Number: {emp[0]}\nName: {emp[1]}\nAddress: {emp[2]}\nCivil Status: {emp[3]}\nNumber of Dependents: {emp[4]}\nTax Rate: {emp[5]:.2f}\n" + "-" * 30)

def edit_record():
    if not employees:
        print("No records to edit.")
        return

    while True:
        try:
            emp_num = int(input("Enter Employee Number to edit: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid employee number.")

    for i, emp in enumerate(employees):
        if emp[0] == emp_num:
            print(f"Editing record for Employee Number: {emp_num}")
            name = input("Enter new name: ").upper() or emp[1]
            address = input("Enter new address: ").upper() or emp[2]

            while (civil_status = input("Civil Status [M]-Married / [S]-Single: ").upper()) not in ('M', 'S'):
                print("Invalid input! Please enter 'M' or 'S'.")

            num_dependents = input_dependents(civil_status)
            tax_rate = get_tax_rate(civil_status, num_dependents)
            employees[i] = (emp_num, name, address, "MARRIED" if civil_status == 'M' else "SINGLE", num_dependents, tax_rate)

            print(f"\nRecord updated successfully!\nNew Name: {name}\nNew Address: {address}\nNew Civil Status: {'MARRIED' if civil_status == 'M' else 'SINGLE'}\nNumber of Dependents: {num_dependents}\nNew Tax Rate: {tax_rate:.2f}\n")
            return
    
    print(f"Employee Number {emp_num} not found.")

def menu():
    while True:
        option = input("\nChoose Option\n1. Add\n2. Edit\n3. Display\n4. Exit\nSelect Option (1-4): ").strip()
        if option == '1': add_record()
        elif option == '2': edit_record()
        elif option == '3': display_record()
        elif option == '4': print("Exiting the program."); break
        else:
            print("Invalid option. Please try again.")

menu()