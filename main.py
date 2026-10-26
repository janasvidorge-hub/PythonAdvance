
from pathlib import Path

def count_lines(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return sum(1 for line in file)


def extract_first_two_lines(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return [next(file, "") for _ in range(2)]


def write_to_file(filename, lines):
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(lines)


# Main Program
input_file = Path(__file__).parent / "input.txt"
output_file = Path(__file__).parent / "output.txt"

try:
    total_lines = count_lines(input_file)
    print("Total number of lines:", total_lines)

    first_two_lines = extract_first_two_lines(input_file)

    print("\nFirst two lines:")
    for line in first_two_lines:
        print(line.rstrip("\n"))

    write_to_file(output_file, first_two_lines)

    print("\nFirst two lines have been written to output.txt")

except FileNotFoundError:
    print("Error: input.txt was not found.")
except OSError as error:
    print("File error:", error)
