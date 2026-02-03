import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email
    }
    save_contacts(contacts)
    print("✅ Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("📭 No contacts found.")
        return

    for name, info in contacts.items():
        print(f"\nName: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")

def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"\nName: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
    else:
        print("❌ Contact not found.")

def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("🗑️ Contact deleted.")
    else:
        print("❌ Contact not found.")

def main():
    contacts = load_contacts()

    while True:
        print("\n📖 Contact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice.")

if __name__ == "__main__":
    main()
