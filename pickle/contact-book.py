#use of pickle to make a contack book to perform CRUD functions


import pickle

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name}: {self.phone}"


class ContactBook:
    def __init__(self):
        self.contacts = {}
        self.load_contacts()

    def load_contacts(self):
        try:
            with open("contacts.pkl", "rb") as file:
                self.contacts = pickle.load(file)
        except (FileNotFoundError, EOFError):
            self.contacts = {}

    def save_contacts(self):
        with open("contacts.pkl", "wb") as file:
            pickle.dump(self.contacts, file)

    def add_contact(self, name, phone):
        if name in self.contacts:
            print(f"Contact '{name}' already exists.")
        else:
            self.contacts[name] = Contact(name, phone)
            self.save_contacts()
            print(f"Contact '{name}' added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        print("Contacts:")
        for contact in self.contacts.values():
            print(contact)

    def update_contact(self, name, new_phone):
        if name in self.contacts:
            self.contacts[name].phone = new_phone
            self.save_contacts()
            print(f"Contact '{name}' updated.")
        else:
            print(f"Contact '{name}' does not exist.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"Contact '{name}' deleted.")
        else:
            print(f"Contact '{name}' does not exist.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            contact_book.add_contact(name, phone)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            name = input("Enter contact name to update: ")
            new_phone = input("Enter new phone number: ")
            contact_book.update_contact(name, new_phone)

        elif choice == '4':
            name = input("Enter contact name to delete: ")
            contact_book.delete_contact(name)

        elif choice == '5':
            print("Exiting the Contact Book.")
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
