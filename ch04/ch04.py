from utils.files import readfile

reals: list[str] = []


def solve() -> None:
    lines: list = readfile("ch04/input.txt")

    for line in lines:
        line = line.strip()
        alpha, checksum = line.split("-")
        real: bool = check(alpha, checksum)
        if real:
            reals.append(checksum)
    print(reals[32])


def check(alpha: str, checksum: str) -> bool:
    counter: dict[str, int] = {}
    for letter in alpha:
        try:
            counter[letter] += 1
        except KeyError:
            counter[letter] = 1
    result: str = ""
    for key, value in counter.items():
        if value == 1:
            result += key
    return result == checksum
