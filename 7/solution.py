import re
from collections import defaultdict

FILE_PATTERN = r"^(?P<filesize>\d+) [a-z]+(\.[a-z]+)?$"
CD_PATTERN = r"^\$ cd (?P<path>[a-z/.]+)$"
USELESS_COMMANDS_PATTERN = r"(\$ cd /|\$ ls|dir [a-z+]+)\n"

TOTAL_SPACE = 70_000_000
REQUIRED_SPACE = 30_000_000


def get_current_path(path_components: list[str]) -> str:
    return "".join(path_components)


def update_path(current_path: list[str], new_component: str) -> list[str]:
    if new_component == "..":
        return current_path[:-1]

    return current_path + [f"{new_component}/"]


def construct_tree(commands: str) -> dict[str, int]:
    paths = defaultdict(int)
    current_path = ["/"]

    for command in commands.split("\n"):
        if is_file := re.fullmatch(FILE_PATTERN, command):
            # Adding file to all parent folders
            for index in range(len(current_path)):
                paths[get_current_path(current_path[:index + 1])] += int(is_file.group("filesize"))

        if is_cd := re.fullmatch(CD_PATTERN, command):
            current_path = update_path(current_path, is_cd.group("path"))

    return paths


def main():
    with open("input.txt", "r") as infile:
        # Not really commands but ¯\_(ツ)_/¯
        commands = infile.read()

    tree = construct_tree(re.sub(USELESS_COMMANDS_PATTERN, "", commands))

    # Part 1
    print(sum([folder_size for folder_size in tree.values() if folder_size <= 100_000]))

    # Part 2
    missing_space = REQUIRED_SPACE - (TOTAL_SPACE - tree["/"])
    print(sorted([folder_size for folder_size in tree.values() if folder_size >= missing_space])[0])


if __name__ == "__main__":
    main()
