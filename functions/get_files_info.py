import os


def get_files_info(working_directory, directory="."):
    try:
        absolute_working_directory = os.path.abspath(working_directory)
        relative_path = os.path.join(working_directory, directory)
        absolute_path = os.path.abspath(relative_path)

        if not absolute_path.startswith(absolute_working_directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(absolute_path):
            return f'Error: "{directory}" is not a directory'

        dir_name = "current" if directory == "." else f"'{directory}'"
        file_results = [f"Result for {dir_name} directory"]

        for file in os.listdir(absolute_path):
            file_path = os.path.join(absolute_path, file)
            is_dir = os.path.isdir(file_path)
            file_size = os.path.getsize(file_path)
            file_results.append(
                f"- {file}: file_size={file_size} bytes, is_dir={is_dir}"
            )

        return "\n".join(file_results)
    except Exception as e:
        return f"Error: {e}"
