class SoftList(list):
    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except:
            return False
