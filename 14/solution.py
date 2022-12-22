from itertools import zip_longest
from operator import add


SAND_SOURCE_COOR = (500, 0)


def get_cave_depth(cave: list[tuple]) -> int:
    return max([c[1] for c in cave])


def get_corner(corner_coor: str) -> tuple[int, int]:
    x, y = corner_coor.split(",")
    return int(x), int(y)


def create_wall(horizontal: list[int], vertical: list[int]) -> list[tuple[int, int]]:
    horizontal_shift = list(range(horizontal[0], horizontal[1] + 1))
    vertical_shift = list(range(vertical[0], vertical[1] + 1))
    fill_in = horizontal_shift[0] if len(horizontal_shift) == 1 else vertical_shift[0]
    return list(zip_longest(horizontal_shift, vertical_shift, fillvalue=fill_in))


def build_cave(crevices: list[str]) -> list[tuple[int, int]]:
    cave = []
    for crevice in crevices:
        corners = [get_corner(corner) for corner in crevice.split(" -> ")]
        for start_coor, end_coor in zip(corners[:-1], corners[1:]):
            horizontal, vertical = [sorted(coor) for coor in zip(start_coor, end_coor)]
            cave += create_wall(horizontal, vertical)

    return list(set(cave))


def let_the_sand_fall(cave: list[tuple[int,int]], sand_source: tuple[int, int], cave_depth: int) -> int:
    down_left, down, down_right = (-1, 1), (0, 1), (1, 1)

    def get_next_position(_sand_unit: tuple, _occupied_space: list[tuple]) -> tuple:
        next_down = tuple(map(add, _sand_unit, down))

        if next_down not in _occupied_space:
            return next_down

        next_down_left = tuple(map(add, _sand_unit, down_left))
        if next_down_left not in _occupied_space:
            return next_down_left

        next_down_right = tuple(map(add, _sand_unit, down_right))
        if next_down_right not in _occupied_space:
            return next_down_right

        return _sand_unit

    occupied_space = [] + cave
    sand_unit = sand_source
    sand_unit_count = 1

    while True:
        next_position = get_next_position(sand_unit, occupied_space)
        print(sand_unit_count, sand_unit, next_position)

        if next_position == sand_unit:
            if next_position == sand_source:
                return sand_unit_count

            occupied_space.append(sand_unit)
            sand_unit = sand_source
            sand_unit_count += 1
            continue

        if sand_unit[1] >= cave_depth:
            return sand_unit_count - 1

        sand_unit = next_position


def add_cave_floor(cave: list[tuple[int, int]]) -> list[tuple[int, int]]:
    floor_level = get_cave_depth(cave) + 2
    return cave + [
        (span, floor_level)
        for span in range(
            SAND_SOURCE_COOR[0] - (floor_level + 100),
            SAND_SOURCE_COOR[0] + (floor_level + 101),
        )
    ]


def main():
    with open("input.txt", "r") as infile:
        cave = infile.read().strip()

    cave = build_cave(cave.split("\n"))
    cave_depth = get_cave_depth(cave)

    # Part 1
    print(let_the_sand_fall(cave, SAND_SOURCE_COOR, cave_depth))

    # Part 2
    cave = add_cave_floor(cave)
    # Runs for a long time, depth is 180 so the number of sand units
    # can be up to "180 ** 2 - len(cave)" (and will probably be close)
    print(let_the_sand_fall(cave, SAND_SOURCE_COOR, cave_depth + 2))


if __name__ == "__main__":
    main()
