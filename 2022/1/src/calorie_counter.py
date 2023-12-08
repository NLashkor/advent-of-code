from os import path


def get_highest_calorie_holder(elves):
    return sorted([sum(elf) for elf in elves], reverse=True)[0]


def get_top_three_calorie_holders_total(elves):
    return sum(sorted([sum(elf) for elf in elves], reverse=True)[:3])


def organise_elves(file):
    elves = []
    elf = []
    for line in file:
        if line == "\n":
            elves.append(elf)
            elf = []
        else:
            elf.append(int(line))
    return elves


if __name__ == "__main__":
    source_path = "/".join(path.realpath(__file__).split("/")[:-1])
    with open(f"{source_path}/resources/input.txt", "r", encoding="utf-8") as file:
        elves = organise_elves(file)
    print(get_highest_calorie_holder(elves))
    print(get_top_three_calorie_holders_total(elves))
