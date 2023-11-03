"""
** Examples: **
cat dog dog car Cat doG sun -> cat2dog3car1sun1
keys house HOUSE house keys -> keys2house3
cup te a cup -> cup2te1a1
houses house housess -> houses1house1housess1
"""


from utils.files import readfile

counter_words: dict[str, int] = {}


def solve() -> None:
    message: str = readfile("./ch01/message_01.txt")
    message = message.lower().strip()

    words: list = message.split(" ")

    for word in words:
        try:
            counter_words[word] += 1
        except:
            counter_words[word] = 1

    result: str = ""
    for key, value in counter_words.items():
        result += f"{key}{value}"

    print(result)
