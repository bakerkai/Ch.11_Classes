class Character():
    def __init__(self):
        self.name=""
        self.status=""
        self.strength = 0
        self.midichlorian_count = 0
        self.home = ""
    def fight(self):
        print("lightsaber on!, says " + self.name)

jedi1 = Character()

jedi1.name = "Obi Wan"
jedi1.status = "Jedi Master"
jedi1.strength = 100
jedi1.midichlorian_count = 20
jedi1.home = "Tatooine"

jedi2 = Character()

jedi2.name = "Yoda"
jedi2.status = "Jedi Master"
jedi2.strength = 200
jedi2.midichlorian_count = 50
jedi2.home = "Dagobah"

print("The first object created was " + jedi1.name)
print("The first object created was " + jedi2.name)

jedi1.fight()
jedi2.fight()

