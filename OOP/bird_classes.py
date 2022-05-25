class Bird:
    def __init__(self, species, colour, can_fly):
        self.species = species
        self.colour = colour
        self.wings = 2
        self.can_fly = can_fly
        self._age = 0

    def reproduce(self):
        if self._age < 2:
            return "Too young"
        else:
            return "Egg"

    def age_up(self):
        self._age += 1


# Instantiate an object
bird = Bird("Sparrow", "Brown", True)

# Calling methods

bird.age_up()
bird.age_up()
bird.age_up()
egg = bird.reproduce()

print(egg)


# Inheritance

class Penguin(Bird):
    def __init__(self, subspecies, colour=("Black", "White")):
        super().__init__("Penguin", colour, False)
        self.subspecies = subspecies

    def hunt_for_fish(self):
        print("Splash")

# penguin = Penguin("Rockhopper")

# print(Penguin.get_age())
# print(Penguin.hunt_for_fish())

class Royal(Penguin):
    def __init__(self, location, sex):
        self.location = location
        self.sex = sex
        super().__init__("Royal", "black and yellow")

    def hunt_method(self):
        return "In groups"


royal = Royal("East", "Female")
print(Royal)
print(royal.hunt_method())
print(royal.hunt_for_fish())



