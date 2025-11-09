# Program starting.
# Insert filename: A7_T5_D1.csv
# Reading file "A7_T5_D1.csv".
# Analysing timestamps.
# Displaying results.
# ### Electricity consumption summary ###
#  - Monday usage 2510.00 kWh, cost 279.42 €
#  - Tuesday usage 2364.00 kWh, cost 286.46 €
#  - Wednesday usage 0.00 kWh, cost 0.00 €
#  - Thursday usage 0.00 kWh, cost 0.00 €
#  - Friday usage 0.00 kWh, cost 0.00 €
#  - Saturnday usage 0.00 kWh, cost 0.00 €
#  - Sunday usage 0.00 kWh, cost 0.00 €
# ### Electricity consumption summary ###
# Program ending.

print("Program starting.")
file_name = input("Insert filename: ")
print(f"Reading file {file_name}. ")
print("Analysing timestamps.")
print("Displaying results.")

# Weekdays tuple
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# Create a class to hold timestamp info
class Timestamp:
    weekday = ""
    hour = ""
    consumption = 0.0
    price = 0.0

# Create empty list to store timestamps
timestamps = []

# Read the file
with open(file_name, "r") as f:
    lines = f.readlines()

# Skip header line
data_lines = lines[1:]

# Process each line
for line in data_lines:
    line = line.strip()       # remove \n
    if line == "":            # skip empty lines
        continue

    parts = line.split(";")   # split by semicolon

    t = Timestamp()
    t.weekday = parts[0]
    t.hour = parts[1]
    t.consumption = float(parts[2])
    t.price = float(parts[3])
    timestamps.append(t)

# Initialize daily usage and cost for all weekdays
daily_usage = {}
daily_cost = {}
for day in WEEKDAYS:
    daily_usage[day] = 0.0
    daily_cost[day] = 0.0

# Go through all timestamps and calculate totals
for t in timestamps:
    total = t.consumption * t.price
    daily_usage[t.weekday] += t.consumption
    daily_cost[t.weekday] += total

# Print the results
print("### Electricity consumption summary ###")
for day in WEEKDAYS:
    print(f" - {day} usage {daily_usage[day]:.2f} kWh, cost {daily_cost[day]:.2f} €")
print("### Electricity consumption summary ###")
print("Program ending.")