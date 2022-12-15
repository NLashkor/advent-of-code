from os import path

POINTS_MAPPING = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
    "win": 6,
    "draw": 3,
    "loss": 0,
}
STATE_MAPPING = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

OUTCOMES = {
    "AX": "draw",
    "AY": "win",
    "AZ": "loss",
    "BX": "loss",
    "BY": "draw",
    "BZ": "win",
    "CX": "win",
    "CY": "loss",
    "CZ": "draw",
}


def calculate_score(result, line):
    return POINTS_MAPPING[result] + POINTS_MAPPING[STATE_MAPPING[line[2]]]


if __name__ == "__main__":
    source_path = "/".join(path.realpath(__file__).split("/")[:-1])
    score_count = 0
    with open(f"{source_path}/resources/input.txt", "r", encoding="utf-8") as file:
        for line in file:
            result = OUTCOMES[line.strip().replace(" ", "")]
            score_count += calculate_score(result=result, line=line)
        print(score_count)
