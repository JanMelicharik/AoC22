EXECUTION_TIME = {
    "noop": 1,
    "addx": 2,
}
CHECK_CYCLES = [20, 60, 100, 140, 180, 220]
LINE_LENGTH = 40
LINES = 6


def get_pixel(position: int, registry: int) -> str:
    return "#" if position in [registry - 1, registry, registry + 1] else " "


def main():
    with open("input.txt", "r") as infile:
        instructions = infile.read().strip().split("\n")

    signal_strengths = []
    pixels = [[] for _ in range(LINES)]
    registry = 1
    cycle = 0
    instruction_index = 0
    execute_for = 0
    instruction = None

    while instruction_index < len(instructions):
        # Start
        cycle += 1
        if not instruction:
            instruction = instructions[instruction_index].split(" ")
            execute_for = EXECUTION_TIME[instruction[0]]

        # Mid
        if cycle in CHECK_CYCLES:
            signal_strengths.append(registry * cycle)

        execute_for -= 1
        pixels[(cycle - 1) // LINE_LENGTH].append(get_pixel((cycle - 1) % LINE_LENGTH, registry))

        # End
        if execute_for == 0:
            if len(instruction) > 1:
                registry += int(instruction[1])
            instruction = None
            instruction_index += 1

        if instruction_index == len(instructions):
            break

    print(sum(signal_strengths))

    # Part 2
    for row in pixels:
        print("".join(row))


if __name__ == "__main__":
    main()
