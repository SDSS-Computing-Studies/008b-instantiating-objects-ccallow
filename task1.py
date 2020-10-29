#!python3

"""
Create a class that will store a database for a veterinarian.
Your class will need the following properties:

animal (dog, cat, fish, bird, turtle, etc)
breed
name (the pet's name)
owner (the owner's name)
birthdate (of the pet, expressed as yyyy-mm-dd)

The constructor will need to ask for each of those values
for the database when the pet is instantiated

Methods:
display() - should show the name of the pet and type followed by their breed and owner


Main block should have a menu that has the following options:
1. Enter a new pet
2. Retrieve a pet
3. Exit

If they choose to retrieve a pet,
display the following:
Enter pet's name:
and then go through the list, looking for the name of the pet.
If the pet is found, it should call the display() method from the object

Example output:
1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Benjamin
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? dog
Breed? Shih-tzu
Name? Buster
Owner? Christy
Birthdate? 2008-10-16

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Casey
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
2

Which Pet? Buster

Buster dog
Shih-tzu is owned by Christy
(10 points) 
"""

class veterinarian:
    animalType = None
    breed = None
    name = None
    owner = None
    birthdate = None

    def __init__(self):
        self.animalType = input("Type of animal?  ")
        self.breed = input("Breed? ")
        self.name = input("Name? ")
        self.owner = input("Owner? ")
        self.birthdate = input("Birthdate? ")

    def displayPet(self):
        output = str(self.name) + str(self.animalType)
        output1 = str(self.breed) + "is owned by" + str(self.owner)
        print(output + "\n"+ output1)




def mainMenu():
    print("\n1. Enter a pet \n2. Retrieve a pet \n3. Exit \n")
    prompt = int(input())
    print("=====\n")
    return prompt

def options(prompt):
    if prompt == 1:
        pets.append(veterinarian())
    elif prompt ==2:
        name1 = input("Which pet? \n") 
        search(name1,pets)
    elif prompt == 3:
        print("Exiting the system...")
        break

def search(name1, pets):
    length = len(pets)
    for i in range(0,length):
        name = pets[i].name
        if name1 == name:
            pets[i].display()
           

 


pets = []
while True:
    command = mainMenu()
    options(command)
    
    