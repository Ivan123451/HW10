
def menu():
    print('''\nГлавное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать контакты
    4. Создать контакт
    5. Изменить контакт
    6. Найти контакт
    7. Удалить контакт
    8. Выход''')
    while True:
        try:
            choice = int(input('Выберите пункт меню: '))
            if 0 < choice < 9:
                return choice
            else:
                print('Введите число от 1 до 8')
        except:
            print('Вводи цифрами, а не буквами!')


def show_contacts(pb: list[dict]):
    if pb == []:
        print('Телефонная книга пуста или файл не открыт!')
    else:
        for i, contact in enumerate(pb, 1):
            name = contact.get('name')
            phone = contact.get('phone')
            comment = contact.get('comment')
            print(f'{i}. {name:20} {phone:<15} {comment:<20}')

def new_contact_input():
    name = input('Введите имя и фамилию: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    new_contact = {'name': name,
                   'phone': phone,
                   'comment': comment}
    return new_contact

def find_contact():
    find = input('Введите искомый элемент: ')
    return find

def input_id():
    ind = int(input('Введите индекс: '))
    return ind

def confirm(condition: str, name: str):
    answer = input(f'Вы действительно хотите {condition} контакт {name}? (y/n)')
    if answer == 'y':
        return True
    else:
        return False


def confirm_changes():
    answer = input('У вас есть несохраненные изменения, хотите их сохранить? (y/n)')
    return True if answer == 'y' else False
