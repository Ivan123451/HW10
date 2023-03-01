
def menu() -> int:
    print('''\nГлавное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать контакты
    4. Добавить контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход''')
    choice = int(input('Выберите пункт меню: '))
    return choice



def show_contacts(phone_book: list[dict]):
    print()
    if phone_book:
        for i, contact in enumerate(phone_book, 1):
            print(f'{i}. {contact.get("name"):<20} '
                  f'{contact.get("phone"):<20}'
                  f'{contact.get("comment"):<20}')
        print()
    else:
        print('\nТелефонная книга пуста или файл не открыт!\n')



def new_contact() -> dict:
    print()
    name = input('Введите имя и фамилию: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    print()
    return {'name': name, 'phone': phone, 'comment': comment}

def change_contact(book: list) -> tuple:
    show_contacts(book)
    choice = int(input('выберете контакт, который вы хотите изменить: '))
    name = input('введите новое имя или Enter оставить без изменией:')
    phone = input('введите новый телефон или Enter оставить без изменией:')
    comment = input('введите новый комментарий или Enter оставить без изменией:')
    return choice - 1, {'name': name if name else book[choice-1].get('name'),
                        'phone': phone if phone else book[choice-1].get('phone'),
                        'comment': comment if comment else book[choice-1].get('comment')}

def select_to_delete(book: list):
    show_contacts(book)
    return int(input('введите номер элемента, который хотите удалить')) -1
def input_requeat(text: str) -> str:
    return input(f'Введите {text}: ')

def goodbye():
    print('Досвидания')

