# Program starting.

# Options:
# 1 - View devices
# 2 - Turn device on/off
# 3 - Daily consumption
# 0 - Exit
# Your choice: 1

# Devices:
# - Light (Status: off, 0.05 kWh/hour)
# - Heater (Status: on, 1.50 kWh/hour)
# - Fan (Status: off, 0.20 kWh/hour)

# Options:
# 1 - View devices
# 2 - Turn device on/off
# 3 - Daily consumption
# 0 - Exit
# Your choice: 2

# Enter device name: Light
# Light turned ON.

# Options:
# 1 - View devices
# 2 - Turn device on/off
# 3 - Daily consumption
# 0 - Exit
# Your choice: 3

# Enter device name: Heater
# Enter hours ON: 5

# Daily consumption: 7.5 kWh
# Estimated cost (@0.20 €/kWh): 1.50 €

# Options:
# 1 - View devices
# 2 - Turn device on/off
# 3 - Daily consumption
# 0 - Exit
# Your choice: 0

# Exiting program.
# Program ending.
def consump(name, hours):
    for device in devices:
        if device['name'].lower() == name.lower():
            rate = device['kWh'] * hours
            cost = 0.20*rate
            return (
                f"\nDaily consumption: {rate} kWh\n"
                f"Estimated cost (@0.20 €/kWh): {cost} €"
            )
    return "Device not found."
          


devices = [
        {"name": "Light", "status": "off", "kWh": 0.05 },
        {"name": "Heater", "status": "on", "kWh": 1.50 },
        {"name": "Fan", "status": "off", "kWh": 0.20 }
]
def main() -> None:
    print("Program starting.")

    

    while True:
        print("\nOptions:")
        print("1 - View devices")
        print("2 - Turn device on/off")
        print("3 - Daily consumption")
        print("0 - Exit")
        choice = int(input("Your choice: "))
        if choice == 1:
            print("\nDevices:")
            for i in devices:
                print(f"- {i['name']} (status: {i['status']}, {i['kWh']:.2f} kWh/hour)")
        elif choice == 2:
            name = input("Enter device name: ")
            found = False
            for device in devices:
                if device["name"].lower() == name.lower():
                    found = True
                    if device["status"] == "off":
                        device["status"] = "on"
                        print(f"{device['name']} turned ON")
                    else:
                        device["status"] = "off"
                        print(f"{device['name']} turned OFF")
            if not found:
                print("Device not found.")
        elif choice == 3:
            name = input("Enter device name:")
            hours = int(input("Enter hours ON:"))
            print(consump(name, hours))
            

        elif choice == 0:
            print("Exiting program.")
            print("Program ending")
            break
main()




            

            

