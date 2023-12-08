from pathlib import Path

if __name__ == "__main__":
    source = Path(__file__).resolve().parent
    input_file_path = source / "resources/input.txt"
    with input_file_path.open() as file:
        lines = file.read().splitlines()
        answer = 0
        for line in lines:
            for index, character in enumerate(line):
                if character.isdigit():
                    answer += int(character)
                    break
            for index, character in enumerate(line[::-1]):
                if character.isdigit():
                    answer += int(character)
                    break
        print(answer)
