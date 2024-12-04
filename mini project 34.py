def display_menu():
    print("\n--- Contact Book  ---")
    print("1. Add a New Contact")
    print("2. Search for a Contact")
    print("3. Delete a Contact")
    print("4. View All Contacts")
    print("5. Exit")
def add_contact(contact_book):
    name = input("Enter the contact's name: ")
    phone_number = input("Enter the phone number: ")
    contact_book[name] = phone_number
    print(f"Contact for {name} added successfully.")


def search_contact(contact_book):
    name = input("Enter the contact's name to search: ")
    if name in contact_book:
        print(f"{name} - {contact_book[name]}")
    else:
        print("Contact not found.")


def delete_contact(contact_book):
    name = input("Enter the contact's name to delete: ")
    if name in contact_book:
        del contact_book[name]
        print(f"Contact for {name} deleted successfully.")
    else:
        print("Contact not found.")


def view_contacts(contact_book):
    if contact_book:
        print("\n--- All Contacts ---")
        for name, phone_number in contact_book.items():
            print(f"{name} - {phone_number}")
    else:
        print("No contacts available.")


def main():
    contact_book = {}  # Initialize an empty dictionary to store contacts
    print('program started')
    while True:
        display_menu()  # Show menu
        choice = input("Choose an option (1-5): ")
        if choice == '1':

            add_contact(contact_book)
        elif choice == '2':

            search_contact(contact_book)
        elif choice == '3':
            delete_contact(contact_book)
        elif choice == '4':
            view_contacts(contact_book)
        elif choice == '5':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
    