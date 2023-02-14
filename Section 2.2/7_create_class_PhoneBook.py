class PhoneBook:
    def __init__(self):
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, index):
        del self.phones[index]

    def get_phone_list(self):
        return self.phones[:]


class PhoneNumber:
    def __init__(self, number, fio):
        self.number = number
        self.fio = fio


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
print(phones)