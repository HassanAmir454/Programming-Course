def askDimension(PPrompt) -> float:
   Feed = float(input(f"Insert {PPrompt}: "))
   return Feed

def calcRectangleArea(PWidth, PHeight) -> float:
   Area = PWidth * PHeight
   return float(Area)

def main() -> None:
   print("Program Starting.")
   Width = askDimension("width")
   Height = askDimension("height")
   Area = calcRectangleArea(Width, Height)
   print("")
   print(f"Area is {Area}²")
   print("Program Starting.")
   return None
main()