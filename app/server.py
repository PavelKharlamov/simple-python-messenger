"""
Серверное приложение для соединений
"""
import asyncio
from asyncio import transports
from typing import Optional


class ClientProtocol(asyncio.Protocol):
    login: str
    server: 'Server'
    transport: transports.Transport

    def __init(self, server: 'Server'):
        self.server = server
        self.login = None

    def data_received(self, data: bytes):
        decoded = data.decode()
        print(decoded)

        if self.login is None:
            # login:User
            if decoded.startswith("login:"):
                self.login = decoded.replace("login:", "").replace("\r\n", "")
                self.transport.write(
                    f"Привет, {self.login}!".encode()
                )
        else:
            self.send_message(decoded)

    def send_message(self, message):
        format_string = f"<{self.login}> {message}"
        encoded = format_string.encode()

        for client in self.server.clients:
            if client.login != self.login:
                client.transport.write(encoded)

    def connection_made(self, transport: transports.BaseTransport):
        self.transport = transport
        self.server.clients.append(self)
        print("Соединение установлено")

    def connection_lost(self, exc):
        self.server.clients.remove(self)
        print("Соединение разорвано")


class Server:
    clients: list

    def __init__(self):
        self.clients = []

    def create_protocol(self):
        return ClientProtocol(self)

    def start(self):
        loop = asyncio.get_running_loop()
        coroutine = loop.create_server(
            self.create_protocol,
            "127.0.0.1",
            8088
        )
        print("Сервер запущен")

        await coroutine.serve_forever()


process = Server()
try:
    asyncio.run(process.start())
except KeyboardInterrupt:
    print("Сервер остановлен вручную")
