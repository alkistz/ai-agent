import os


def write_file(working_directory, file_path, content):
    try:
        absolute_working_directory = os.path.abspath(working_directory)
        relative_path = os.path.join(working_directory, file_path)
        absolute_path = os.path.abspath(relative_path)

        if not absolute_path.startswith(absolute_working_directory):
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

        os.makedirs(os.path.dirname(absolute_path), exist_ok=True)

        with open(absolute_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"


write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
