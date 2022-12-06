def get_item_priority(value: int) -> int:
    return value - 96 if value > 96 else value - 38


def get_priority(rucksack: str) -> int:
    sep = int(len(rucksack) / 2)
    return get_item_priority(ord(set(rucksack[:sep]).intersection(set(rucksack[sep:])).pop()))


def find_badge_priority(rucksacks: list[str]) -> int:
    return get_item_priority(ord(set.intersection(*map(set, rucksacks)).pop()))


def main():
    with open("input.txt", "r") as infile:
        rucksacks = infile.read()

    # Part 1
    print(sum(map(get_priority, rucksacks.strip().split("\n"))))

    # Part 2
    individual_rucksacks = rucksacks.strip().split("\n")
    priorities = []
    for i in range(0, len(individual_rucksacks), 3):
        priorities.append(find_badge_priority(individual_rucksacks[i:i+3]))

    print(sum(priorities))


if __name__ == "__main__":
    main()


