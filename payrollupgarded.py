import datetime

# Print system title and year
print(f"GNCI Payroll System".center(75, "-"))
cy = datetime.datetime.now().year
next_year = cy + 1
print(f"Year: {cy} - {next_year}".center(75, " "))
print(f"Guagua, Pampanga".center(75, "-"))

# Constants
PHILHEALTH, SSS, PAGIBIG = 350, 250, 500
month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Lists to store salary details
employees = []
gross_salaries = []
net_salaries = []
taxes = []
contributions_list = []
loan_payments = []

# Function to get tax rate based on civil status and dependents
def get_tax_rate(civil_status, total_dependents):
    if civil_status == "M":
        if total_dependents == 1:
            return 0.08
        elif 2 <= total_dependents <= 3:
            return 0.05
        else:
            return 0.03
    return 0.10

# Function to calculate deductions including tax, contributions, and loan payments
def calculate_deductions(gross_salary, tax_rate, loan_payment):
    tax = gross_salary * tax_rate
    contributions = PHILHEALTH + SSS + PAGIBIG
    deductions = tax + contributions + loan_payment
    return deductions, tax, contributions

# Function to calculate loan payment and remaining loan amount
def calculate_loan_payment(loan, loan_type, loan_amount, gross_salary):
    loan_payment = 0
    if loan:
        if loan_type in ("1", "2"):
            loan_payment = gross_salary * 0.01
        elif loan_type == "3":
            loan_payment = gross_salary * 0.02
        
        loan_payment = min(loan_payment, loan_amount)
        loan_amount -= loan_payment
    return loan_payment, loan_amount

# Function to display the summary for a specific month
def display_month_summary(month, gross_salary, hours_worked, rate, deductions, tax, contributions, loan_amount, loan_payment, net_salary):
    print("-" * 76)
    print(f"{month_names[month % 12]}".center(75))
    print("-" * 76)
    print(f"Gross Monthly Salary                     : PhP {gross_salary:,.2f}")
    print("-" * 76)
    print(f"Monthly Salary Details".center(71))
    print("-" * 76)
    print(f"        Total Hours Worked : {hours_worked} hours")
    print(f"        Rate per Hour           : PhP {rate:.2f}")
    print("-" * 76)
    print(f"Deductions".center(74))
    print("-" * 76)
    print(f"Deductions                             : PhP {deductions:,.2f}")
    print("-" * 76)
    print(f"Deductions Details".center(72))
    print("-" * 76)
    print(f"        BIR            : PhP {tax:,.2f}")
    print(f"        SSS           : PhP {SSS}")
    print(f"        PhilHealth  : PhP {PHILHEALTH}")
    print(f"        Pag-ibig     : PhP {PAGIBIG}")
    print("-" * 76)
    print(f"Loan Status".center(74))
    print("-" * 76)
    print(f"Current Loan Amount            : PhP {loan_amount:,.2f}")
    print(f"Amount Paid      : PhP {loan_payment:,.2f}")
    print("-" * 76)
    print(f"Take Home Pay".center(71))
    print("-" * 76)
    print(f"Net Monthly Salary                     : PhP {net_salary:,.2f}")

# Function to display the year-end summary
def display_year_summary():
    print("Year-End Summary".center(75, "-"))
    print(f"Total Gross Salary for the Year       : PhP {sum(gross_salaries):,.2f}")
    print(f"Total Net Salary for the Year         : PhP {sum(net_salaries):,.2f}")
    print(f"Total Tax Paid for the Year           : PhP {sum(taxes):,.2f}")
    print(f"Total Contributions for the Year      : PhP {sum(contributions_list):,.2f}")
    print(f"        Total PhilHealth Paid         : PhP {len(gross_salaries) * PHILHEALTH:,.2f}")
    print(f"        Total SSS Paid                : PhP {len(gross_salaries) * SSS:,.2f}")
    print(f"        Total Pag-ibig Paid           : PhP {len(gross_salaries) * PAGIBIG:,.2f}")
    print(f"Total Loan Payment for the Year       : PhP {sum(loan_payments):,.2f}")

