import random

from flask import Flask

server = Flask(__name__)


def heads_or_tails():
    return random.randint(0, 1) == 1


def build_valid_string(remaining):
    if remaining == 0:
        return ""

    new_brackets = random.choice(("()", "[]", "{}"))
    if heads_or_tails():
        return f"{new_brackets}{build_valid_string(remaining - 2)}"
    else:
        return f"{new_brackets[0]}{build_valid_string(remaining - 2)}{new_brackets[1]}"


@server.route("/input")
def input_string():
    input_length = 50
    is_correct = heads_or_tails()

    if is_correct:
        # Return a valid input
        input_string = build_valid_string(input_length)
    else:
        # Return an invalid input
        alphabet = "()[]{}"
        input_string = "".join(random.choice(alphabet) for _ in range(input_length))

    return input_string


if __name__ == "__main__":
    server.run(host="0.0.0.0")
