from pakudex import *

if __name__ == "__main__":
    print("Welcome to Pakudex: Tracker Extraordinaire!")

    #Prompts user to enter a correct capacity for the pakudex
    while True:
        try:
            MaxCap = int(input("Enter max capacity of the Pakudex: "))
            if MaxCap > 0:
                break
            else:
                raise  ValueError
        except ValueError:
            print("Please enter a valid size.")
    pakudex = Pakudex(MaxCap)
    print(f"The Pakudex can hold {MaxCap} species of Pakuri.")

    #variables used to store the list of species names in pakudex, and dictionnary to store stats of pakuri
    list = pakudex.pakuris
    dic = {}

    while True:
        #prints menu and propmts user to select a valid option from the menu
        Pakudex.menu()
        option = input("\nWhat would you like to do? ")
        try:
            option = int(option)
        except ValueError:
            print("Unrecognized menu selection!")
            continue

        #forces user to pic an option from 1 through 6
        if 1 <= option <= 6:
            #creates a list of pakuri currently in pakudex
            if option == 1:
                if len(list) != 0:
                    print("Pakuri In Pakudex: ")
                    for index, value in enumerate(list):
                        print(f"{str(index + 1)}. {list[index]}")
                else:
                    print("No Pakuri in Pakudex yet!")

            #shows the stats of a pakuri that is chosen by the user
            if option == 2:
                display = input("Enter the name of the species to display: ")
                if display in list:
                    print("")
                    print(f"Species: {display}")
                    print(f"Attack: {dic[display][0]}")
                    print(f"Defense: {dic[display][1]}")
                    print(f"Speed: {dic[display][2]}")
                else:
                    print("Error: No such Pakuri!")

            #adds a pakuri to the pakudex if the pakudex isn't full or the species entered isn't a repeat
            if option == 3:
                if int(pakudex.get_size()) > (int(pakudex.get_capacity()) - 1):
                    print("Error: Pakudex is full!")
                else:
                    NameOfSpecies = input("Enter the name of the species to add: ")
                    pakudex.add_pakuri(NameOfSpecies)
                    pakuri = Pakuri(NameOfSpecies)
                    dic[NameOfSpecies] = [pakuri.get_attack(), pakuri.get_defense(), pakuri.get_speed()]

            #evolves a pakuri which is chosen by the user
            if option == 4:
                EvolveWho = input("Enter the name of the species to evolve: ")
                if EvolveWho in list:
                    try:
                        pakudex.evolve_species(EvolveWho)
                        pakuri = Pakuri(EvolveWho)
                        pakuri.evolve()
                        dic[EvolveWho] = [pakuri.get_attack(), pakuri.get_defense(), pakuri.get_speed()]
                    except:
                        print("Error: No such Pakuri!")
                        print("tomato paste")
                        pass
                else:
                    print("Error: No such Pakuri!")

            #sorts the pakuri within the pakudex
            if option == 5:
                pakudex.sort_pakuri()
                print("Pakuri have been sorted!")

            #exits the program
            if option == 6:
                print("Thanks for using Pakudex! Bye!")
                break

        else:
            print("Unrecognized menu selection!")