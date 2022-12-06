def find_marker(message: str, marker_length) -> int:
    for i in range(len(message[:-(marker_length - 1)])):
        if len(set(message[i:i + marker_length])) == marker_length:
            return i + marker_length


def main():
    with open("input.txt", "r") as infile:
        message = infile.read()

    # Part 1
    print(find_marker(message, marker_length=4))

    # Part 2
    print(find_marker(message, marker_length=14))


if __name__ == "__main__":
    main()


