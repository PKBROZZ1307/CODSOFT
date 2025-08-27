import sys

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        self.contacts.append(Contact(name, phone, email, address))
        print(f"Contact '{name}' added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        print("\nContact List:")
        for idx, c in enumerate(self.contacts, 1):
            print(f"{idx}. {c.name} - {c.phone}")

    def search_contact(self, query):
        found = [c for c in self.contacts if query.lower() in c.name.lower() or query in c.phone]
        if not found:
            print("No matching contacts found.")
            return
        for c in found:
            print(f"Name: {c.name}\nPhone: {c.phone}\nEmail: {c.email}\nAddress: {c.address}\n")

    def update_contact(self, query):
        for c in self.contacts:
            if query.lower() == c.name.lower() or query == c.phone:
                print(f"Updating contact '{c.name}'")
                c.name = input("New name (leave blank to keep current): ") or c.name
                c.phone = input("New phone (leave blank to keep current): ") or c.phone
                c.email = input("New email (leave blank to keep current): ") or c.email
                c.address = input("New address (leave blank to keep current): ") or c.address
                print("Contact updated.")
                return
        print("Contact not found.")

    def delete_contact(self, query):
        for i, c in enumerate(self.contacts):
            if query.lower() == c.name.lower() or query == c.phone:
                print(f"Deleting contact '{c.name}'")
                del self.contacts[i]
                print("Contact deleted.")
                return
        print("Contact not found.")


def main():
    book = ContactBook()
    while True:
        print("\nContact Book CLI")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            book.add_contact(name, phone, email, address)
        elif choice == '2':
            book.view_contacts()
        elif choice == '3':
            query = input("Enter name or phone to search: ")
            book.search_contact(query)
        elif choice == '4':
            query = input("Enter name or phone to update: ")
            book.update_contact(query)
        elif choice == '5':
            query = input("Enter name or phone to delete: ")
            book.delete_contact(query)
        elif choice == '6':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
