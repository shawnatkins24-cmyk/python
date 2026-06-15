# Clinic Patient Record System - Simple Version

def show_welcome():
    print("========================================")
    print(" VICTORIA UNIVERSITY HEALTH CENTRE")
    print(" Patient Record System v1.0")
    print("========================================")

def preload_patients():
    # List of tuples: ID, Name, Age, Blood Type, Phone
    patients = [
        ("PAT-0001", "John Kasasa",35,"O+","0772123456"),
        ("PAT-0002", "Mary Sserunjoji",28,"A+","0772987654"),
        ("PAT-0003", "Allan Okello",42,"B+","0773567890"),
        ("PAT-0004", "Enock Namuli",25,"AB+","0774123456"),
        ("PAT-0005", "David Ssewagudde",60,"O-","0775234567")
    ]
    return patients

def add_patient(patients):
    print("\n--- Add New Patient ---")

    # Generate ID like PAT-0006
    new_id = "PAT-" + str(len(patients) + 1).zfill(4)
    print("Your Patient ID is:", new_id)

    name = input("Enter Full Name: ")
    name = name.strip().title() # string method 1 & 2

    # Age validation
    age_input = input("Enter Age: ")
    if not age_input.isdigit():
        print("Error: Age must be a number")
        return
    age = int(age_input)
    if age < 1 or age > 120:
        print("Error: Age must be between 1 and 120")
        return

    blood_type = input("Enter Blood Type: ").upper() # string method 3

    # Phone validation
    phone = input("Enter Phone Number (10 digits): ")
    phone = phone.strip() # string method 4
    if not phone.isdigit() or len(phone)!= 10:
        print("Error: Phone must be exactly 10 digits")
        return

    # Add to list
    patients.append((new_id, name, age, blood_type, phone))
    print("Patient added successfully!")

def search_patient(patients):
    search_name = input("\nEnter name to search: ").lower() # string method 5
    found = False

    print("\n--- Search Results ---")
    for p in patients:
        if search_name in p[1].lower(): # check if name contains search text
            print(p)
            found = True

    if not found:
        print("No patient found.")

def update_phone(patients):
    pid = input("\nEnter Patient ID: ").upper()
    for i in range(len(patients)):
        if patients[i][0] == pid:
            print("Current phone:", patients[i][4])
            new_phone = input("Enter new phone: ")
            if new_phone.isdigit() and len(new_phone) == 10:
                # Rebuild the tuple since tuples can't be changed
                patients[i] = (patients[i][0], patients[i][1], patients[i][2], patients[i][3], new_phone)
                print("Phone updated!")
            else:
                print("Error: Phone must be 10 digits")
            return
    print("Patient ID not found.")

def display_patients(patients):
    if len(patients) == 0:
        print("No patient records found.")
        return

    print("\n{:<10} {:<20} {:<5} {:<10} {:<12}".format("ID", "Name", "Age", "Blood", "Phone")) # string method 6
    print("-" * 60)
    for p in patients:
        print("{:<10} {:<20} {:<5} {:<10} {:<12}".format(p[0], p[1], p[2], p[3], p[4]))

def display_statistics(patients):
    if len(patients) == 0:
        print("No patients to show statistics for.")
        return

    total = len(patients)

    # Calculate average age
    total_age = 0
    for p in patients:
        total_age = total_age + p[2]
    avg_age = round(total_age / total, 1)

    # Find youngest and oldest
    youngest = patients[0]
    oldest = patients[0]
    for p in patients:
        if p[2] < youngest[2]:
            youngest = p
        if p[2] > oldest[2]:
            oldest = p

    print("\n--- Statistics Report ---")
    print("Total Patients:", total)
    print("Average Age:", avg_age)
    print("Youngest:", youngest[1], "(", youngest[2], "years )")
    print("Oldest:", oldest[1], "(", oldest[2], "years )")

def show_menu():
    print("\n--- Main Menu ---")
    print("1. Add New Patient")
    print("2. Search Patient by Name")
    print("3. Update Patient Phone Number")
    print("4. Display All Patients")
    print("5. Display Statistics Report")
    print("6. Exit")

def main():
    show_welcome()
    patients = preload_patients()

    while True:
        try:
            show_menu()
            choice = input("Enter choice 1-6: ")

            if choice == "1":
                add_patient(patients)
            elif choice == "2":
                search_patient(patients)
            elif choice == "3":
                update_phone(patients)
            elif choice == "4":
                display_patients(patients)
            elif choice == "5":
                display_statistics(patients)
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

        except Exception as e:
            print("Error:", e)

        input("Press Enter to continue...")

if __name__ == "__main__":
    main()