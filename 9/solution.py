from operator import sub, add

DIRECTION_TRANSLATION = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}
START_POS = (0, 0)
KNOT_TO_KNOT_LENGTH = 1
KNOTS = 10


def sign(number: int) -> int:
    return 1 if abs(number) == number else -1


def move_knot(knot: tuple, direction) -> tuple:
    return tuple(map(add, knot, direction))


def fix_distance(head: tuple, tail: tuple) -> tuple:
    x_diff, y_diff = tuple(map(sub, head, tail))

    if abs(x_diff) > KNOT_TO_KNOT_LENGTH or abs(y_diff) > KNOT_TO_KNOT_LENGTH:
        x_fix = x_diff - sign(x_diff) * KNOT_TO_KNOT_LENGTH if abs(x_diff) > KNOT_TO_KNOT_LENGTH else x_diff
        y_fix = y_diff - sign(y_diff) * KNOT_TO_KNOT_LENGTH if abs(y_diff) > KNOT_TO_KNOT_LENGTH else y_diff
        return move_knot(tail, (x_fix, y_fix))

    return tail


def print_rope(rope: list[tuple], map_size: tuple[int, int]) -> None:
    offset_x, offset_y = int(map_size[0] / 2), int(map_size[1] / 2)
    rope_map = []
    for _ in range(map_size[0]):
        rope_map.append(["."] * map_size[1])

    for index, knot in enumerate(rope):
        rope_map[map_size[0] - (knot[1] + offset_x)][knot[0] + offset_y] = str(index)

    for line in rope_map:
        print("".join(line))

    print("\n====================\n")


def main():
    with open("input.txt", "r") as infile:
        moves = infile.read()

    moves = moves.strip().split("\n")

    # Part 1
    rope = [START_POS, START_POS]
    tail_visited = [rope[-1]]

    for move in moves:
        direction, distance = move.split(" ")
        change_in_coords = DIRECTION_TRANSLATION[direction]
        for _ in range(int(distance)):
            rope[0] = move_knot(rope[0], change_in_coords)
            rope[-1] = fix_distance(rope[0], rope[-1])
            tail_visited.append(rope[-1])

    print(len(set(tail_visited)))

    # Part 2
    rope_2 = [START_POS] * KNOTS
    tail_visited_2 = [rope_2[-1]]

    for move in moves:
        direction, distance = move.split(" ")
        change_in_coords = DIRECTION_TRANSLATION[direction]
        for _ in range(int(distance)):
            rope_2[0] = move_knot(rope_2[0], change_in_coords)
            for knot_index in range(1, len(rope_2)):
                rope_2[knot_index] = fix_distance(rope_2[knot_index - 1], rope_2[knot_index])

            tail_visited_2.append(rope_2[-1])

    print(len(set(tail_visited_2)))


if __name__ == "__main__":
    main()
