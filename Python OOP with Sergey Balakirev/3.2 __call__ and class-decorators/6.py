class HandlerGET:

    def __init__(self, func):
        self.func = func

    def __call__(
        self, request, *args, **kwargs
    ):  # {"method": "GET", "url": "contact.html"}
        m = request.get("method", "GET")
        if m == "GET":
            return self.get(self.func, request)

    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request)}"
