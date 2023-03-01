import view
import phone_book

pb = phone_book.PhoneBook()

def start():
    while True:
        choice = view.menu()
        match choice:
            case 1:
                pb.open_file()
            case 2:
                pb.save()
            case 3:
                book = pb.get()
                view.show_contacts(book)
            case 4:
                new_entry = view.new_contact()
                pb.new_contact(new_entry)
            case 5:
                word = view.input_requeat('искомое слово')
                result = pb.search(word)
                view.show_contacts(result)

            case 6:
                new_value = view.change_contact(pb.get())
                pb.change(*new_value)
            case 7:
                index = view.select_to_delete(pb.get())
                name = pb.get_name(index+1)
                if view.confirm('удалить', name):
                    pb.delete(index)
            case 8:
                if pb.check_changes():
                    if view.confirm_changes():
                        pb.save()
                        print('Изменеия успешно сохранены')
                view.goodbye()
                break

