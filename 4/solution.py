def parse_ranges(sections: str) -> [int, int]:
    first, second = [s.split("-") for s in sections.split(",")]
    lower_0, upper_0 = int(first[0]), int(first[1])
    lower_1, upper_1 = int(second[0]), int(second[1])
    return lower_0, upper_0, lower_1, upper_1


def sections_fully_overlap(section: str) -> bool:
    lower_0, upper_0, lower_1, upper_1 = parse_ranges(section)
    lower = lower_0 - lower_1
    upper = upper_0 - upper_1
    return (lower <= 0 <= upper) or (upper <= 0 <= lower)


def sections_overlap(section: str) -> bool:
    lower_0, upper_0, lower_1, upper_1 = parse_ranges(section)
    diff_1 = upper_0 - lower_1  # > 0
    diff_2 = lower_0 - upper_1  # < 0
    return (diff_2 <= 0 <= diff_1) or (diff_1 <= 0 <= diff_2)


# 1 0 0 1
# 0 1 1 0

# 0 1 0 1
# 1 0 1 0

# 1 1 0 0
# 0 0 1 1

def main():
    with open("input.txt", "r") as infile:
        sections = infile.read()

    # Part 1
    print(sum(map(sections_fully_overlap, sections.strip().split("\n"))))

    # Part 2
    print(sum(map(sections_overlap, sections.strip().split("\n"))))


if __name__ == "__main__":
    main()


