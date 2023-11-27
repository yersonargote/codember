from utils.files import readfile


def solve():
    lines: list = readfile("ch03/encryption_policies.txt")
    validation: dict = {}
    order: int = 1
    for line in lines:
        line = line.replace("\n", "")
        ran, letter, value = line.split(" ")
        down, up = ran.split("-")
        letter = letter.replace(":", "")
        up = int(up)
        down = int(down)
        counter: int = letter_counter(value, letter)
        print(
            f"{value} {letter} / {down} <= {counter} <= {up} -> {(down <= counter <= up)} {order}"
        )
        if not (down <= counter <= up):
            validation[order] = value
            order += 1
    print(validation)


def letter_counter(text: str, key: str) -> int:
    counter: int = 0
    for letter in text:
        if key == letter:
            counter += 1
    return counter
