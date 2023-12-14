from pathlib import Path

if __name__ == "__main__":
    source = Path(__file__).resolve().parent
    input_file_path = source / "resources/input.txt"
    with input_file_path.open() as file:
        lines = file.read().splitlines()
        answer: int = 0
        for line in lines:
            number_to_sum: str = ""
            for character in line:
                if character.isdigit():
                    number_to_sum += character
                    break
            for character in line[::-1]:
                if character.isdigit():
                    number_to_sum += character
                    break
            answer += int(number_to_sum)
        print(answer)
