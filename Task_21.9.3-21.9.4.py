class Clients:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'''"{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб."'''

    def get_guest(self):
        return f'{self.name} {self.surname}, {self.city}'

client_1 = Clients('Иван', 'Петров', 'Москва', 50)

print(client_1)

client_2 = Clients('Пётр', 'Иванов', 'Волгоград', 170)
client_3 = Clients('Ольга', 'Орлова', 'Омск', 284)
client_4 = Clients('Мария', 'Мухина', 'Пермь', 65)

guest_list = [client_1, client_2, client_3, client_4]

for guest in guest_list:
    print(guest.get_guest())


