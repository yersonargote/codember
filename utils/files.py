def readfile(path: str) -> str:
    with open(path, "r") as file:
        lines: list = file.readlines()
    lines_str: str = "".join(lines)
    return lines_str


def writefile(path: str, content: str) -> None:
    with open(path, "w") as file:
        file.write(content)
