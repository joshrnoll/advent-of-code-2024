import re
from my_lib import get_input


def main():
    mem = get_input()

    instructions = get_instructions(mem)
    total = 0
    for instruction in instructions:
        total += call_instruction(instruction)
    print(total)

def get_instructions(str):
    match = re.findall(r"mul\(\d{1,3},\d{1,3}\)", str)
    return match

def call_instruction(str):
    numbers = re.findall(r"\d{1,3}", str)
    answer = int(numbers[0]) * int(numbers[1])
    return answer


if __name__ == "__main__":
    main()