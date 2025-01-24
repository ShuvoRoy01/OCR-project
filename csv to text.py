import csv

# Path to the CSV file
csv_file = "output.csv"

# Reading the CSV file
try:
    with open(csv_file, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        
        # Reading the header
        header = next(reader)
        print("Header:", header)

        # Reading the rows
        for row in reader:
            print("Row:", row)
except FileNotFoundError:
    print(f"The file {csv_file} does not exist.")
except Exception as e:
    print(f"Error reading the file: {e}")
