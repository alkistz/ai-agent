import os

MAX_CHARS = 10000


def get_file_content(working_directory, file_path):
    try:
        absolute_working_directory = os.path.abspath(working_directory)
        relative_path = os.path.join(working_directory, file_path)
        absolute_path = os.path.abspath(relative_path)

        if not absolute_path.startswith(absolute_working_directory):
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(absolute_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(absolute_path, "r") as f:
            file_content_string = f.read()
            if len(file_content_string) > MAX_CHARS:
                return (
                    file_content_string[:MAX_CHARS]
                    + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )

            return file_content_string

    except Exception as e:
        return f"Error: {e}"
