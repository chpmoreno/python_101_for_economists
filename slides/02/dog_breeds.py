"""Read Dog Breeds file"""
from typing import List

FOLDER_PATH = "/Users/jose.moreno/Documents/Other/UPF/python_101_for_economists"

def read_file_read(file_name: str) -> str:
    """
    Reads a file and returns the content as a string.

    Args:
        file_name: str
            The path to the file to be read.

    Returns:
        str
            The content of the file.

    Raises:
        FileNotFoundError
            If the file does not exist.
    """
    with open(
        file=file_name,
        mode='r',
        encoding="utf-8"
    ) as file:
        content = file.read()
    return content

def read_file_readlines(file_name: str) -> List[str]:
    """
    Reads a file and returns the content as a list of strings, 
    where each string represents a line in the file.

    Args:
        file_name: str
            The path to the file to be read.

    Returns:
        List[str]
            A list of strings, each representing a line in the file.

    Raises:
        FileNotFoundError
            If the file does not exist.
    """
    with open(
        file=file_name,
        mode='r',
        encoding="utf-8"
    ) as file:
        content = file.readlines()
    return content

#content_of_dog_breeds = read_file_read(f"{FOLDER_PATH}/slides/02/files/dog_breeds.txt")
#print(content_of_dog_breeds)

content_of_dog_breeds = read_file_readlines(f"{FOLDER_PATH}/slides/02/files/dog_breeds.txt")

for breed_line in content_of_dog_breeds:
    print(breed_line)
