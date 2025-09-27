print("Program starting.\n")
print("Options:")
print("1 - Celsius to Farenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")
choice = int(input("Your choice:"))
if choice == 1:
    temp_celcious = float(input("Insert temperature in Celcius: "))
    temp_farenheit = (temp_celcious * 1.8) + 32
    print(f"{round(temp_celcious,1)}°C  equals to  {round(temp_farenheit,1)}°F \n")

elif choice == 2:
    temp_farenheit = float(input("Insert the amount of Farenheit: "))
    temp_celcious = (temp_farenheit - 32)/1.8
    print(f"{round(temp_farenheit,1)}°F  equals to  {round(temp_celcious,1)}°C \n")
elif choice == 0:
    print("Exiting...\n")
else:
    print("Unknown option.\n")
print("Program ending.")