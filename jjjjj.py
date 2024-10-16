import datetime
print(f"GNCI Payroll System".center(75, "-"))
cy = datetime.datetime.now().year
print(f"Year: {cy} - {cy + 1}".center(75, " "))
print(f"Guagua, Pampanga".center(75, "-"))
employees = []
while True:
    option = input("\nChoose Option\n1. Add\n2. Edit\n3. Display\n4. Exit\nSelect Option (1-4): ")
    if option == '1':
        print("-" * 76 + "\nAdding Records".center(75) + "\n" + "-" * 76)
        name = input("Name: ").upper()
        address = input("Address: ").upper()
        civil_status = input("Civil Status [M/S]: ").upper()
        while civil_status not in ('M', 'S'):
            civil_status = input("Invalid! Enter 'M' or 'S': ").upper()
        num_dependents = 0
        if civil_status == 'M':
            while True:
                try:
                    num_dependents = int(input("Number of Dependents: "))
                    if num_dependents >= 0: break
                    print("Cannot be negative.")
                except ValueError:
                    print("Enter a valid number.")
        tax_rate = (0.08 if civil_status == 'M' and num_dependents <= 1 else
                    0.05 if civil_status == 'M' and num_dependents <= 3 else
                    0.03 if civil_status == 'M' else 0.10)
        employees.append((len(employees) + 1, name, address, "MARRIED" if civil_status == 'M' else "SINGLE", num_dependents, tax_rate))
        print(f"\nEmployee Number: {len(employees)}\nName: {name}\nAddress: {address}\nCivil Status: {'MARRIED' if civil_status == 'M' else 'SINGLE'}\nDependents: {num_dependents}\nTax Rate: {tax_rate:.2f}\nRecord added!")
    elif option == '2':
        while True:
            try:
                emp_num = int(input("Enter Employee Number to edit: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid employee number."
        for i, emp in enumerate(employees):
            if emp[0] == emp_num:
                name = input("New name: ").upper() or emp[1]
                address = input("New address: ").upper() or emp[2]
                civil_status = input("Civil Status [M/S]: ").upper()
                while civil_status not in ('M', 'S'):
                    civil_status = input("Invalid! Enter 'M' or 'S': ").upper() or emp[3]
                num_dependents = 0
                if civil_status == 'M':
                    while True:
                        try:
                            num_dependents = int(input("Number of Dependents: ")) or emp[4]
                            if num_dependents >= 0: break
                            print("Cannot be negative.")
                        except ValueError:
                            print("Enter a valid number.")
                tax_rate = (0.08 if civil_status == 'M' and num_dependents <= 1 else
                            0.05 if civil_status == 'M' and num_dependents <= 3 else
                            0.03 if civil_status == 'M' else 0.10) or emp[5]
                employees[i] = (emp_num, name, address, "MARRIED" if civil_status == 'M' else "SINGLE", num_dependents, tax_rate)
                print(f"\nRecord updated for {name}!")
                break
        else:
            print(f"Employee Number {emp_num} not found.")
    elif option == '3':
        if not employees:
            print("No records to display.")
        else:
            print("-" * 76 + "\nDisplay Records".center(75) + "\n" + "-" * 76)
            for emp in employees:
                print(f"Employee Number: {emp[0]}\nName: {emp[1]}\nAddress: {emp[2]}\nCivil Status: {emp[3]}\nDependents: {emp[4]}\nTax Rate: {emp[5]:.2f}\n" + "-" * 30)
    elif option == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid option.")
