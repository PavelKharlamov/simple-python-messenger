"""
Клиентское приложение с интерфейсом
"""
import asyncio
from asyncio import transports
from PySide2.QtWidgets import QMainWindow, QApplication
from asyncqt import QEventLoop
from app.interface import Ui_Messenger


class ClientProtocol(asyncio.Protocol):
    transport: transports.Transport
    window: 'Chat'

    def __init__(self, chat):
        self.window = chat

    def data_received(self, data: bytes):
        print(data)
        decoded = data.decode()
        self.window.plainTextEdit.appendPlainText(decoded)

    def connection_made(self, transport: transports.Transport):
        self.window.plainTextEdit.appendPlainText("You have successfully connected.\n"
                                                  "Enter login: <YOUR_LOGIN>")
        self.transport = transport

    def connection_lost(self, exception):
        self.window.plainTextEdit.appendPlainText("You are disconnected from the server")


class Chat(QMainWindow, Ui_Messenger):
    protocol: ClientProtocol

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.send_message)

    def send_message(self):
        message = self.lineEdit.text()
        self.lineEdit.clear()
        self.protocol.transport.write(message.encode())

    def create_protocol(self):
        self.protocol = ClientProtocol(self)
        return self.protocol

    async def start(self):
        self.show()
        loop = asyncio.get_running_loop()
        coroutine = loop.create_connection(
            self.create_protocol,
            "127.0.0.1",
            8080
        )

        await asyncio.wait_for(coroutine, 1000)


app = QApplication()
loop = QEventLoop(app)
asyncio.set_event_loop(loop)
window = Chat()

loop.create_task(window.start())
loop.run_forever()
