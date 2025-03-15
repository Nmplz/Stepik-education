import sys


class MailBox:
    def __init__(self):
        self.inbox_list = []

    def receive(self):
        lst_in = [
            "sc_lib@list.ru; От Балакирева; Успехов в IT!",
            "mail@list.ru; Выгодное предложение; Вам одобрен кредит.",
            "Python ООП; Балакирев С.М.; 2022",
            "mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.",
        ]
        # lst_in = list(map(str.strip, sys.stdin.readlines()))
        self.inbox_list = [MailItem(*mail.split(";")) for mail in lst_in]


class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, fl_read):
        self.is_read = fl_read

    def __bool__(self):
        return self.is_read


mail = MailBox()
mail.receive()
mail.inbox_list[0].set_read(True)
mail.inbox_list[-1].set_read(True)

inbox_list_filtered = list(filter(bool, mail.inbox_list))
