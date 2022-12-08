def transpose_map(forest_map: list[tuple]) -> list[tuple[int]]:
    return list(zip(*forest_map))


def get_forest_map(forest: str) -> list[tuple[int]]:
    forest_map = []
    for line in forest.strip().split("\n"):
        forest_map.append(tuple(map(int, line)))

    return forest_map


def analyze_tree_by_tree(forest_map: list[tuple[int]]) -> list[list[int]]:
    treehouse_map = []
    forest_map_t = transpose_map(forest_map)
    for row_number, row in enumerate(forest_map):
        visible_trees = []
        for col_number, my_tree in enumerate(row):
            column = forest_map_t[col_number]
            # visibility
            left = any(tree >= my_tree for tree in row[:col_number])
            right = any(tree >= my_tree for tree in row[col_number + 1:])
            top = any(tree >= my_tree for tree in column[:row_number])
            bottom = any(tree >= my_tree for tree in column[row_number + 1:])
            visible_trees.append(int(not all([left, right, top, bottom])))

        treehouse_map.append(visible_trees)

    return treehouse_map


def get_visible_distance(row: tuple[int], index: int) -> tuple[int, int]:
    limit_height = row[index]

    visible_to_the_left = []
    for tree in row[:index][::-1]:
        visible_to_the_left.append(tree)
        if tree >= limit_height:
            break

    visible_to_the_right = []
    for tree in row[index + 1:]:
        visible_to_the_right.append(tree)
        if tree >= limit_height:
            break

    return len(visible_to_the_left), len(visible_to_the_right)


def get_scenic_score(forest_map: list[tuple[int]]) -> list[list[int]]:
    scenic_map = []
    forest_map_t = transpose_map(forest_map)
    for row_number, row in enumerate(forest_map):
        scenic_visibilities = []
        for col_number, my_tree in enumerate(row):
            column = forest_map_t[col_number]

            left, right = get_visible_distance(row, col_number)
            top, bottom = get_visible_distance(column, row_number)

            scenic_visibilities.append(left * right * top * bottom)

        scenic_map.append(scenic_visibilities)

    return scenic_map


def main():
    with open("input.txt", "r") as infile:
        forest = infile.read()

    forest_map = get_forest_map(forest)
    hidden_trees_map = analyze_tree_by_tree(forest_map)

    # Part 1
    visible_trees = 0
    for row in hidden_trees_map:
        visible_trees += sum(row)

    print(visible_trees)

    # Part 2
    scenic_map = get_scenic_score(forest_map)
    print(max([max(row) for row in scenic_map]))


if __name__ == "__main__":
    main()