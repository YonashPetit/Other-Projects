#Import libraries, set initial True/False values, set variables
import p1_random
rng = p1_random.P1Random()
PlayerWins =0
DealerWins =0
TieGames =0
TotalGames = 0
GameContinue = True
GameNum = 0

#Overlying while loop which keeps the game going until the user chooses to exit
while GameContinue:
    #set up initail message abt game number
    GameNum += 1
    print("START GAME#",GameNum)
    print("")

    #reset variables at the begining of every new game
    player_hand = 0
    dealer_hand = 0

    #Deal a card to the player
    card = rng.next_int(13) +1
    if card == 1:
        print("Your card is a ACE!")
    elif 2<= card <= 10:
        print("Your card is a",card, end="!\n")
    elif card == 11:
        card = 10
        print("Your card is a JACK!")
    elif card == 12:
        card = 10
        print("Your card is a QUEEN!")
    elif card == 13:
        card = 10
        print("Your card is a KING!")
    player_hand += card

    #print hand value information
    print("Your hand is:", player_hand)
    print("")
    no_winners = True

    #While loop which constantly desplays the menu after every in game round, and contains Booleans which represent what choice the player chooses from the menu
    while no_winners:
        print("1. Get another card")
        print("2. Hold hand")
        print("3. Print statistics")
        print("4. Exit")
        print("")
        choice = int(input("Choose an option:"))


        #This choice represents the player drawing a card from ACE through KING
        if choice == 1:
            card = rng.next_int(13) + 1

            print("")
            if card == 1:
                print("Your card is a ACE!")
            elif 2 <= card <= 10:
                print("Your card is a", card, end="!\n")
            elif card == 11:
                card = 10
                print("Your card is a JACK!")
            elif card == 12:
                card = 10
                print("Your card is a QUEEN!")
            elif card == 13:
                card = 10
                print("Your card is a KING!")
            player_hand += card
            print("Your hand is:", player_hand)
            print("")

            #If the player's hand is above 21, they lose, if it's at 21 they win
            if player_hand == 21:
                print("BLACKJACK! You win!\n")
                PlayerWins += 1
                TotalGames += 1
                no_winners=False
            if player_hand > 21:
                print("You exceeded 21! You lose.\n")
                DealerWins += 1
                TotalGames += 1
                no_winners = False

        #This choice represents the player passing his turn and the dealer draws a card
        elif choice == 2:
            card = rng.next_int(11) + 16
            print("")
            dealer_hand += card
            print("Dealer's hand:", dealer_hand)
            print("Your hand is:", player_hand)
            print("")

            #if the dealer's hand is 21,the dealer wins; if it's above 21, the dealer loses; if the dealer's hand is equal to the player's hand, it's a tie
            #if the dealer's hand is less than the players hand, the player wins and VISE VERSA
            if dealer_hand == 21:
                print("Dealer wins!\n")
                DealerWins += 1
                TotalGames += 1
                no_winners = False
            elif dealer_hand > 21:
                print("You win!\n")
                PlayerWins += 1
                TotalGames += 1
                no_winners = False
            elif player_hand==dealer_hand:
                print("It's a tie! No one wins!\n")
                TieGames += 1
                TotalGames += 1
                no_winners = False
            elif player_hand < dealer_hand:
                print("Dealer wins!\n")
                DealerWins += 1
                TotalGames += 1

                no_winners = False
            elif player_hand > dealer_hand:
                print("You win!\n")
                TotalGames += 1
                PlayerWins += 1
                no_winners = False

        #this choice is just used to print out all of the past game statistics
        elif choice == 3:
            print("Number of Player wins:", PlayerWins)
            print("Number of Dealer wins:", DealerWins)
            print("Number of tie games:", TieGames)
            print("Total # of games played is:", TotalGames)
            ratio = float(PlayerWins)/float(TotalGames)
            PercentRatio = (100*ratio)
            print("Percentage of Player wins:", PercentRatio,end="%\n")
            print("")
            pass

        #This is the choice to exit playing the game
        elif choice == 4:
            no_winners = False
            GameContinue = False

        #This is what occurs when the user inputs an invalid choice that isn't on the menu
        else:
            print("Invalid input!\nPlease enter an integer value between 1 and 4.\n")
