class ContactBook:
    def _init_(self):
        self.contacts = {}

    def add_contact(self, name, number):
        """Add a contact to the contact book."""
        self.contacts[name] = number
        print("Contact added successfully.")

    def remove_contact(self, name):
        """Remove a contact from the contact book."""
        if name in self.contacts:
            del self.contacts[name]
            print("Contact removed successfully.")
        else:
            print("Contact not found.")

    def search_contact(self, name):
        """Search for a contact in the contact book."""
        if name in self.contacts:
            print(f"Name: {name}, Number: {self.contacts[name]}")
        else:
            print("Contact not found.")

    def display_contacts(self):
        """Display all contacts in the contact book."""
        if self.contacts:
            print("Contacts:")
            for name, number in self.contacts.items():
                print(f"Name: {name}, Number: {number}")
        else:
            print("Contact book is empty.")


def main():
    contact_book = ContactBook()
    while True:
        print("\n1. Add Contact\n2. Remove Contact\n3. Search Contact\n4. Display Contacts\n5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            contact_book.add_contact(name, number)
        elif choice == "2":
            name = input("Enter contact name to remove: ")
            contact_book.remove_contact(name)
        elif choice == "3":
            name = input("Enter contact name to search: ")
            contact_book.search_contact(name)
        elif choice == "4":
            contact_book.display_contacts()
        elif choice == "5":
            print("Exiting contact book.")
            break
        else:
            print("Invalid choice. Please choose again.")


if _name_ == "_main_":
    main()
