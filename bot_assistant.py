def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError as e:
            return f"Name not found"
        except ValueError as e:
            return f"Name and phone must be provided."
        except IndexError as e:
            return f"Invalid input."
    return inner

#Za pomocą tego polecenia bot zapisuje nowy kontakt w swojej pamięci (w słowniku)
@input_error
def add_func(contacts_book, user_input):
    _, name, phone = user_input.split(" ", 2)
    if name not in contacts_book:
        contacts_book[name] = phone
        return f'Contact added: {name}: {phone}'
    else:
        return f'Contact with name {name} already exists.'

#Za pomocą tego polecenia bot zapisuje nowy numer telefonu istniejącego kontaktu w pamięci.
@input_error
def change_func(contacts_book, user_input):
    _, name, phone = user_input.split(" ", 2)
    if name in contacts_book.keys():
        for i in filter(lambda x: contacts_book[name], contacts_book.items()):
            contacts_book[name] = phone
        return 'The phone number has been changed.'
    else:
        return f'Name {name} not found.'

#To polecenie wyświetla numer telefonu dla określonego kontaktu w konsoli
@input_error
def phone_func(contacts_book, user_input):
    _, name = user_input.split(" ", 1)
    if name in contacts_book.keys():
        for i in filter(lambda x: x[0] == name, contacts_book.items()):
            return i[1]
    else:
        return f'Name {name} not found.'

#To polecenie wyświetla wszystkie zapisane kontakty z numerami telefonów w konsoli.
def show_all_func(contacts_book):
    current_contacts = '\n'.join(map(lambda x: f'{x[0]}: {x[1]}', contacts_book.items()))
    return current_contacts

def main():
    contacts = {}
    
    while True:
        user_input = input("Enter a command: ").strip().lower()

        if user_input == "good bye" or user_input == "close" or user_input == "exit":
            print("Good bye!")
            break

        elif user_input == "hello":
            print('How can I help you?')

        elif user_input.startswith("add "):
            print(add_func(contacts, user_input))

        elif user_input.startswith("change "):          
            print(change_func(contacts, user_input))

        elif user_input.startswith("phone "):
            print(phone_func(contacts, user_input))

        elif user_input == "show all":
            print(show_all_func(contacts))

if __name__ == '__main__':

    main()   