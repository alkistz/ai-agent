import os


def get_files_info(working_directory, directory="."):
    root_directory = "/home/alkistz/dev/bootdev/ai-agent"
    absolute_working_directory = os.path.join(root_directory, working_directory)
    relative_path = os.path.join(working_directory, directory)
    absolute_path = os.path.abspath(relative_path)

    if not absolute_path.startswith(absolute_working_directory):
        print("Outside of boundries")
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(absolute_path):
        print("Not a directory")
        return f'Error: "{directory}" is not a directory'

    dir_contents = os.listdir(absolute_path)

    print(f"Result for '{directory}' directory")

    for file in dir_contents:
        file_path = os.path.join(absolute_path, file)
        is_dir = os.path.isdir(file_path)
        file_size = os.path.getsize(file_path)
        print(f"- {file}: file_size={file_size} bytes, is_dir={is_dir}")


# get_files_info("calculator", "../")
get_files_info("calculator", ".")
