# Program starting.
# Collect positive integers.
# Insert positive integer(negative stops): 5
# Insert positive integer(negative stops): 10
# Insert positive integer(negative stops): 15
# Insert positive integer(negative stops): -1
# Stopped collecting positive integers.
# Displaying 3 integers:
# - Index 0 => Ordinal 1 => Integer 5
# - Index 1 => Ordinal 2 => Integer 10
# - Index 2 => Ordinal 3 => Integer 15
# Program ending.


print("Program starting.")
print("Collect positive integers.")
integers = []
count = 0
while True:
    integer = int(input("Insert positive integer(negative stops): "))
    if integer >= 0:
        integers.append(integer)
        count += 1
    else:
        print("Stopped collecting positive integers.")
        break
        
print(f"Displaying {count} integers:")
l = len(integers)
for i in range(0, l-1):
    print(f"- Index {i} => Ordinal {i+1} => Integer {integers[i]}")


print("Program ending.")
