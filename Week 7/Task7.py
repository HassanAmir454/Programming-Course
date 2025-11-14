# Insert config(filename): iconf1.txt
# Insert plugs (y/n)?: n
# No extra plugs inserted.
# Enigma initialized.

# Insert row (empty stops): HELLO
# Character "H" illuminated as "E"
# Character "E" illuminated as "C"
# Character "L" illuminated as "M"
# Character "L" illuminated as "A"
# Character "O" illuminated as "M"
# Converted row - "ECMAM".

# Insert row (empty stops): ECMAM
# Character "E" illuminated as "H"
# Character "C" illuminated as "E"
# Character "M" illuminated as "L"
# Character "A" illuminated as "L"
# Character "M" illuminated as "O"
# Converted row - "HELLO".

# Insert row (empty stops): 

# Enigma closing.


# filename = input("Insert config(filename): ")
# plugs = input("Insert plugs (y/n)?: ")
# if plugs == "y":
#     print("Plugboard not implemented in this version.")
# else:
#     print("No extra plugs inserted.")

# print("Enigma initialized.\n")

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def load_config(filename):
    """Read the rotors and reflector from a file"""
    with open(filename, "r") as f:
        lines = f.read().splitlines()

    # make empty strings first
    rotor1 = rotor2 = rotor3 = reflector = ""

    # read each line from the file
    for line in lines:
        if line.startswith("Rotor1:"):
            rotor1 = line.split(":")[1].strip()
        elif line.startswith("Rotor2:"):
            rotor2 = line.split(":")[1].strip()
        elif line.startswith("Rotor3:"):
            rotor3 = line.split(":")[1].strip()
        elif line.startswith("Reflector:"):
            reflector = line.split(":")[1].strip()

    return rotor1, rotor2, rotor3, reflector


def rotate():
    """Turn the first wheel after every keypress"""
    positions[0] = (positions[0] + 1) % 26
    if positions[0] == 0:
        positions[1] = (positions[1] + 1) % 26
        if positions[1] == 0:
            positions[2] = (positions[2] + 1) % 26


def encode_letter(letter):
    """Encode a single letter"""
    rotate()

    i = alphabet.index(letter)
    i = alphabet.index(rotor1[(i + positions[0]) % 26])
    i = alphabet.index(rotor2[(i + positions[1]) % 26])
    i = alphabet.index(rotor3[(i + positions[2]) % 26])
    letter = reflector[i]
    i = (rotor3.index(letter) - positions[2]) % 26
    letter = alphabet[i]
    i = (rotor2.index(letter) - positions[1]) % 26
    letter = alphabet[i]
    i = (rotor1.index(letter) - positions[0]) % 26
    letter = alphabet[i]
    return letter


# --- Main Program ---
filename = input("Insert config (filename): ")
rotor1, rotor2, rotor3, reflector = load_config(filename)

use_plugboard = input("Insert plugs (y/n)?: ").lower()
if use_plugboard == "y":
    print("Plugboard not implemented in this version.")
else:
    print("No extra plugs inserted.")

print("Enigma initialized.\n")

positions = [0, 0, 0]

while True:
    text = input("Insert row (empty stops): ").upper()
    if not text:
        print("Enigma closing.")
        break

    positions = [0, 0, 0]  # reset before each message
    result = ""

    for ch in text:
        if ch in alphabet:
            result += encode_letter(ch)

    print("Converted row -", result)

