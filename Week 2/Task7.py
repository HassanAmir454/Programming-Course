print("Program starting.")

temperature_farenheit = float(input("Insert temperature in Farenheit: "))
temperature_celcious = (temperature_farenheit - 32)/1.8

print(f"{round(temperature_farenheit,1)}°F  is  {round(temperature_celcious,1)}°C")

print("Program ending.")