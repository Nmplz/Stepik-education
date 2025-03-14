class Data:
    def __init__(self, data, ip_destination):
        self.data = data
        self.ip = ip_destination


class Router:
    def __init__(self):
        self.buffer = []
        self.list_of_servers = []

    def link(self, server):
        if isinstance(server, Server) and server not in self.list_of_servers:
            self.list_of_servers.append(server)
            server.router = self

    def unlink(self, server):
        if isinstance(server, Server) and server in self.list_of_servers:
            self.list_of_servers.remove(server)
            server.router = None

    def send_data(self):
        for i in self.buffer:
            for s in self.list_of_servers:
                if i.ip == s.ip:
                    s.buffer.append(i)
        self.buffer.clear()


class Server:
    server_ip = 1

    def __init__(self, ip=None, router=None):
        if not ip:
            self.ip = Server.server_ip
            Server.server_ip += 1
        self.router = router
        self.buffer = []

    def send_data(self, data):
        if not self.router:
            raise AttributeError("Нет роутера, нельзя отправить пакет")
        else:
            self.router.buffer.append(data)

    def get_data(self):
        data_to_send = self.buffer.copy()
        self.buffer.clear()
        return data_to_send

    def get_ip(self):
        return self.ip
