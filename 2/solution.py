WIN = 6
DRAW = 3
LOSE = 0

ROCK = 1
PAPER = 2
SCISSORS = 3

signs = {"X": ROCK, "Y": PAPER, "Z": SCISSORS, "A": ROCK, "B": PAPER, "C": SCISSORS}

ACTIONS_1 = ["A", "B", "C"]
ACTIONS_2 = ["X", "Y", "Z"]

outcome_map = {"X": -1, "Y": 0, "Z": 1}


def evaluate_round(round_str: str) -> int:
    o, m = round_str.split(" ")

    win_pts = LOSE
    if ACTIONS_2.index(m) == ((ACTIONS_1.index(o) + 1) % 3):
        win_pts = WIN

    if ACTIONS_2.index(m) == ACTIONS_1.index(o):
        win_pts = DRAW

    return win_pts + signs[m]


def strategy_round(round_str: str) -> int:
    action, outcome = round_str.split(" ")
    return signs[ACTIONS_1[(ACTIONS_1.index(action) + outcome_map[outcome]) % 3]] + (outcome_map[outcome] + 1) * 3


def main():
    # X, A - Rock       1pt
    # Y, B - Paper      2pts
    # Z, C - Scissors   3pts

    # R > S
    # S > P
    # P > R

    # Pt. 2 - X = Lose, Y = Draw, Z = Win

    with open("input.txt", "r") as infile:
        strategy = infile.read()

    print(sum(map(evaluate_round, strategy.strip().split("\n"))))
    print(sum(map(strategy_round, strategy.strip().split("\n"))))


if __name__ == "__main__":
    main()
