def readfile(path: str) -> str:
    lines: list = []
    with open(path, "r") as file:
        lines = file.readlines()
    return lines


def writefile(path: str, content: str) -> None:
    with open(path, "w") as file:
        file.write(content)
