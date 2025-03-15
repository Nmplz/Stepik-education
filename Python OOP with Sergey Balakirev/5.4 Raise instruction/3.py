class DateError(Exception):
    pass


class DateString:
    def __init__(self, date_string):
        self.day, self.month, self.year = self.sep_date(date_string)

    def sep_date(self, date_string):
        day, month, year = date_string.split(".")
        if (
            not 0 < int(day) <= 31
            or not 0 < int(month) <= 12
            or not 0 < int(year) <= 3000
        ):
            raise DateError("Неверный формат даты")
        return int(day), int(month), int(year)

    def __str__(self):
        return f"{self.day:02}.{self.month:02}.{self.year:04}"


date_string = input()
try:
    date = DateString(date_string)
    print(date)
except DateError as d:
    print(d)
