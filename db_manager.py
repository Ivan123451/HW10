from copy import deepcopy

phone_book = []
new_phone_book = []
path = 'phone_db.txt'


def open_file():
    global phone_book
    global new_phone_book
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for contact in data:
            new = contact.strip().split(';')
            new_contact = {}
            new_contact['name'] = new[0]
            new_contact['phone'] = new[1]
            new_contact['comment'] = new[2]
            phone_book.append(new_contact)
    new_phone_book = deepcopy(phone_book)

def save_file():
    global phone_book
    global path
    data = []
    for contact in phone_book:
        data.append(';'.join(contact.values()))
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)


def get():
    global phone_book
    return phone_book

def add(new_contact: dict):
    global phone_book
    phone_book.append(new_contact)

def find(find_option: str):
    global phone_book
    all_find = []
    for contact in phone_book:
        for element in contact.values():
            if find_option.lower() in element.lower():
                all_find.append(contact)
    return all_find

def change_contact(ind: int, contact: dict):
    global phone_book
    phone_book.pop(ind-1)
    phone_book.insert(ind-1, contact)

def delete_contact(ind: int):
    global phone_book
    phone_book.pop(ind -1)

def get_name(ind: int):
    global phone_book
    return phone_book[ind-1].get('name')


def check_changes():
    global phone_book
    global new_phone_book
    if phone_book != new_phone_book:
        return True
    return False
