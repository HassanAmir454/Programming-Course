from datetime import datetime

MONTHS = (
    "January","February","March","April","May","June","July","August","September","October","November","December"
)

WEEKDAYS = (
    "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"
)

def readTimestamps(PFilename: str, PTimestamps: list[datetime]) -> None:
    with open(PFilename, "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            timestamp = datetime.strptime(line, "%Y-%m-%dT%H:%M")
            PTimestamps.append(timestamp)

def calculateYears(PYear: int, PTimestamps: list[datetime]) -> int:
    count = 0
    for t in PTimestamps:
        if t.year == PYear:
            count += 1
    return count

def calculateMonths(PMonth: str, PTimestamps: list[datetime]) -> int:
    count = 0
    month_index = MONTHS.index(PMonth) + 1
    for t in PTimestamps:
        if t.month == month_index:
            count += 1
    return count

def calculateWeekdays(PWeekday: str, PTimestamps: list[datetime]) -> int:
    count = 0
    for t in PTimestamps:
        weekday = t.strftime("%A")
        if weekday == PWeekday:
            count += 1
    return count
