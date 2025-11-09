print("Program starting.")
file_name = input("Insert filename: ")
print(f"Reading file {file_name}. ")
print("Electricity usage:")
class Timestamp:
    weekday = ""
    hour = ""
    consumption = 0.0
    price = 0.0

timestamps = []

with open(f"{file_name}", "r") as f:
    lines = f.readlines()
    data_lines = lines[1:]
for line in data_lines:
    line = line.strip()
    if line == "":
        continue
    parts = line.split(";")

    t = Timestamp()
    t.weekday = parts[0]
    t.hour = parts[1]
    t.consumption = float(parts[2])
    t.price = float(parts[3])

    timestamps.append(t)
for t in timestamps:
    total = t.price * t.consumption
    print(f" - {t.weekday} {t.hour}, price {t.price:.2f} € , consumption {t.consumption:.2f} kWh, total {total:.2f} € ")

print("Program ending.")


# # main.py

# print("Program starting.")

# # Define the data structure
# class TIMESTAMP:
#     weekday = ""
#     hour = ""
#     consumption = 0.0
#     price = 0.0


# # Function to read timestamps from a file
# def readTimestamps(filename, timestamps):
#     with open(filename, "r") as f:
#         lines = f.readlines()
#         data_lines = lines[1:]  # skip header

#     for line in data_lines:
#         line = line.strip()
#         if line == "":
#             continue

#         parts = line.split(";")
#         t = TIMESTAMP()
#         t.weekday = parts[0]
#         t.hour = parts[1]
#         t.consumption = float(parts[2])
#         t.price = float(parts[3])
#         timestamps.append(t)


# # Function to display timestamps
# def displayTimestamps(timestamps):
#     print("Electricity usage:")
#     for t in timestamps:
#         total = t.price * t.consumption
#         print(f" - {t.weekday} {t.hour}, price {t.price:.2f} €, consumption {t.consumption:.2f} kWh, total {total:.2f} €")


# # Main program
# def main():
#     file_name = input("Insert filename: ")
#     print(f'Reading file "{file_name}".')
#     timestamps = []
#     readTimestamps(file_name, timestamps)
#     displayTimestamps(timestamps)
#     print("Program ending.")


# if __name__ == "__main__":
#     main()