
import csv
import json
from pathlib import Path


def csv_to_json(csv_file, json_file):
    data = []

    # Read data from CSV file
    with open(csv_file, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)

    # Write data to JSON file
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return len(data)


# Main Program
folder = Path(__file__).parent
input_file = folder / "students.csv"
output_file = folder / "students.json"

try:
    total_students = csv_to_json(input_file, output_file)

    print("CSV file converted to JSON successfully.")
    print("Total records converted:", total_students)
    print("JSON data written to:", output_file.name)

except FileNotFoundError:
    print("Error: students.csv was not found.")
    print("Please create students.csv in the same folder as main.py.")

except OSError as error:
    print("File error:", error)
