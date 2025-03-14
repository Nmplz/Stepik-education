class Viber:
    message_list = []

    @classmethod
    def add_message(cls, msg):
        if isinstance(msg, Message):
            cls.message_list.append(msg)

    @classmethod
    def remove_message(cls, msg):
        cls.message_list.remove(msg)

    @staticmethod
    def set_like(msg):
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls, digit):
        for i in range(digit, 1, -1):
            print(cls.message_list[i].text)

    @classmethod
    def total_messages(cls):
        return len(cls.message_list)


class Message:

    def __init__(self, text):
        self.text = text
        self.fl_like = False
