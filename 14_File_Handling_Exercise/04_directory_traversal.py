import os


def save_extensions(dir_name, first_level=False):
    for file_name in os.listdir(dir_name):
        file = os.path.join(dir_name, file_name)

        if os.path.isfile(file):
            extension = file_name.split(".")[-1]
            extensions[extension] = extensions.get(extension, []) + [file_name]
        elif os.path.isdir(file) and not first_level:
            save_extensions(file, first_level=True)


initial_directory = input("Enter a directory: ")
extensions = {}
report_info = []
report_info_path = os.path.join("report.txt")

try:
    save_extensions(initial_directory)
except FileNotFoundError:
    print("Directory not found!")

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    report_info.append(f".{extension}")

    for file in sorted(files):
        report_info.append(f"- - - {file}")

with open(report_info_path, "w") as report_file:
    report_file.write('\n'.join(report_info))
