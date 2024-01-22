import json

contacts_file = "contacts.txt"
contacts = []

def load_contacts_from_file():
    global contacts
    try:
        with open(contacts_file, 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        pass


def Save_contacts():
    with open(contacts_file, 'w') as file:
        json.dump(contacts, file, indent=2)


def Add_contact():
    print("\nAdd Contact You Want---->\n")
    name = input("Enter Name: ").capitalize()
    phone = input("Enter Phone Number: ")
    while not(phone.isdigit()):
        phone=input("\nInvalid Input! Please Enter a Valid Phone Number.")
    email = input("Enter Email Address: ")
    address=input("Enter address: ")
    contact = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Address":address
    }
    contacts.append(contact)
    Save_contacts()
    print("\nContact added successfully!\n")


def View_contact_list():
    if len(contacts) > 0:
        print("\n\tCONTACT LIST:\n")
        print("S.NO")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. \tName:{contact['Name']}\tPhone NO:{contact['Phone']}\n")
    else:
        print("\nNo Contacts Added Yet.\n")

def Search_contact():
    query = input("Enter Name to search: ").capitalize()
    results = []

    for contact in contacts:
        if query == contact['Name'] :
            results.append(contact)

    if results:
        print("\nSearch Results:")
        for result in results:
            print(result)
        print()
    else:
        print("\nNo matching contacts found.\n")


def Update_contact():
    View_contact_list()
    while True:
        try:
            index = int(input("Enter the S.NO: to update the contact: ")) - 1
            break
        except:
            print("\nInvalid Input! Please enter a number.")
        

    if 0 <= index < len(contacts):
        contact = contacts[index]
        print("\nUpdate Contact:")
        contact["Name"] = input(f"New Name ({contact['Name']}): ").capitalize()
        contact["Phone"] = input(f"New Phone ({contact['Phone']}): ") 
        contact["Email"] = input(f"New Email ({contact['Email']}): ") 
        contact["Address"] = input(f"New Address ({contact['Address']}): ")
        Save_contacts()
        print("\nContact updated successfully!\n")
        print(contact)
    else:
        print("\nInvalid S.NO .\n")


def Delete_contact():
    View_contact_list()
    index = int(input("Enter the S.NO: to delete the contact: ")) - 1

    if 0 <= index < len(contacts):
        permission=input(f"\nConfirm you want to delete {index+1} S.NO: (y/n) ").lower()
        if permission=='y':
            del contacts[index]
            Save_contacts()
            print("\nContact deleted successfully!\n")
        else:
            print('\nDeletion cancelled by user')
    else:
        print("\nInvalid contact number.\n")


def main():
    load_contacts_from_file()

    while True:
        print('''Methods Performs on Contact Book---->\n
        1. Add Contact
        2. View Contact List
        3. Search Contact
        4. Update Contact
        5. Delete Contact''')
        
        while True:
            try:
                choice = int(input("\nChoose one option given above Press(1-5) and 0 for Exit : "))
                if choice < 0 or choice > 5:
                    print("\nPlease enter a number between 1 and 5.\n")
                    choice = int(input("\nChoose one option given above Press(1-5) and 0 for Exit : "))
                elif 0<=choice<=5:
                    break
            except:
                print("\nPlease enter a valid integer.")

        if choice == 1:
            Add_contact()
        elif choice == 2:
            View_contact_list()
        elif choice == 3:
            Search_contact()
        elif choice == 4:
            Update_contact()
        elif choice == 5:
            Delete_contact()
        elif choice==0:
            print("\nExiting....")
            break
        input("Press any key to continue...")
        


if __name__ == "__main__":
    print("\n------------>CONTACT BOOK<-----------\n")
    main()
