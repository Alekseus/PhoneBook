def search():
    print('Укажите по какому параметру будет осуществляться поиск: \n\
        1 - Фамилия;\n\
        2 - Имя;\n\
        3 - Номер телефона;\n\
        4 - Описание.\n')
    a = int(input('Ваш выбор: '))
    if a == 1:
        entry = input('Введите Фамилию: ').title()
    if a == 2:
        entry = input('Введите Имя: ').title()
    if a == 3:
        entry = input('Введите номер телефона: ')
    if a == 4:
        entry = input('Введите описание контакта (личный, рабочий, домашний и т.д.): ').title()

    print('Поиск будет осуществляться по : ', entry)
    return entry