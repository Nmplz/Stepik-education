class FileAcceptor:
    def __init__(self, *args):
        self.extentions = args

    def __call__(self, filenames):
        return filenames.endswith(self.extentions)

    def __add__(self, other):
        return FileAcceptor(*set(self.extentions + other.extentions))
