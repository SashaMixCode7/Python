from file_stream import write_list, read_list
from todo_list2 import todo_process
from user import get_user

File_task = "names.txt"
USER_FILE = "users.txt"


def main() -> None:
    #file_path = "C:\\Users\\User\\Documents\\file.txt"
    task = read_list(File_task)

    user = get_user(USER_FILE)
    print(f"Здравствуйте, {user}!")
    try:
        todo_process(task)
    finally:
        write_list(File_task, task)


if __name__ == "__main__":
    main()
