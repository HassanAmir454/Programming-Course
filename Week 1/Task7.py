print("Calculate fuel consumption:")
Feed = input("Enter travel distance(In km):")
Distance = int(Feed)

Feed = input("Enter fuel usage(In liters):")
FuelUsage = int(Feed)

consumption = (FuelUsage/Distance)*100
consumption = float(consumption)      #we can use two same name variable for same reason

print(f"Consumption of fuel is {consumption} liters per 100 km")