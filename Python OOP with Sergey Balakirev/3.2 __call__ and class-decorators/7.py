class Handler:

    def __init__(self, methods=("GET",)):
        self.methods = methods

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            m = request.get("method", "GET")
            if m in self.methods:
                if m in self.methods:
                    return self.__getattribute__(m.lower())(func, request)

        return wrapper

    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request)}"

    def post(self, func, request, *args, **kwargs):
        return f"POST: {func(request)}"