# Function to update civil status and related details
def update_civil_status(employee):
    civil_status = input("New Civil Status [M]-Married / [S]-Single: ").upper()
    if civil_status == "M":
        number_of_children = int(input("Number of child/children: "))
        employee['Number of Children'] = number_of_children
    else:
        employee['Number of Children'] = 0
    employee['Civil Status'] = "MARRIED" if civil_status == "M" else "SINGLE"
    employee['Tax Rate'] = get_tax_rate(civil_status, employee['Number of Children'])
    print(f"\nRecord updated successfully! New tax rate is {employee['Tax Rate']:.2f}\n")

# Function to add an employee record
def add_record():
    print("-" * 76)
    print(f"Adding Records".center(75))
    print("-" * 76)
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

# Function to display all employee records
def display_record():
    if not employees:
        print("No records to display.")
        return
    
    print("-" * 76)
    print(f"Display Records".center(75))
    print("-" * 76)

    for emp in employees:
        print(f"Employee Number: {emp['Employee Number']}")
        print(f"Name: {emp['Name']}")
        print(f"Address: {emp['Address']}")
        print(f"Civil Status: {emp['Civil Status']}")
        print(f"Number of Children: {emp['Number of Children']}")
        print(f"Tax Rate: {emp['Tax Rate']:.2f}")
        print("-" * 30)

# Function to edit an employee record
def edit_record():
    if not employees:
        print("No records to edit.")
        return
    
    print("-" * 76)
    print(f"Update Record".center(75))
    print("-" * 76)
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

# Function to remove an employee record
def remove_record():
    if not employees:
        print("No records to remove.")
        return
    
    print("-" * 76)
    print(f"Delete Records".center(75))
    print("-" * 76)
    emp_num = int(input("Enter Employee Number to remove: "))
    for i, emp in enumerate(employees):
        if emp['Employee Number'] == emp_num:
            del employees[i]
            print(f"Employee {emp_num} removed successfully!")
            return
    
    print(f"Employee Number {emp_num} not found.")

# Function to search for an employee record by name
def search_record():
    if not employees:
        print("No records to search.")
        return
    print("-" * 76)
    print(f"Searching".center(75))
    print("-" * 76)
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

# Function to handle payroll for an employee
def handle_payroll():
    if not employees:
        print("No records to process payroll.")
        return
    print("-" * 76)
    print(f"Process Payroll".center(75))
    print("-" * 76)
    emp_num = int(input("Enter Employee Number for payroll: "))
    for emp in employees:
        if emp['Employee Number'] == emp_num:
            rate_per_hour = float(input("Rate per Hour: "))
            loan = input("Loan? [Y]-Yes / [N]-No: ").upper() == "Y"
            loan_type, loan_amount = "", 0

            if loan:
                loan_type = input("[1] SSS / [2] Pag-ibig / [3] SSS and Pag-ibig: ")
                loan_amount = float(input("Loan Amount: "))

            month, ans = 0, "Y"
            while ans.upper() == "Y":
                total_hours_worked = float(input(f"Total Hours Worked ({month_names[month % 12]}): "))
                gross_monthly_salary = rate_per_hour * total_hours_worked

                loan_payment, loan_amount = calculate_loan_payment(loan, loan_type, loan_amount, gross_monthly_salary)
                deductions, tax, contributions = calculate_deductions(gross_monthly_salary, emp['Tax Rate'], loan_payment)
                net_monthly_salary = gross_monthly_salary - deductions

                gross_salaries.append(gross_monthly_salary)
                net_salaries.append(net_monthly_salary)
                taxes.append(tax)
                contributions_list.append(contributions)
                loan_payments.append(loan_payment)

                display_month_summary(month, gross_monthly_salary, total_hours_worked, rate_per_hour, deductions, tax, contributions, loan_amount, loan_payment, net_monthly_salary)

                month += 1
                ans = input("Do you want to continue for another month? [Y]-Yes / [N]-No: ")

            return
    
    print(f"Employee Number {emp_num} not found.")

# Main menu function
def menu():
    while True:
        print("\nChoose Option")
        print("1. Add (Enter new record)")
        print("2. Edit (Update record)")
        print("3. Remove (Delete record)")
        print("4. Search (Look for a record)")
        print("5. Display (Show all records)")
        print("6. Payroll (Process payroll for an employee)")
        print("7. Year-End Summary")
        print("8. Exit (Terminate program)")
        
        option = input("Select Option (1-8): ").strip()
        
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
            handle_payroll()
        elif option == '7':
            display_year_summary()
        elif option == '8':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

menu()
