"""
I don't know if I'm going to finish this solution.

It tries to assess whether AREAS of trees are hidden. This could be more efficient for
large ass maps. Spent wayy to long on this approach...

Also it's useless for the part 2.
"""


MAX_TREE_HEIGHT = 9
MIN_TREE_HEIGHT = 0

POTENTIALLY_HIDDEN = "p"
HIDDEN = "h"
VISIBLE = "v"
UNKNOWN = "u"


def transpose_map(forest_map: list[tuple]) -> list[tuple[int]]:
    return list(zip(*forest_map))


def get_forest_map(forest: str) -> list[tuple[int]]:
    forest_map = []
    for line in forest.strip().split("\n"):
        forest_map.append(tuple(map(int, line)))

    return forest_map


def get_blank_map(n_row: int, n_col: int):
    return [[UNKNOWN] * n_col] * n_row


def get_potentially_visible_trees_in_line(line: tuple) -> tuple[int]:
    if not any(line):
        return tuple([0] * len(line))

    # First and last trees that match tree height - always visible
    first = line.index(True)
    last = line[::-1].index(True)

    # if there is only one tree matching the height level in the line
    if first + last == len(line):
        return tuple([0] * first + [5] + [0] * last)

    # 0 - unknown, 1 - potentially hidden, 5 - visible
    return tuple([0] * first + [5] + [1] * (len(line) - last - first - 2) + [5] + [0] * last)


def partial_map_for_level(forest_map: list[tuple[int]], tree_level: int):
    partial_map = []
    for line in forest_map:
        partial_map.append(get_potentially_visible_trees_in_line(tuple(map(lambda x: x >= tree_level, line))))

    return partial_map


def main():
    with open("input.txt", "r") as infile:
        forest = infile.read()

    """
    Place a layer of specific height (9 - 0) on top of the forest and check what trees touch it.
    For each tree height analyze rows and columns separately.
    Create a blank map, of the same size as the original, for marking trees that are hidden (default value of 0)
    Analysis:
        1) Get index of last and first trees in a row/column that are equal to or higher than tree height
        2) The first and last trees are visible, every tree between them (regardless of height) is hidden
        3) Create an intersection of hidden trees in rows and columns
        4) If a tree is hidden in both row and column, mark it as hidden in the blank map (set value to 1)
    Repeat analysis for each tree height - there should be a growing "island of hidden trees" in the map
    
    Note: Could be much easier with using NumPy matrix, but I want to stick with std. library
    """
    forest_map = get_forest_map(forest)
    forest_map_t = transpose_map(forest_map)

    number_of_rows = len(forest_map)
    number_of_columns = len(forest_map[0])

    treehouse_map = get_blank_map(number_of_rows, number_of_columns)

    for tree_level in range(MAX_TREE_HEIGHT, MIN_TREE_HEIGHT - 1, -1):
        partial_map = partial_map_for_level(forest_map, tree_level)
        partial_map_t = partial_map_for_level(forest_map_t, tree_level)
        # TO BE CONTINUED


if __name__ == "__main__":
    main()