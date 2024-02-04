#  Дополнить телефонный справочник возможностью изменения и удаления данных.
#  Пользователь также может ввести имя или фамилию, и Вы должны реализовать
#  функционал для изменения и удаления данных


def correct_input() -> int:
    is_correct = True
    while is_correct:
        a = input()
        try:
            a = int(a)
            if a >= 0 and a < 7:
                is_correct = False
                return a
            else:
                print(
                    'Ошибка ввода. Пожалуйста, введите цифры в диапазоне [0 ; 6] !')
        except ValueError:
            print('Input error')


def help_menu():
    print("\nДобро пожаловать в Phone Git программу!\n")
    print("0 -> Выход из программы")
    print("1 -> просмотреть все данные телефонной книги")
    print("2 -> добавить новую запись")
    print("3 -> найти определенные данные пользователя")
    print("4 -> редактировать данные")
    print("5 -> удалить данные")
    print("6 -> help menu")


def view_data():
    print("\n PHONE BOOK LIST: \n")
    with open("PHONE_BOOK.txt", "r", encoding="utf-8") as file:
        return file.read().replace(";", " ")


def add_data() -> str:
    print("\n___ADD NEW RECORD mode___\n")
    print("Введите новые данные: ")
    with open("PHONE_BOOK.txt", "a", encoding="utf-8") as data:
        data.write(";".join(tuple(input().split())) + "\n")
    return ("Добавлена ​​новая запись")


def find_data(search_data: str) -> str:
    with open("PHONE_BOOK.txt", "r", encoding="utf-8") as file:
        res = []
        for data in file:
           
            if search_data.lower() in data.lower():
                res.append(data.replace(";", " "))
        if len(res) == 0:
            return "Данные не найдены"
    return ("".join(res))


def edit_data(record_to_be_changed: str) -> str:
    temp = ""
    with open("PHONE_BOOK.txt", "r", encoding="utf-8") as file:
        for line in file:
            if record_to_be_changed.lower() in line.lower():
                print(f"Data found -> {line}")
                y = "y"
                print("Верна ли запись: Y/N")
                if input().lower() == y:
                    print("Введите новые данные: ")
                    new_data = tuple(input().split(" "))
                    temp += ";".join(new_data) + "\n"
                else:
                    temp += line
            else:
                temp += line
        with open("PHONE_BOOK.txt", "w", encoding="utf-8") as file:
            file.write(temp)
        return "Запись была изменена"


def delete_data(to_delete: str) -> str:
    temp = ""
    with open("PHONE_BOOK.txt", "r", encoding="utf-8") as file:
        for data in file:
            if to_delete.lower() in data.lower():
                print(f"Data found -> {data}")
                n = "n"
                print("Верна ли запись: Y/N")
                if input().lower() == n:
                    temp += data
            else:
                temp += data
        with open("PHONE_BOOK.txt", "w", encoding="utf-8") as file:
            file.write(temp)
        return "Запись удалена"


help_menu()

while True:
    mode = correct_input()
    if mode == 0:
        break
    elif mode == 1:
        print(view_data())
    elif mode == 2:
        print(add_data())
    elif mode == 3:
        print("\n___SEARCH DATA mode___\n")
        print("Введите данные для поиска: ")
        print(find_data(str(input())))
    elif mode == 4:
        print("\n___EDIT DATA mode___\n")
        print("Введите запись, которую необходимо изменить:\n")
        print(edit_data(str(input())))
    elif mode == 5:
        print("\n___DELETE DATA mode___\n")
        print("Введите необходимые данные для удаления: ")
        print(delete_data(str(input())))
    elif mode == 6:
        help_menu()