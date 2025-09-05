import os
import subprocess


def run_python_file(working_directory: str, file_path: str, args: list = []):
    try:
        absolute_working_directory = os.path.abspath(working_directory)
        relative_path = os.path.join(working_directory, file_path)
        absolute_path = os.path.abspath(relative_path)

        if not absolute_path.startswith(absolute_working_directory):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(absolute_path):
            return f'Error: File "{file_path}" not found.'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        print(absolute_path)
        result = subprocess.run(
            ["python", absolute_path, *args], timeout=30, capture_output=True, text=True
        )

        formatted_results = [
            f"STDOUT: {result.stdout}",
            f"STDERR: {result.stderr}",
        ]

        if result.returncode != 0:
            formatted_results.append(f"Process exited with code{result.returncode}")

        if result.stdout is None:
            formatted_results.append("No output produced.")

        return "\n".join(formatted_results)
    except Exception as e:
        return f"Error: executing Python file: {e}"


print(run_python_file("calculator", "main.py", ["3 + 5"]))
