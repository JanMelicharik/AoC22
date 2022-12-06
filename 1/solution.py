def sum_list_str(list_str: str):
    return sum(map(int, list_str.strip().split("\n")))


def main():
    with open("input.txt", "r") as infile:
        elf_list = infile.read()

    calories = list(map(sum_list_str, elf_list.split("\n\n")))

    # Print elf who carries the most calories
    print(max(calories))

    # Print how many calories are carrying the top 3 elves
    print(sum(sorted(calories, reverse=True)[0:3]))


if __name__ == "__main__":
    main()
