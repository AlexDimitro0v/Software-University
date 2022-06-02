from abc import ABC, abstractmethod


class Directory(ABC):
    """
    A directory is a book which gives lists of facts, for example people's names, addresses, and phone numbers,
    or the names and addresses of business companies, usually arranged in alphabetical order...a telephone directory.
    
    It can also be:
    • an area of a computer disk which contains one or more files or other directories;
    • a list of the subjects that you can find information on (e.g. Yahoo - the oldest internet directory service).

    - Collins Dictionary's definition of the word "directory"
    """
    
    def __init__(self):
        self.directory = {}
    
    @abstractmethod
    def store_record(self, key, value):
        pass
    
    @abstractmethod
    def retrieve_record(self, key):
        pass
    
    @abstractmethod
    def delete_record(self, key):
        pass
    
    @abstractmethod
    def list_records(self):
        pass


class ContactsBook(Directory):
    def __init__(self):
        super(ContactsBook, self).__init__()
    
    def store_record(self, contact_id, contact_details: str):
        """
        Stores a record in the dictionary. In case of a repeating contact_id, the 'contact_details' value is appended
        to the existing contact details.
        """
        contact_id = self.parse_contact_id(contact_id)
        
        # with open(f"{contact_id}", 'x') as f:
        #     f.write(f"{contact_details}\n")
        #     fd = os.open(f"{contact_id}", os.O_RDWR)
        #     os.fsync(fd)

        if contact_id not in self.directory.keys():
            self.directory[contact_id] = []
        if contact_details not in self.directory[contact_id]:
            self.directory[contact_id].append(contact_details)
    
    def retrieve_record(self, contact_id):
        contact_id = self.parse_contact_id(contact_id)
        return self.directory.get(contact_id, "No such record found. Try again.\n")
    
    def delete_record(self, contact_id):
        contact_id = self.parse_contact_id(contact_id)
        return self.directory.pop(contact_id, "No such record found. Try again.\n")
    
    def list_records(self):
        records = ""
        for key, value in self.directory.items():
            records += f"{key} --> {', '.join(map(str, value))}\n"
    
        return records if records else "No records.\n"
    
    @staticmethod
    def parse_contact_id(contact_id):
        try:
            # Integer ID case
            contact_id = int(contact_id)
        except ValueError:
            # String ID case
            contact_id = str(contact_id)
        return contact_id


def help_menu():
    print(">List of commands you can use:\n" +
          "1. store <KEY> <VALUE> (to store contact details)\n" +
          "2. retrieve <KEY> (to retrieve contact details based on some key)\n" +
          "3. delete <KEY> (to delete contact details based on some key)\n" +
          "4. list (to list all existing records)\n" +
          "5. exit (to exit the application)\n")


def main():
    print("\n====================== Welcome to the 'Basic Contacts' Application!======================")
    my_contacts_book = ContactsBook()
    help_menu()
    user_input = input(">Enter your command:")
    while user_input.lower() != "exit":
        command = user_input.split()[0].lower()
        if command == 'store':
            try:
                contact_id = user_input.split()[1]
                contact_details = user_input.split()[2]
                my_contacts_book.store_record(contact_id, contact_details)
            except IndexError:
                print(">Missing <KEY> and/or <VALUE>. Type 'help' to see the list of available commands.\n")
        
        elif command == "retrieve":
            try:
                contact_id = user_input.split()[1]
                print(f">Retrieved contact details: {my_contacts_book.retrieve_record(contact_id)}")
            except IndexError:
                print(">Missing <KEY>. Type 'help' to see the list of available commands.\n")
        
        elif command == "delete":
            try:
                contact_id = user_input.split()[1]
                print(f">Deleted contact details: {my_contacts_book.delete_record(contact_id)}")
            except IndexError:
                print(">Missing <KEY>. Type 'help' to see the list of available commands.\n")
        
        elif command == "list":
            print(f"{my_contacts_book.list_records()}")
        
        elif command == "help":
            help_menu()
        
        else:
            print(">Invalid command. Type 'help' to see the list of available commands.\n")
        
        user_input = input(">Enter your command:")


def test():
    my_contacts_book = ContactsBook()
    print(dir(my_contacts_book))


if __name__ == '__main__':
    main()
