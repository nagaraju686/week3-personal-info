import json
import csv
import re
from datetime import datetime

DATA_FILE = "contacts_data.json"

def load_contacts():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except:
        return {}

def save_contacts(contacts):
    with open(DATA_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def validate_phone(phone):
    digits = re.sub(r"\D", "", phone)

    if 10 <= len(digits) <= 15:
        return True, digits

    return False, None

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def add_contact(contacts):

    print("\nADD CONTACT")

    name = input("Name: ").strip()

    if name in contacts:
        print("Contact already exists")
        return

    phone = input("Phone: ").strip()

    valid, phone = validate_phone(phone)

    if not valid:
        print("Invalid phone")
        return

    email = input("Email: ").strip()

    if email and not validate_email(email):
        print("Invalid email")
        return

    group = input("Group: ").strip() or "Other"

    contacts[name] = {
        "phone": phone,
        "email": email,
        "group": group,
        "created": datetime.now().isoformat()
    }

    save_contacts(contacts)

    print("Contact added successfully")

def search_contact(contacts):

    keyword = input("Search name: ").lower()

    found = False

    for name, info in contacts.items():

        if keyword in name.lower():

            print("\nName:", name)
            print("Phone:", info["phone"])
            print("Email:", info["email"])
            print("Group:", info["group"])

            found = True

    if not found:
        print("No contact found")

def update_contact(contacts):

    name = input("Enter contact name: ")

    if name not in contacts:
        print("Contact not found")
        return

    phone = input("New phone: ")

    valid, phone = validate_phone(phone)

    if valid:
        contacts[name]["phone"] = phone

    email = input("New email: ")

    if email:
        contacts[name]["email"] = email

    save_contacts(contacts)

    print("Updated successfully")

def delete_contact(contacts):

    name = input("Contact name: ")

    if name in contacts:

        del contacts[name]

        save_contacts(contacts)

        print("Deleted")

    else:
        print("Contact not found")

def display_contacts(contacts):

    if not contacts:
        print("No contacts available")
        return

    for name, info in contacts.items():

        print("\n-------------------")
        print("Name:", name)
        print("Phone:", info["phone"])
        print("Email:", info["email"])
        print("Group:", info["group"])

def export_csv(contacts):

    with open("contacts_export.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Name", "Phone", "Email", "Group"])

        for name, info in contacts.items():

            writer.writerow([
                name,
                info["phone"],
                info["email"],
                info["group"]
            ])

    print("CSV exported successfully")

def statistics(contacts):

    print("\nCONTACT STATISTICS")
    print("Total Contacts:", len(contacts))

    groups = {}

    for info in contacts.values():

        group = info["group"]

        groups[group] = groups.get(group, 0) + 1

    for group, count in groups.items():

        print(group, ":", count)

def menu():

    contacts = load_contacts()

    while True:

        print("\n====================")
        print("CONTACT MANAGEMENT")
        print("====================")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View Contacts")
        print("6. Export CSV")
        print("7. Statistics")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            search_contact(contacts)

        elif choice == "3":
            update_contact(contacts)

        elif choice == "4":
            delete_contact(contacts)

        elif choice == "5":
            display_contacts(contacts)

        elif choice == "6":
            export_csv(contacts)

        elif choice == "7":
            statistics(contacts)

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()