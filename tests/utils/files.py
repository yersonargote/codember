import json


def read_file(path: str) -> list:
    _, ext = path.split(".")
    lines: list = []
    with open(path, "r") as file:
        if ext == "json":
            lines = json.load(file)
        else:
            lines = file.readlines()
    return lines


def write_file(path: str, content: str) -> None:
    with open(path, "w") as file:
        file.write(content)
