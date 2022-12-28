from pakuri import *

class Pakudex:
    #takes in the capacity the user wants and uses that to create an insance
    def __init__(self, capacity=20):
        self.pakuris = []
        self.capacity = capacity
        self.size = 0

    #gets the amount of pakuri in the pakudex
    def get_size(self):
        return self.size

    #gets the total capacity of pakuri in the pakudex
    def get_capacity(self):
        return self.capacity

    #gets a list of the names of the pakuri in the pakudex
    def get_species_array(self):
        if self.pakuris != []:
            return self.pakuris

    #gets the stats of a given pakuri within pakudex
    def get_stats(self, species):
        list = self.pakuris
        list2 = []

        if species in list:
            list2.append(Pakuri(species).get_attack())
            list2.append(Pakuri(species).get_defense())
            list2.append(Pakuri(species).get_speed())
        else:
            return None

        if list2 != []:
            return list2
        else:
            return None

    #sorts the pakuri in alphabeital order that are being stored in the pakudex
    def sort_pakuri(self):
        sorted_list = self.pakuris
        sorted_list.sort()
        return sorted_list

    #adds a pakuri into the pakudex
    def add_pakuri(self, species):
        list = self.pakuris

        # 1. check duplicates
        if species in self.pakuris:
            print("Error: Pakudex already contains this species!")
            return False
            pass
        # 2. when list is full, can't addy anything new
        if self.size > self.capacity - 1:
            print("Error: Pakudex is full!")
            return False
            pass
        else:
            pakuri = Pakuri(species)
            # dic[species] = [pakuri.get_attack, pakuri.get_defense, pakuri.get_speed]
            list.append(species)
            self.size += 1
            print(f"Pakuri species {species} successfully added!\n")
            return True

    #eveoles a selected pakuri (raises the chosens pakuri's stats)
    def evolve_species(self, species):
        if species in self.pakuris:
            Pakuri(species).evolve()
            print(f"{species} has evolved!")
            return True
        else:
            return False

    #method i used to make the menu
    @staticmethod
    def menu():
        print("\nPakudex Main Menu")
        print("-----------------")
        print("1. List Pakuri \n2. Show Pakuri \n3. Add Pakuri \n4. Evolve Pakuri \n5. Sort Pakuri \n6. Exit")



