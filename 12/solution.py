from collections import defaultdict


START = "S"
END = "E"

reference_level = ord("a")


def get_position(area_map: list[str], node: str) -> tuple[int, int]:
    for row_number, line in enumerate(area_map):
        if node in line:
            return row_number, line.index(node)


def find_possible_starting_points(area_map: list[tuple[int]]) -> list[tuple[int, int]]:
    possible_starting_points = []
    for row_index, row in enumerate(area_map):
        for col_index, current_node_level in enumerate(row):
            if current_node_level == 0:
                possible_starting_points.append((row_index, col_index))

    return possible_starting_points


def analyze_terrain(area_lines: list[str]) -> tuple[tuple, tuple, list[tuple[int]]]:
    start_pos = get_position(area_lines, START)
    end_pos = get_position(area_lines, END)

    area_lines[start_pos[0]] = area_lines[start_pos[0]].replace("S", "a")
    area_lines[end_pos[0]] = area_lines[end_pos[0]].replace("E", "z")

    area_map = [tuple(map(lambda letter: ord(letter) - reference_level, line)) for line in area_lines]
    return start_pos, end_pos, area_map


def create_graph(area_map: list[tuple[int]]) -> dict[tuple, list[tuple[int, int]]]:
    map_width = len(area_map[0])
    map_height = len(area_map)

    graph = defaultdict(list)
    for row_index, row in enumerate(area_map):
        for col_index, current_node_level in enumerate(row):
            neighbor_nodes = [
                (row_index, col_index - 1),
                (row_index, col_index + 1),
                (row_index - 1, col_index),
                (row_index + 1, col_index),
            ]
            for neighbor_node in neighbor_nodes:
                if 0 <= neighbor_node[0] < map_height and 0 <= neighbor_node[1] < map_width:
                    neighbor_node_level = area_map[neighbor_node[0]][neighbor_node[1]]
                    if neighbor_node_level - current_node_level <= 1:
                        graph[(row_index, col_index)].append(neighbor_node)

    return graph


def bfs(graph: dict[tuple, list[tuple]], start_node: tuple[int, int], end_node: tuple[int, int]) -> list[tuple[int]]:
    visited = [start_node]
    queue = [start_node]
    parents = {}

    while queue:
        current = queue.pop(0)
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
                parents[neighbor] = current

    if end_node not in parents:
        return []

    path = []
    current = end_node
    while start_node not in path:
        path.append(parents[current])
        current = parents[current]

    return path[::-1]


def main():
    with open("input.txt", "r") as infile:
        area_lines = infile.read().strip().split("\n")

    start_pos, end_pos, area_map = analyze_terrain(area_lines)

    graph = create_graph(area_map)

    # Part 1
    shortest_path = bfs(graph, start_pos, end_pos)
    print(len(shortest_path))

    # Part 2
    starting_points = find_possible_starting_points(area_map)
    path_lengths = []
    for i, starting_point in enumerate(starting_points):
        print(f"{i} / {len(starting_points)}")
        shortest_path_from_point = bfs(graph, starting_point, end_pos)
        if shortest_path_from_point:
            print(f"OK")
            path_lengths.append(len(shortest_path_from_point))

    print(min(path_lengths))


if __name__ == "__main__":
    main()
