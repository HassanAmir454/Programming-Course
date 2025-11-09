# Program starting.
# Insert filename: A7_T3_D1.csv
# Reading file "A7_T3_D1.csv".
# Analysing timestamps.
# Displaying results.
# ### Timestamp analysis ###
#  - Monday 24 stamps
#  - Tuesday 24 stamps
#  - Wednesday 0 stamps
#  - Thursday 0 stamps
#  - Friday 0 stamps
#  - Saturnday 0 stamps
#  - Sunday 0 stamps
# ### Timestamp analysis ###
# Program ending.

print("Program starting.")
file_name = input("Insert filename: ")
print(f"Reading file \"{file_name}\".")
print("Analysing timestamps.")
print("Displaying results.")
print("### Timestamp analysis ###")

# Open file and skip header line
with open(file_name, "r") as f:
    lines = f.readlines()
    data_lines = lines[1:]  # skip first line

# Initialize counters
mon_count = tue_count = wed_count = thurs_count = fri_count = sat_count = sun_count = 0

# Go through each line
for line in data_lines:
    line = line.strip()  # remove newline
    if line == "":       # skip empty lines
        continue

    # Count based on weekday name
    if line.startswith("Monday"):
        mon_count += 1
    elif line.startswith("Tuesday"):
        tue_count += 1
    elif line.startswith("Wednesday"):
        wed_count += 1
    elif line.startswith("Thursday"):
        thurs_count += 1
    elif line.startswith("Friday"):
        fri_count += 1
    elif line.startswith("Saturday"):
        sat_count += 1
    elif line.startswith("Sunday"):
        sun_count += 1

# Tuple for names (optional)
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# Print results
print(f" - {weekdays[0]} {mon_count} stamps")
print(f" - {weekdays[1]} {tue_count} stamps")
print(f" - {weekdays[2]} {wed_count} stamps")
print(f" - {weekdays[3]} {thurs_count} stamps")
print(f" - {weekdays[4]} {fri_count} stamps")
print(f" - {weekdays[5]} {sat_count} stamps")
print(f" - {weekdays[6]} {sun_count} stamps")

print("### Timestamp analysis ###")
print("Program ending.")
