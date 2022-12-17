from __future__ import annotations

import re

from math import floor


ROUNDS = 10000
# ROUNDS = 20


class Monkey:
    def __init__(self, monkey_id, starting_items, operation, test, target_1, target_2):
        self.id = self._get_monkey_id(monkey_id)
        self.items = self._get_starting_items(starting_items)
        self.operation = self._get_operation(operation)
        self.divisor = self._get_divisor(test)
        self.targets = [self._get_target(target_1), self._get_target(target_2)]
        self.inspected_items = 0

    def throw_stuff(self, monkeys: dict[int, Monkey], divisor):
        for item in self.items:
            worry_index = self._get_worry_index(item)
            # Part 1
            # worry_index = floor(worry_index / 3)
            target = monkeys[self.targets[bool(worry_index % self.divisor)]]
            target.items.append(worry_index % divisor)
            self.inspected_items += 1

        self.items = []

    def _get_worry_index(self, item_value) -> int:
        return eval(self.operation.replace("old", f"{item_value}"))

    @staticmethod
    def _get_monkey_id(monkey_id: str) -> int:
        return int(re.search(r"Monkey (?P<id>\d+):", monkey_id).group("id"))

    @staticmethod
    def _get_starting_items(starting_items: str) -> list[int]:
        return [int(item) for item in starting_items.split(",")]

    @staticmethod
    def _get_operation(operation: str) -> str:
        return operation.replace(" new = ", "")

    @staticmethod
    def _get_divisor(test: str) -> int:
        return int(re.search(r"divisible by (?P<div>\d+)", test).group("div"))

    @staticmethod
    def _get_target(target: str) -> int:
        return int(re.search(r"throw to monkey (?P<target>\d+)", target).group("target"))

    def __repr__(self):
        return f"Monkey ID: {self.id}, targets: {self.targets}, test divisor: {self.divisor}, throws: {self.items}"


def create_monkey(monkey_str: str) -> Monkey:
    monkey_list = monkey_str.split("\n")
    return Monkey(monkey_list[0], *[conf.split(":")[1] for conf in monkey_list[1:]])


def main():
    with open("input.txt", "r") as infile:
        monkeys_list = infile.read().strip().split("\n\n")

    monkeys = {}
    common = 1
    for monkey_str in monkeys_list:
        monke = create_monkey(monkey_str)
        monkeys[monke.id] = monke
        common *= monke.divisor

    # part 1
    for _ in range(ROUNDS):
        for monkey_index in range(len(monkeys)):
            monkey = monkeys[monkey_index]
            monkey.throw_stuff(monkeys, common)

    most_active_monkeys = sorted([monkey.inspected_items for monkey in monkeys.values()])
    print(most_active_monkeys[-1] * most_active_monkeys[-2])


if __name__ == "__main__":
    main()
