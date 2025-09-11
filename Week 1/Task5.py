print("Calculate the area of a wall.")
Feed = input("Enter the width in meters:")
Width = int(Feed)
# Width = float(Feed)  it is good you can give measurements also in decimal

Feed = input("Enter the height in meters:")
Height = int(Feed)
# Height = float(Feed)  it is good you can give measurements also in decimal


print(f"Width is {Width}m and height is {Height}m")

Area = Width*Height
print(f"The wall will be {Area} square meters")