class Contact:
    def __init__(self, name, phone_number, contact_id):
        self.name = name
        self.phone = phone_number
        self.id = contact_id

    @classmethod
    def validate_phone_number(cls, phone_number):
        if phone_number.isdigit() and len(phone_number) == 10:
            return True
        else:
            return False

class ContactList:
    all_contacts = []
    last_id = 0

    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            cls.last_id = cls.last_id + 1
            contact = Contact(name, phone_number, cls.last_id)
            cls.all_contacts.append(contact)
        else:
            print("Error: номер должен содержать 10 цифр")

    @classmethod
    def remove_contact(cls, contact_id):
        for contact in cls.all_contacts:
            if contact.id == contact_id:
                cls.all_contacts.remove(contact)

print(ContactList.all_contacts)

ContactList.add_contact("Вася Пупкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")
ContactList.add_contact("John Doe", "5551234")   # ошибка

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone, contact.id)

print(ContactList.last_id)

ContactList.remove_contact(1)

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone, contact.id)