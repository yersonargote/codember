"""
** Input Examples: **
Input: "##*&"
Expected Output: "4"
Explanation: Increment (1), increment (2), multiply (4), print (4).

Input: "&##&*&@&"
Expected Output: "0243"
Explanation: Print (0), increment (1), increment (2), print (2), multiply (4), print (4), decrement (3), print (3).
"""


from collections.abc import Callable

from utils.files import readfile

operations: dict[str, Callable] = {
    "#": lambda x: x + 1,
    "@": lambda x: x - 1,
    "*": lambda x: x * x,
    "&": lambda x: print(x, end="") or x,
}


def solve() -> None:
    message: str = readfile("./ch02/message_02.txt")
    message = message.lower().strip()

    acum: int = 0
    result: str = ""

    for letter in message:
        operation = operations[letter]
        acum = operation(acum)
    print(result)
