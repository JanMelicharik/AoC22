import re

from copy import deepcopy
from typing import Iterable, Tuple


def get_starting_columns(initial_setup: str) -> dict[str, str]:
    first_line = initial_setup.split("\n")[0]
    line_length = len(first_line)
    number_of_steps = len(first_line[1::4])

    columns = []

    for letter_index in range(number_of_steps):
        columns.append(initial_setup[(letter_index * 4) + 1::line_length + 1])

    return {stack[-1]: stack[:-1].strip() for stack in columns}


def rearrange_stack(instructions: Iterable[Tuple[int, str, str]], stacks: dict[str, str], new_model: bool) -> dict[str, str]:
    for instruction in instructions:
        count = instruction[0]
        from_label = instruction[1]
        to_label = instruction[2]

        from_column = stacks[from_label]
        to_column = stacks[to_label]

        manipulation = from_column[:count]
        from_column = from_column[count:]

        if new_model:
            to_column = manipulation + to_column
        else:
            to_column = manipulation[::-1] + to_column

        stacks[to_label] = to_column
        stacks[from_label] = from_column

    return stacks


def parse_movement_info(movement: str) -> (int, int, int):
    match = re.match(r"^move (?P<count>\d+) from (?P<from>\d) to (?P<to>\d)$", movement)
    return int(match.group("count")), match.group("from"), match.group("to")


def get_top_boxes(stack: dict[str, str]) -> str:
    return "".join(column[0] for column in stack.values())


def main():
    with open("input.txt", "r") as infile:
        initial_setup, moves = infile.read().split("\n\n")

    original_columns = get_starting_columns(initial_setup)

    instructions = list(map(parse_movement_info, moves.strip().split("\n")))
    # Part 1 - GFTNRBZPF
    columns_1 = rearrange_stack(instructions, deepcopy(original_columns), new_model=False)

    # Part 2 - VRQWPDSGP
    columns_2 = rearrange_stack(instructions, deepcopy(original_columns), new_model=True)

    print(get_top_boxes(columns_1))
    print(get_top_boxes(columns_2))


if __name__ == "__main__":
    main()
