from file_stream import read_users_files, add_users_to_files
from fault import NoMoreAttempts, RefuseCreateNewUser
import hashlib

USERNAME = [
    'admin:superpassword',
    'user:usual:/password2',
    'kulhacker:ku:ef:lpasw0rd',
    'stevieballmer:12345',
    'zippy:pfoejxt09,g2']

def parse_tex_to_dict(username: list[str]) -> dict[str, str]:
    r = {}
    for line in username:
        if ":" in line:
            us, p = line.split(':', 1)
            r[us] = p
    return r

def hashed(md: str) -> str: return hashlib.md5(md.encode()).hexdigest()
def get_user(user_filename: str) -> str:
    users = read_users_files(user_filename)
    us = input("Введите пользователя: ")
    if us in users:
        for i in range(3):
            password = input("Введите пароль:")
            if password == users[us]:
                return us
            else:
                print("Пароль неверен. Еще раз.")
        else:
            raise NoMoreAttempts("Попытки закончились. Прощайте.")

    choice = input(f"Пользователя не существует. Можете создать [Да/Нет]").strip().lower()
    if choice == "Нет":
        raise RefuseCreateNewUser("Прощайте.")
    for i in range(3):
        password = input(f"Введите пароль:")
        password2 = input(f"Еще раз:")
        if password == password2:
            users[us] = password
            add_users_to_files(user_filename, us, password)
            return us
        print(f"пароль не верен.")
    else:
        raise NoMoreAttempts("Попытки закончились. Прощайте.")


