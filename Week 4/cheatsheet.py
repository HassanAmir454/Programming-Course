children = 3
Hometown = "Lahti"

TowninFinland = ["Lahti", "Tampere", "Laperantaa", "Oulu", "Helsinki"]

RandomInformation = ["Mira", 48, children, Hometown, True]

print(TowninFinland[0])
print(TowninFinland[-1])
print(TowninFinland[0])

TowninFinland.append("Rovaniemi")
print(TowninFinland)

Numoftown = len(TowninFinland)
print(TowninFinland)

print(TowninFinland[Numoftown-1])
print(TowninFinland[0])
print(TowninFinland[1])
print(TowninFinland[-1])

num = 3
print(TowninFinland[num])

Name = len("Mira")  #4
print(TowninFinland[Name])

Greetings = len("Hi") #2
print(TowninFinland[Greetings])

Num1 = 4
print(TowninFinland[Num1])

villages = ["Asikkala", "Hollola", "Karvia", "Kempele"]
Towns = ["Lahti", "Tampere", "Laperantaa", "Oulu", "Helsinki"]

villagesAndTowns = [villages, Towns]
print(villagesAndTowns[1][-2])    #result = Oulu [here frist[1] is showing Towns list if there is 0 means villages like frist []shows number of list and other showing the index of list 1]

Towns.sort()
print(Towns)


#Dictionary 

Teacher = {
    "name" : "Juha",
    "age" : 50,
    "city" : "Lahti"

}
print(Teacher['name'])
print(Teacher['age'])
print(Teacher['city'])
Teacher['city'] = 'Tampere'
print(Teacher)

empty = {}
empty['street'] = 'Mukkulankatu 19'
print(empty)

for key in Teacher:
    print(key)
    print(Teacher[key])

TownsAgain = ["Lahti", "Tampere", "Laperantaa", "Oulu", "Helsinki"]
for towns in TownsAgain:
    print(f"The town of {towns}")

for i in range(1, 10):
    print(i)

for i in range(1, 10):
    print(i, end="") #if we do not need new lines for each entry means you wana present in row

for i in range(1, 10, 3):
    print(i)

print("")

Total = 0 
for i in range(1, 101):
    Total += 1
    print(Total)
print(Total)

#For loop
#While loop
#break command in while loop
#continue command in while loop