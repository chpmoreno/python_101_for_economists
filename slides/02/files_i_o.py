"""File I/O in Python"""
import json
import csv
from typing import List, Dict, Any

FOLDER_PATH = "/Users/jose.moreno/Documents/Other/UPF/python_101_for_economists"

# Open a file
def open_file_flow(file_name: str, mode: str) -> None:
    file = open(
        file=file_name,
        mode=mode,
        encoding="utf-8"
    )
    # Perform read/write operations here
    file.close()  # Always close the file

# Read a file
def read_file_read(file_name: str) -> str:
    with open(
        file=file_name,
        mode='r',
        encoding="utf-8"
    ) as file:
        content = file.read()
    return content

def read_file_readlines(file_name: str) -> List[str]:
    with open(
        file=file_name,
        mode='r',
        encoding="utf-8"
    ) as file:
        content = file.readlines()
    return content

# Write to a file
def write_file(file_name: str, content: List[str]) -> None:
    with open(
        file=file_name,
        mode='w',
        encoding="utf-8"
    ) as file:
        file.writelines(content)

# Write examples
def write_hello_world_write() -> None:
    with open(
        file=f"{FOLDER_PATH}/slides/02/files/hello_world_write_output.txt",
        mode="w",
        encoding="utf-8"
    ) as file:
        file.write("Hello, world! Hello again!")

def write_hello_world_writelines() -> None:
    with open(
        file=f"{FOLDER_PATH}/slides/02/files/hello_world_writelines_output.txt",
        mode="w",
        encoding="utf-8"
    ) as file:
        file.writelines(["Hello\n", "World\n", "Hello again!"])

write_hello_world_write()
write_hello_world_writelines()

read_hello_world_write = read_file_read(f"{FOLDER_PATH}/slides/02/files/hello_world_write_output.txt")
print(read_hello_world_write)

read_hello_world_writelines = read_file_readlines(f"{FOLDER_PATH}/slides/02/files/hello_world_writelines_output.txt")
print(read_hello_world_writelines)

read_hello_world_write = read_file_readlines(f"{FOLDER_PATH}/slides/02/files/hello_world_write_output.txt")
print(read_hello_world_write)

read_hello_world_write = read_file_read(f"{FOLDER_PATH}/slides/02/files/hello_world_writelines_output.txt")
print(read_hello_world_write)

# Read files
def read_csv_file(file_path: str) -> List[Dict[str, Any]]:
    data: List[Dict[str, Any]] = []
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                data.append(dict(row))
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    return data

def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    data: List[Dict[str, Any]] = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    return data

students = read_csv_file(file_path=f"{FOLDER_PATH}/slides/02/files/courseid_77298_participants.csv")
print(students)

# Save to CSV
def write_csv(
        list_of_dictionaries: List[Dict[str, Any]],
        file_path: str
    ) -> None:
    fieldnames = list_of_dictionaries[0].keys()
    with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(list_of_dictionaries)

students_json_data = read_json_file(file_path=f"{FOLDER_PATH}/slides/02/files/courseid_77298_participants.json")

write_csv(
    list_of_dictionaries=students_json_data,
    file_path = f"{FOLDER_PATH}/slides/02/files/courseid_77298_participants_2.csv"
)

def write_json(file_path: str, data: Dict[str, Any]) -> None:
    """Writes a dictionary to a JSON file."""
    with open(file_path, mode='w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
