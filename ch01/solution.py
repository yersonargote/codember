"""
** Examples: **
cat dog dog car Cat doG sun -> cat2dog3car1sun1
keys house HOUSE house keys -> keys2house3
cup te a cup -> cup2te1a1
houses house housess -> houses1house1housess1
"""
from collections import Counter


def solve(words: list) -> str:
    counter_words: Counter = Counter(words)

    result: str = ""
    for key, value in counter_words.items():
        result += f"{key}{value}"

    return result
