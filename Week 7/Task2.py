# Program starting.
# Insert comma separated integers: 2,2,1,3
# There are 4 integers in the list.
# Sum of the integers is 8 and it's even.
# Program ending.

print("Program starting.")
integers = input("Insert comma separated integers: ")
numbers = integers.split(",")
valid_num = []
invalid_num = []
count = 0
for num in numbers:
    num = num.strip()
    if num.isdigit():
        valid_num.append(int(num))
        count += 1
    else:
        invalid_num.append(num)
        print(f"Invalid value \"{num}\" detected.")

sum_num = sum(valid_num)
def even_or_odd(sum_num):
    if sum_num % 2 == 0:
        return "even"
    else:
        return "odd" 
    
result = even_or_odd(sum_num)

    
print(f"There are {count} integers in the list.")
print(f"Sum of the integers is {sum_num} and it's {result}")
print("Program ending.")