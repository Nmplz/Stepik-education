class PhoneBook:
    def __init__(self):
        self.phone_book = []

    def add_phone(self, phone):
        self.phone_book.append(phone)

    def remove_phone(self, indx):
        self.phone_book.remove(self.phone_book[indx])

    def get_phone_list(self):
        return self.phone_book


class PhoneNumber:
    def __init__(self, number, fio):
        if isinstance(number, int) and len(str(number)) == 11 and isinstance(fio, str):
            self.number = number
            self.fio = fio
