from random import randint


class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self):
        pass_range = randint(self.min_length, self.max_length)
        pswrd = ""
        for i in range(pass_range):
            pswrd += self.psw_chars[randint(0, len(self.psw_chars) - 1)]
        return pswrd


rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)
lst_pass = [rnd() for _ in range(3)]
