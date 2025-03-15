class DigitRetrieve:
    def __call__(self, digit):
        try:
            return int(digit)

        except ValueError:
            return None
