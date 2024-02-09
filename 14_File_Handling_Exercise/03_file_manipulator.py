import os

while True:
    command, *args = input().split("-")

    if command == "End":
        break

    file_name = args[0]
    if command == "Create":
        with open(os.path.join("resources", file_name), "w") as f:
            pass

    elif command == "Add":
        content = args[1]
        with open(os.path.join("resources", file_name), "a") as file:
            file.write(f"{content}\n")

    elif command == "Replace":
        old_string = args[1]
        new_string = args[2]
        file_path = os.path.join("resources", file_name)
        try:
            with open(file_path, "r+") as f:
                text = f.read()
                text = text.replace(old_string, new_string)

                f.seek(0)
                f.write(text)
                f.truncate()

        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        try:
            os.remove(os.path.join("resources", file_name))
        except FileNotFoundError:
            print("An error occurred")

