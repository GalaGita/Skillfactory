total_price = 0
number_of_tickets = int(input('Сколько билетов хотите приобрести?\t'))
for i in range(1, number_of_tickets + 1):
    visitor_age = int(input(f'Сколько лет посетителю {i}?\t'))
    if visitor_age < 18:
        print(f'Для посетителя {i} билет бесплатный.')
    elif 18 <= visitor_age < 25:
        print(f'Стоимость билета для посетителя {i} - 990 руб.')
        total_price += 990
    else:
        print(f'Стоимость билета для посетителя {i} - 1390 руб.')
        total_price += 1390
if number_of_tickets > 3:
    print(f'Вы приобретаете больше трех билетов и получаете скидку 10%. Сумма скидки - {int(total_price * 0.1)} руб.')
    total_price = int(total_price - total_price * 0.1)
print(f'Сумма к оплате - {total_price} руб.')