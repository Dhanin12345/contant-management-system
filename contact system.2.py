import re

class Contact:
    """
    Represents a single contact with name, phone, email (Gmail), and age.
    """
    def __init__(self, name, phone, gmail, age):
        self.name = name
        self.phone = phone
        self.gmail = gmail
        self.age = age

    def __str__(self):
        """
        Returns a user-friendly string representation of the contact.
        """
        return (f"Name: {self.name}\n"
                f"  Phone: {self.phone}\n"
                f"  Gmail: {self.gmail}\n"
                f"  Age: {self.age} years")

class ContactManager:
    """
    Manages a collection of Contact objects with CRUD operations.
    """
    def __init__(self):
        # Dictionary to store contacts: {name (str): Contact object}
        self.contacts = {}

    def validate_input(self, data_type, value):
        """
        Performs basic validation for phone and age.
        """
        if data_type == 'phone':
            # Simple check for 10-15 digits, allowing spaces, hyphens, and parentheses
            pattern = r"^\+?\d[\d\s\-\(\)]{8,14}\d$"
            if not re.match(pattern, value):
                return False, "Invalid phone number format."
        
        elif data_type == 'age':
            try:
                age = int(value)
                if not (0 <= age <= 120):
                    return False, "Age must be a number between 0 and 120."
            except ValueError:
                return False, "Age must be a valid number."
        
        return True, ""

    def add_contact(self, name, phone, gmail, age):
        """
        Adds a new contact after validating the age and phone number.
        """
        name = name.strip()
        
        if not name:
            print("\n❌ Error: Name cannot be empty.")
            return

        if name in self.contacts:
            print(f"\n❌ Error: Contact with name '{name}' already exists.")
            return
            
        # Validate inputs
        phone_valid, phone_error = self.validate_input('phone', phone)
        age_valid, age_error = self.validate_input('age', age)
        
        if not phone_valid:
            print(f"\n❌ Validation Error (Phone): {phone_error}")
            return
        
        if not age_valid:
            print(f"\n❌ Validation Error (Age): {age_error}")
            return

        new_contact = Contact(name, phone, gmail, int(age))
        self.contacts[name] = new_contact
        print(f"\n✅ Success: Contact '{name}' added successfully!")

    def view_all_contacts(self):
        """
        Displays all contacts in the system.
        """
        if not self.contacts:
            print("\nℹ️ The contact list is empty.")
            return

        print("\n--- All Contacts ---")
        # 
        for name, contact in self.contacts.items():
            print(f"--------------------")
            print(contact)
        print("--------------------")

    def search_contact(self, query):
        """
        Searches for a contact by name (partial match is allowed).
        """
        results = []
        query = query.lower()
        
        for name, contact in self.contacts.items():
            if query in name.lower():
                results.append(contact)
        
        if results:
            print(f"\n--- Search Results for '{query}' ---")
            for contact in results:
                print(f"----------------------------------")
                print(contact)
            print("----------------------------------")
        else:
            print(f"\nℹ️ No contacts found matching '{query}'.")

    def delete_contact(self, name):
        """
        Deletes a contact by their exact name.
        """
        name = name.strip()
        if name in self.contacts:
            del self.contacts[name]
            print(f"\n✅ Success: Contact '{name}' deleted.")
        else:
            print(f"\n❌ Error: Contact with name '{name}' not found.")

# --- Main Program Loop ---

def run_contact_manager():
    """
    The main function to run the command-line interface.
    """
    manager = ContactManager()
    
    # Adding an initial contact for testing
    manager.add_contact("Elon Musk", "310-555-0100", "elon.musk@x.com", "54")
    manager.add_contact("Gwynne Shotwell", "3105550200", "gwynne@spacex.com", "62")
    
    print("\n\n*** Welcome to the Python Contact Manager ***")
    
    while True:
        print("\n--- Menu ---")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search Contact (by name)")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            print("\n--- Add New Contact ---")
            name = input("Enter Name: ").strip()
            phone = input("Enter Phone: ").strip()
            # Note: A real system would also validate the Gmail format
            gmail = input("Enter Gmail Address: ").strip() 
            age = input("Enter Age: ").strip()
            
            manager.add_contact(name, phone, gmail, age)
        
        elif choice == '2':
            manager.view_all_contacts()
            
        elif choice == '3':
            query = input("\nEnter name or part of a name to search: ").strip()
            if query:
                manager.search_contact(query)
            else:
                print("\n❌ Error: Search query cannot be empty.")

        elif choice == '4':
            name = input("\nEnter the **exact** name of the contact to delete: ").strip()
            manager.delete_contact(name)
            
        elif choice == '5':
            print("\n👋 Thank you for using the Contact Manager. Goodbye!")
            break
            
        else:
            print("\n❌ Invalid choice. Please enter a number between 1 and 5.")

# Run the system
if __name__ == "__main__":
    run_contact_manager()