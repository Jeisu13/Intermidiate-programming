import datetime

print(f"GNCI Payroll System".center(75, "-"))
cy = datetime.datetime.now().year
next_year = cy + 1
print(f"Year: {cy} - {next_year}".center(75, " "))
print(f"Guagua, Pampanga".center(75, "-"))

employees = []


def get_tax_rate(civil_status, total_dependents):
    if civil_status == "M":
        if total_dependents == 1:
            return 0.08
        elif 2 <= total_dependents <= 3:
            return 0.05
        else:
            return 0.03
    return 0.10

def add_record():
    print(f"Adding Records".center(75, "-"))
    name = input("Name: ").upper()
    address = input("Address: ").upper()
    civil_status = input("Civil Status [M]-Married / [S]-Single: ").upper()

    if civil_status == 'M':
        num_children = int(input("Number of child/children: "))
    else:
        num_children = 0
    
    tax_rate = get_tax_rate(civil_status, num_children)
    
    employee = {
        'Employee Number': len(employees) + 1,
        'Name': name,
        'Address': address,
        'Civil Status': "MARRIED" if civil_status == 'M' else "SINGLE",
        'Number of Children': num_children,
        'Tax Rate': tax_rate
    }
    
    employees.append(employee)
    print(f"\nRecord added successfully! Tax rate is {tax_rate:.2f}\n")

def display_record():
    if not employees:
        print("No records to display.")
        return
    
    print(f"Display Records".center(75, "-"))
    
    for emp in employees:
        print(f"Employee Number: {emp['Employee Number']}")
        print(f"Name: {emp['Name']}")
        print(f"Address: {emp['Address']}")
        print(f"Civil Status: {emp['Civil Status']}")
        print(f"Number of Children: {emp['Number of Children']}")
        print(f"Tax Rate: {emp['Tax Rate']:.2f}")
        print("-" * 30)

def edit_record():
    if not employees:
        print("No records to edit.")
        return
    
    print(f"Update Record".center(75, "-"))
    emp_num = int(input("Enter Employee Number to edit: "))
    for emp in employees:
        if emp['Employee Number'] == emp_num:
            print(f"Editing record for Employee Number: {emp_num}")
            emp['Name'] = input("Enter new name: ").upper() or emp['Name']
            emp['Address'] = input("Enter new address: ").upper() or emp['Address']
            civil_status = input("Civil Status [M]-Married / [S]-Single: ").upper() or emp['Civil Status'][0]
            emp['Civil Status'] = "MARRIED" if civil_status == 'M' else "SINGLE"
            
            if civil_status == 'M':
                emp['Number of Children'] = int(input("Number of child/children: "))
            else:
                emp['Number of Children'] = 0
            
            emp['Tax Rate'] = get_tax_rate(civil_status, emp['Number of Children'])
            print(f"\nRecord updated successfully! New tax rate is {emp['Tax Rate']:.2f}\n")
            return
    
    print(f"Employee Number {emp_num} not found.")

def remove_record():
    if not employees:
        print("No records to remove.")
        return
    
    print(f"Delete Records".center(75, "-"))
    emp_num = int(input("Enter Employee Number to remove: "))
    for i, emp in enumerate(employees):
        if emp['Employee Number'] == emp_num:
            del employees[i]
            print(f"Employee {emp_num} removed successfully!")
            return
    
    print(f"Employee Number {emp_num} not found.")

def search_record():
    if not employees:
        print("No records to search.")
        return
    
    print(f"Searching".center(75, "-"))
    search_name = input("Enter name to search: ").upper()
    for emp in employees:
        if emp['Name'] == search_name:
            print(f"Employee Number: {emp['Employee Number']}")
            print(f"Name: {emp['Name']}")
            print(f"Address: {emp['Address']}")
            print(f"Civil Status: {emp['Civil Status']}")
            print(f"Number of Children: {emp['Number of Children']}")
            print(f"Tax Rate: {emp['Tax Rate']:.2f}")
            print("-" * 30)
            return
    
    print(f"No employee found with the name {search_name}.")

def menu():
    while True:
        print("\nChoose Option")
        print("1. Add (Enter new record)")
        print("2. Edit (Update record)")
        print("3. Remove (Delete record)")
        print("4. Search (Look for a record)")
        print("5. Display (Show all records)")
        print("6. Exit (Terminate program)")
        
        option = input("Select Option (1-6): ").strip()
        
        if option == '1':
            add_record()
        elif option == '2':
            edit_record()
        elif option == '3':
            remove_record()
        elif option == '4':
            search_record()
        elif option == '5':
            display_record()
        elif option == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

menu()
