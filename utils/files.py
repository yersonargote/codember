def readfile(path: str) -> str:
    with open(path) as file:
        lines: list = file.readlines()
    lines_str: str = "".join(lines)
    return lines_str
