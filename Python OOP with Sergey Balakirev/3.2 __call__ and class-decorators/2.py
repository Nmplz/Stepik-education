class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, filename):
        return filename.split(".")[-1] in self.extensions
