def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


#adds name and number to the dict contats
def add_contact(args, contacts):
    name, phone = args
    if name == "username" or not phone.isnumeric():
        raise ValueError("Enter real name, or numeric phone number")
    else:
        contacts[name] = str(phone)
        return "Contact added."



#overwrites the phone number to the new one
def change_phone(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = str(new_phone)
        return "Contact changed."
    else:
        raise ValueError("This contact doesn't exist.")



#show the phone for a specific user name
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise ValueError("This contact doesn't exist.")



#shows all numbers in the list
def show_all(contacts):
    phone_numbers = contacts.values()
    str = ("\n".join(phone_numbers))
    return str


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello" or command == "hi":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_phone(args, contacts))
            elif command == "phone":
                print(show_phone(args, contacts))
            elif command == "all":
                print(show_all(contacts))
            else:
                print("Invalid command.")
        except ValueError:
            print("Invalid input. Please try again.")
        except IndexError:
            print("Invalid number of arguments. Please try again.")


if __name__ == "__main__":
    main()
