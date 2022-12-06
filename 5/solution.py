import re

# Top of pile is at the beginning
STACKS = [
    "JZGVTDBN",
    "FPWDMRS",
    "ZSRCV",
    "GHPZJTR",
    "FQZDNJCT",
    "MFSGWPVN",
    "QPBVCG",
    "NPBZ",
    "JPW",
]


def rearrange_stack(instruction: (int, int, int), new_model: bool):
    count = instruction[0]
    from_index = instruction[1] - 1
    to_index = instruction[2] - 1

    from_column = STACKS[from_index]
    to_column = STACKS[to_index]

    manipulation = from_column[:count]
    from_column = from_column[count:]

    if new_model:
        to_column = manipulation + to_column
    else:
        to_column = manipulation[::-1] + to_column

    STACKS[to_index] = to_column
    STACKS[from_index] = from_column


def parse_movement_info(movement: str) -> (int, int, int):
    match = re.match(r"^move (?P<count>\d+) from (?P<from>\d) to (?P<to>\d)$", movement)
    return int(match.group("count")), int(match.group("from")), int(match.group("to"))


def main():
    with open("input.txt", "r") as infile:
        moves = infile.read()

    instructions = map(parse_movement_info, moves.strip().split("\n"))
    # Part 1
    # for instruction in instructions:
    #     rearrange_stack(instruction, new_model=False)

    # Part 2
    for instruction in instructions:
        rearrange_stack(instruction, new_model=True)

    for stack in STACKS:
        print(stack[0])


if __name__ == "__main__":
    main()
