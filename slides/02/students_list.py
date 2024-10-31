"""Students list in Python"""
import json
import csv
from typing import List, Dict, Any, Union

FOLDER_PATH = "C:/Users/u138478/Documents/programming_lecture/python_101_for_economists"

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

def write_json(file_path: str, data: Dict[str, Any]) -> None:
    """Writes a dictionary to a JSON file."""
    with open(file_path, mode='w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

students_json_data = read_json_file(file_path=f"{FOLDER_PATH}/slides/02/files/courseid_77298_participants.json")

students_list_in_english: List[Dict[str, Union[str, int]]] = []
for student_data in students_json_data:
    student_data_dictionary: Dict[str, Union[str, int]] = {
        "name": str(student_data["nom"].title()),
        "last_name": str(student_data["cognoms"].title()),
        "student_id": int(student_data["nmeroid"].replace("u", ""))
    }
    students_list_in_english.append(student_data_dictionary)


write_csv(
    list_of_dictionaries=students_list_in_english,
    file_path = f"{FOLDER_PATH}/slides/02/files/courseid_77298_participants_english_version.csv"
)
