phone_book: list[dict[str,str]] = []
path = 'phone.txt'

def open_pb():
    global phone_book, path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(':')
        phone_book.append({'id': contact[0], 'name': contact[1], 'phone': contact[2], 'comment': contact[3]})
        

def save_pb():
    global phone_book,path
    data = []
    for contact in phone_book:
        contact = ':'.join([value for value in contact.values()])
        data.append(contact)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(data))

def get_pb() -> list[dict[str,str]]:
    global phone_book
    return phone_book
    
def load():
    return phone_book

def add_contact(contact: dict[str,str]):
    global phone_book
    phone_book.append(contact)
    return contact.get('name')

def search(word: str) -> list[dict[str, str]]:
    res: list[dict[str, str]] = []
    for contact in phone_book:
        for field in contact.values():
            if word.lower() in field.lower():
                res.append(contact)
                break
    return res


def change(contact: dict, index: int | str) -> str:
    for contact in phone_book:
        if index == contact.get('id'):
            contact['name'] = contact.get('name', contact.get('name'))
            contact['phone'] = contact.get('phone', contact.get('phone'))
            contact['comment'] = contact.get('comment', contact.get('comment'))
            return contact.get('name')

def del_contact(index: int):
    return phone_book.pop(index-1).get('name')


