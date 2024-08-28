
N = [""] * 10
y = 1

for x in range(10):
    name = input(f"Enter Name {x + 1}: ")
    if name:
        N[x] = name

while True:
    print("\nMenu:")
    print("1. Search a name")
    print("2. Add a new name")
    print("3. Update an existing name")
    print("4. Display all names")
    print("5. Exit")
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        z = input("Enter the Name to search: ")

        if z in N:
            print(f"{z} is found in the list.")
        else:
            print(f"{z} is not found in the list.")

    elif choice == "2":
        new_name = input("Enter the new name: ")
        if "" in N:
            index = N.index("")
            N[index] = new_name
        else:
            N.append(new_name)
            print("Name added successfully.")

    elif choice == "3":
        old_name = input("Enter the name you want to update: ")
        if old_name in N:
            new_name = input("Enter the new name: ")
            index = N.index(old_name)
            N[index] = new_name
            print(f"Updated {old_name} to {new_name}.")
        else:
            print(f"{old_name} is not found in the list.")

    elif choice == "4":
        print(f"JAYCE COMPANY".center(75, "-"))
        print("\nLIST OF NAMES")
        for x in range(len(N)):
            if N[x]:
                print(f"{y + x}. {N[x]}")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter '1', '2', '3', '4', or '5'.")
