import csv
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row["Marks"]) > 75:
            print(row["Name"],row["Marks"])

            