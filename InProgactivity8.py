N = [""] * 10
y = 1

for x in range(10):
    name = input(f"Enter Name {x + 1}: ")
    if name:
        N[x] = name

print(f"\nLIST OF NAMES")
for x in range(len(N)):
    if N[x]:
        print(f"{y + x}. {N[x]}")

while True:
    print("\nMenu:")
    print("1. Add a new name")
    print("2. Exit")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        new_name = input("Enter the new name: ")
        if "" in N:
            index = N.index("")
            N[index] = new_name
        else:
            N.append(new_name)

        print("\nUpdated List:")
        for x in range(len(N)):
            if N[x]:
                print(f"{y + x}. {N[x]}")

    elif choice == "2":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter '1' or '2'.")
