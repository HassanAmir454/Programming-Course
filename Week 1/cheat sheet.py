Name = "Hassan"
print("Hello world", Name)
print("I am an interntional student in Finland")


#This is comment it is not shown  
#you can comment multiple line by click cntrl + / 

print("He said: \"Hello!\" and kept walking")    #escapt character \" \" for commas
print("He said: \"Hello!\"  \n and kept walking")    #escapt character \n for next line
# \n	Newline
# \t	Horizontal tab
# \r	Carriage return

name = input("Enter your name:")
print(f"Welcome {name}")

Sentence = "Find a substring"
print(Sentence)
print(Sentence[2]) #n
print(Sentence[-2]) #16-2=14 subtract -2 from total number of characters  n
print(Sentence[2:9]) # nd a su
print(Sentence[:9])  #Find a su
print(Sentence[-9:-2]) #16-9= 7  16-2=14  substri
print(Sentence[2:9:3]) # by gap of 3 nau
print(Sentence[::3]) # Fd brg
print(Sentence[::-1]) #gnirtsbus a dniF

exString = "Hello"
exInt = 2
exBool = True #or False
exFloat = 3.145

print(str(123) + str(456))

num1 = input("Enter frist number:")
num2 = input("Enter second number:")
print(num1 + num2)

print(int(num1) + int(num2))






#Using % formatting 
Name1 = "Hassan g"
Age = 20

Formatted = "My name is %s and I am %d years old" %(Name1, Age)
print(Formatted)

# %s = placeholder for a string
# %d = place holder for a integer

#Figure out what is the placeholder for float when using % formating

#Using format() method
Formatted2 = "My name is {0} and I am {1} year old.".format(Name, Age)
print(Formatted2)

RoundThis = 5.345353534
print("{:.2f}".format(RoundThis))