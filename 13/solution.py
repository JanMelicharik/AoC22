from ast import literal_eval

CORRECT = "CORRECT"
WRONG = "WRONG"
UNDECIDED = "UNDECIDED"


def packet_pair_correct(packet_pair: str) -> str:
    left, right = map(literal_eval, packet_pair.split("\n"))

    def analyze_integers(left_int, right_int):
        if left_int == right_int:
            return UNDECIDED
        return [WRONG, CORRECT][left_int < right_int]

    def analyze_lists(left_list, right_list):
        decision = UNDECIDED
        for left_item, right_item in zip(left_list, right_list):
            left_type, right_type = type(left_item), type(right_item)

            if left_type == right_type:
                if left_type == list:
                    decision = analyze_lists(left_item, right_item)
                if left_type == int:
                    decision = analyze_integers(left_item, right_item)

            if left_type == int and right_type == list:
                decision = analyze_lists([left_item], right_item)
            if left_type == list and right_type == int:
                decision = analyze_lists(left_item, [right_item])

            if decision != UNDECIDED:
                return decision

        if len(left_list) != len(right_list):
            decision = [WRONG, CORRECT][len(left_list) < len(right_list)]

        return decision

    return analyze_lists(left, right)


def tuplize(packet: str) -> tuple:
    values = packet.replace("[", "").replace("]", "").split(",")
    return tuple([int(value) if value else 0 for value in values])


def main():
    with open("input.txt", "r") as infile:
        packet_pairs = infile.read().strip()

    packet_pairs_in_right_order = []
    for index, packet_pair in enumerate(packet_pairs.split("\n\n"), start=1):
        packet_pairs_in_right_order.append((index, packet_pair_correct(packet_pair)))

    # Part 1
    print(sum([index for index, value in packet_pairs_in_right_order if value == CORRECT]))

    # Part 2 - a bit hacky but works - might break in case there are more packets which tuplize to (2,)
    sorted_packets = sorted([tuplize(packet) for packet in packet_pairs.replace("\n\n", "\n").split("\n")] + [(2,), (6,)])
    print((sorted_packets.index((2,)) + 1) * (sorted_packets.index((6,)) + 1))


if __name__ == "__main__":
    main()
