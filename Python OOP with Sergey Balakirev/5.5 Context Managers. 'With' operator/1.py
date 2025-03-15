# здесь объявляйте класс PrimaryKey
class PrimaryKey:

    def __enter__(self):
        print(f"вход")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{exc_type}")
        return True


with PrimaryKey() as pk:
    raise ValueError
