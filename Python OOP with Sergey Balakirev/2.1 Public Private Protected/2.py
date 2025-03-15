class Money:
    def __init__(self, money=0):
        if isinstance(money, int):
            self.__money = money

    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money

    def __check_money(self, money):
        if money >= 0 and isinstance(money, int):
            return True
        return False

    def get_money(self):
        return self.__money

    def add_money(self, money):
        self.__money += money.__money
