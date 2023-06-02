import text
import view
import model

def start():
    
    while True:
        choice = view.main_menu()

        match choice:
            case 1:
                model.open_pb()
                view.print_message(text.load_successful)
            case 2:
                model.save_pb()
                view.print_message(text.save_successful)
            case 3:
                pb = model.load()
                view.print_contacts(pb, text.pb_empty)
            case 4:
                contact = view.input_contact(text.input_new_contact)
                name = model.add_contact(contact)
                view.print_message(text.new_contact_successful(name))
            case 5:
                key_word = view.input_search(text.input_search)
                res = model.search(key_word)
                view.print_contacts(res, text.empty_search(key_word))
            case 6:
                key_word = view.input_search(text.input_change)
                res = model.search(key_word)
                if res:
                    if len(res) != 1:
                        view.print_contacts(res, '')
                        current_id = view.input_search(text.input_index)
                    else:
                        current_id = res[0].get('id')
                    new_contact = view.input_contact(text.change_contact)
                    name = model.change(new_contact, current_id)
                    view.print_message(text.change_successful(name))
                else:
                    view.print_message(text.empty_search(key_word))
            case 7:
                pb = model.get_pb()
                index = view.input_index(text.index_del_contact, pb, text.pb_empty)
                name = model.del_contact(index)
                view.print_message(text.del_contact(name))
            case 8:
                break