import random

from flask import Flask

server = Flask(__name__)


def heads_or_tails():
    return random.randint(0, 1) == 1


@server.route("/input")
def input_string():
    input_length = 50
    is_correct = heads_or_tails()

    if is_correct:
        # Return a valid input
        open_brackets = ["(", "[", "{"]
        close_brackets = {"(": ")", "[": "]", "{": "}"}
        close_stack = []
        input_list = []
        while len(close_stack) + len(input_list) < input_length:
            if close_stack and heads_or_tails():
                # Close last opened bracket
                new_el = close_stack.pop(-1)
            else:
                # Open a new bracket
                new_el = random.choice(open_brackets)
                close_stack.append(close_brackets[new_el])
            input_list.append(new_el)

        # Close everything
        input_list.extend(close_stack[::-1])
        input_string = "".join(input_list)
    else:
        # Return an invalid input
        alphabet = ["(", ")", "[", "]", "{", "}"]
        input_string = "".join(random.choice(alphabet) for _ in range(input_length))

    return input_string


if __name__ == "__main__":
    server.run(host="0.0.0.0")
