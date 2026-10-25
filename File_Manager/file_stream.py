import os


def write_list(filename: str, tasks: list[str]) -> None:
    with open(filename, "w", encoding='utf-8') as file:
        file.write("\n".join(tasks))


def read_list(filename: str) -> list[str]:
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding='utf-8') as files:
        return [line.rstrip("\n") for line in files if line.strip()]
        #print(len(files.readlines()))


def read_users_files(filename: str) -> dict[str,str]:
    result: dict[str, str] = {}
    if not os.path.exists(filename):
        return result

    with open(filename, "r", encoding="utf-8") as file:   
        for line in file:
            line = line.rstrip("\n")
            if ":" not in line:                            
                continue
            user, password = line.split(":", 1)
            result[user.strip()] = password.strip()
    return result


def write_users_files(filename: str, users: dict[str, str]) -> None:
     with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(f"{k}:{v}" for k, v in users.items()))


def add_users_to_files(filename: str, key: str, value: str):
    with open(filename, "a", encoding='utf-8') as file:
        file.write(f"{key}:{value}\n")