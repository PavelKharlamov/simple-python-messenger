"""
Пример программы для работы с функциями

Сделать
- функцию hello, которая выводит текст приветствия клиенту
"""


def hello(user):
    print(f"Hello, {user}")


clients = ['John', 'David', 'Kate', 'Alex']

for user in clients:
    hello(user)

new_user = 'Arthur'
clients.append(new_user)
hello(new_user)
