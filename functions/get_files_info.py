import os


def get_files_info(working_directory, directory="."):
    root_directory = "/home/alkistz/dev/bootdev/ai-agent"
    absolut_working_directory = os.path.join(root_directory, working_directory)
    relative_path = os.path.join(working_directory, directory)
    absolut_path = os.path.abspath(relative_path)

    if not absolut_path.startswith(absolut_working_directory):
        print("Outside of boundries")
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(absolut_path):
        print("Not a directory")
        return f'Error: "{directory}" is not a directory'

    dir_contents = os.listdir(absolut_path)
    print(os.path.isdir(absolut_path))

    print(relative_path)
    print(absolut_path)
    print(dir_contents)


get_files_info("calculator", ".")
