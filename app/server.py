"""
Серверное приложение для соединений
"""
import asyncio
from asyncio import transports


class ClientProtocol(asyncio.Protocol):
    login: str
    server: 'Server'
    transport: transports.Transport

    def __init__(self, server: 'Server'):
        self.server = server
        self.login = None

    def data_received(self, data: bytes):
        decoded = data.decode()

        if self.login is None:
            # login:User
            if decoded.startswith("login:"):
                self.login = decoded.replace("login:", "").replace("\r\n", "")

                self.transport.write(
                    f"Hi, {self.login}!".encode()
                )
                self.send_history()
        else:
            self.send_message(decoded)
            print(f"<{self.login}> {decoded}")

    def send_history(self):
        last_messages = self.server.messages[-10:]

        for x in last_messages:
            text = f"\n{x}"
            self.transport.write(text.encode())

    def send_message(self, message):
        format_string = f"<{self.login}> {message}"
        self.server.messages.append(format_string)
        encoded = format_string.encode()

        for client in self.server.clients:
            client.transport.write(encoded)

    def connection_made(self, transport: transports.Transport):
        self.transport = transport
        self.server.clients.append(self)
        print("Connection success")

    def connection_lost(self, exception):
        self.server.clients.remove(self)
        print("Connection lost")


class Server:
    clients: list
    messages: list

    def __init__(self):
        self.clients = []
        self.messages = []

    def create_protocol(self):
        return ClientProtocol(self)

    async def start(self):
        loop = asyncio.get_running_loop()
        coroutine = await loop.create_server(
            self.create_protocol,
            "127.0.0.1",
            8080
        )
        print("Server is started")

        await coroutine.serve_forever()


process = Server()
try:
    asyncio.run(process.start())
except KeyboardInterrupt:
    print("Server stopped manually")
