import datetime
def errCS(prompt):
    while True:
        value = input(prompt).upper()
        if value in ('M', 'S'):
            return value
        print("Invalid! Enter 'M' or 'S'.")
def dependents(civil_status):
    return 0.08 if civil_status == 'M' else 0.10
def edit(employees):
    print("-" * 76 + "\nEDIT Records".center(75) + "\n" + "-" * 76)
    x = input("Enter name to update: ").upper()
    for i in range(len(employees)):
        if x == employees[i][1]:
            emp = employees[i]
            print(f"Name : {emp[1]}\nAddress : {emp[2]}")
            print(f"Civil Status : {'MARRIED' if emp[3] == 'M' else 'SINGLE'}")
            print(f"Tax Rate : {emp[5]:.0%}\nRate per Hour : PhP{emp[6]:.2f}")
            print("Press Enter to retain the current value...")
            mname = input("Name: ") or emp[1]
            maddress = input("Address: ") or emp[2]
            mcs = errCS("Civil Status [M]-Married / [S]-Single: ") or emp[3]
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
        employees[i] = (emp[0], mname.upper(), maddress.upper(), mcs.upper(), emp[4], dependents(mcs), tax_rate, emp[6])
        ans = input("Save changes? (Y/N) ")
        print("Changes are saved!" if ans.upper() == "Y" else "Changes are not saved!"); break
    else:
        print(f"{x} is not found!")
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
        while True:
            try:
                rph = float(input("Rate per Hour: ")); break
            except ValueError:
                print("Enter a valid number.")
        employees.append((len(employees) + 1, name, address, 
                          "MARRIED" if civil_status == 'M' else "SINGLE", 
                          num_dependents, tax_rate, rph))
        print(f"\nEmployee Number: {len(employees)}\nName: {name}\nAddress: {address}\n"
              f"Civil Status: {'MARRIED' if civil_status == 'M' else 'SINGLE'}\n"
              f"Dependents: {num_dependents}\nTax Rate: {tax_rate:.2f}\n"
              f"Rate per Hour: PhP{rph:.2f}\nRecord added!")
    elif option == '2':
        edit(employees)
    elif option == '3':
        if not employees:
            print("No records to display.")
        else:
            print("-" * 76 + "\nDisplay Records".center(75) + "\n" + "-" * 76)
            for emp in employees:
                print(f"\nEmployee Number: {emp[0]}\nName: {emp[1]}\nAddress: {emp[2]}\n"
                      f"Civil Status: {'MARRIED' if emp[3] == 'M' else 'SINGLE'}\n"
                      f"Dependents: {emp[4]}\nTax Rate: {emp[5]:.2f}\n"
                      f"Rate per Hour: PhP{emp[6]:.2f}\n")
    elif option == '4':
        print("Exiting the program."); break
    else:
        print("Invalid option.")
