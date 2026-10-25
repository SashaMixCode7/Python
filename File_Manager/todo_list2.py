# Задача 2024.08.09.04
#
# Настройте чтение списка задач из файла в начале работы программы и сохранение задач в конце работы программы.

#Задача 2024.08.22.04

#Добавьте проверку вводимой даты в вашу программу.
# Задача 2024.08.22.06
#
# Давайте сначала реализуем процедуру проверки нашего пользователя. Наш ли он или нет.
# Есть ли он или нет у нас в базе?
# Задача 2024.08.22.07
#
# Добавьте в работу программы возможность зайти под своим именем, и если такого имени не сохранено, тогда добавить его.
#
# Нужно хранить и имя и пароль.


from file_stream import write_list, read_list
from date_parser import is_date


#TASK = []


def add_task_to_list(task) -> None:
    newtask = input("Новая задача ").strip()
    if not newtask:
        print("Пустая задача — отмена.")
        return
    term = input("ввести срок исполнения (yyyy.m.d):").strip()
    # task1 = newtask + term
    while not is_date(term):
        print("Формат даты не совпадает. Попробуйте снова или оставьте пустым для отмены.")
        term = input("Введите срок исполнения (yyyy.m.d): ").strip()
        if not term:
            print("Задача отменена.")
            return
        task.append(f"Задача: {newtask} | Срок: {term}")
        print(f"Задание '{newtask}' добавлено (срок: {term}).")




def delete_task_from_list(task) -> None:
    if not task:
        print("Список пуст — нечего удалять.")
        return

    print_list_of_tasks(task)
    raw = input("Введите номер для удаления: ").strip()
    try:
        index = int(raw)
    except ValueError:                     
        print("Нужно ввести число.")
        return
    if not 0 <= index < len(task):         
        print("Нет задачи с таким номером.")
        return
    removed = task.pop(index)              
    print(f"Удалено: {removed}")


def print_list_of_tasks(task) -> None:
    if not task:
        print("Список задач пуст.")
        return
    for i, item in enumerate(task):
        print(f"[{i}]: {item}")


# def print_list_of_tasks():
#     for  item in enumerate(TASK):
#         print(f" {item}")


def todo_process(task):
    while True:
        print("Введите 1 Добавить задание\n"
              "введите 2 Удалить задачу\n"
              "Введите 3 Посмотреть список\n"
              "Введите 5 Прочитать файл\n"
              "Введите 6 для выхода")
        n = input("Введите число:").strip()
        if n == "1":
            add_task_to_list(task)
        elif n == "2":
            delete_task_from_list(task)
            # for i, item in enumerate(TASK):
            #     print(f"[{i}]: {item}")
            # index = int(input("Введите номер для удаления: "))
            # TASK.remove(TASK[index])
        elif n == "3":
            print_list_of_tasks(task)
            # for i, item in enumerate(TASK):
            #     print(f"[{i}]: {item}")
        elif n == "5":
            fname = input("Имя файла для чтения: ").strip()
            loaded = read_list(fname)
            if loaded:
                task[:] = loaded          
                print(f"Загружено {len(loaded)} строк(и) из {fname}.")
            else:
                print("Файл пуст или не найден.")
        elif n == "6":
            print("Программа закончена")
            break
        else:
            print("Неверный ввод. ВВедите 1,3,4")




