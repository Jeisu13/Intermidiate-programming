N = [""] * 10
y = 1

for x in range(10):
    name = input(f"Enter Name {x + 1}: ")
    if name:
        N[x] = name

z = input("Enter your Name to search: ")

if z in N:
    print(f"{z} is found in the list.")
else:
    print(f"{z} is not found in the list.")
    print("Ending the program.")

print(f"\nLIST OF NAMES")
for x in range(len(N)):
    if N[x]:
        print(f"{y + x}. {N[x]}")

while True:
    print("\nMenu:")
    print("1. Update a name")
    print("2. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        old_name = input("Enter the name you want to update: ")
        if old_name in N:
            new_name = input("Enter the new name: ")
            index = N.index(old_name)
            N[index] = new_name
            print(f"Updated {old_name} to {new_name}.")
        else:
            print(f"{old_name} is not found in the list.")

        print("\nUpdated List:")
        for x in range(len(N)):
            if N[x]:
                print(f"{y + x}. {N[x]}")

    elif choice == "2":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter '1', '2', or '3'.")
