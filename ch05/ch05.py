from utils.files import readfile
import re

alphanumeric: str = r"^[a-zA-Z0-9]+$"
number: str = r"[0-9]+"
mail: str = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.com$"
letters: str = r"[a-zA-Z]+"


def solve() -> None:
    lines: list = readfile("ch05/input.txt")
    invalid: list = []
    for line in lines:
        line = line.strip()
        id, username, email, age, location = line.split(",")
        if not (
            re.match(alphanumeric, id)
            and re.match(alphanumeric, username)
            and re.match(mail, email)
            and (re.match(number, age) or age == "")
            and (re.match(letters, location) or location == "")
        ):
            print(
                f"id={id} username={username} email={email} age={age} location={location}"
            )
            invalid.append(username[0])
            print(invalid)
            print(line)

    print("".join(invalid))
