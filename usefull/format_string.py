
name = 'Semen'
mid_name = 'Semenovich'
last_name = 'Gorbumkov'
balance = 1256.76



if __name__ == '__main__':

    # Позиционный Формат
    text_pos = """
Дорогой, {2} {0} {1}. 
Баланс Вашего счета {3} руб. 
{0}, благодарим Вас за пользование нашими услугами""".format(name, mid_name, last_name, balance)

    text_names = """
Дорогой, {lastn} {n} {midn}. 
Баланс Вашего счета {b} руб. 
{n}, благодарим Вас за пользование нашими услугами""".format(n=name, midn=mid_name, lastn=last_name, b=balance)

    print(text_pos)
    print(text_names)