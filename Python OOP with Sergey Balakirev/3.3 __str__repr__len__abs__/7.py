import time


class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        res = self.clock1.get_time() - self.clock2.get_time()
        if res < 0:
            return "00: 00: 00"
        r_hours = self.clock1.hours - self.clock2.hours
        r_minutes = self.clock1.minutes - self.clock2.minutes
        r_seconds = self.clock1.seconds - self.clock2.seconds
        return f"{r_hours:02}: {r_minutes:02}: {r_seconds:02}"

    def __len__(self):
        res = self.clock1.get_time() - self.clock2.get_time()
        return res if res > 0 else "00: 00: 00"


class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds
