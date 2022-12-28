class Pakuri:
    #This creates inital stats of pakuri
    def __init__(self, species):
        self.species = species
        self.attack = (len(species) * 7) + 9
        self.defense = (len(species) * 5) + 17
        self.speed = (len(species) * 6) + 13

    # This retrieves the species of the pakuri entered
    def get_species(self):
        return self.species

    # This retrieves the attack of the pakuri entered
    def get_attack(self):
        return self.attack

    # This retrieves the defense of the pakuri entered
    def get_defense(self):
        return self.defense

    # This retrieves the speed of the pakuri entered
    def get_speed(self):
        return self.speed

    # This sets the new attack of the pakuri entered
    def set_attack(self, new_attack):
        self.attack = new_attack

    # This evolves the pakuri entered
    def evolve(self):
        self.attack = self.attack * 2
        self.defense = self.defense * 4
        self.speed = self.speed * 3

    # Developer function use to test the class
    def __str__(self):
        return f"Name:{self.species} - Attack:{self.attack} - Defense:{self.defense} - Speed:{self.speed}"




