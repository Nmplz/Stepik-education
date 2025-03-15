class GenericView:
    def __init__(self, methods=("GET",)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):

    def render_request(self, request, method):
        if method.upper() not in self.methods:
            raise TypeError("данный запрос не может быть выполнен")
        return getattr(self, method.lower())(request)

    def get(self, request):
        if not type(request) == dict:
            raise TypeError("request не является словарем")
        if not "url" in request:
            raise TypeError("request не содержит обязательного ключа url")
        return f"url: {request['url']}"
