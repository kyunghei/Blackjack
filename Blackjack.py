import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

start_game = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")



def blackjack():
    if start_game == 'y':
        print( """
        .------.            _     _            _    _            _    
        |A_  _ |.          | |   | |          | |  (_)          | |   
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
        `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
              |  \/ K|                            _/ |                
              `------'                           |__/           
        """)
        # total score of cards
        my_score = 0
        dealer_score = 0
        # list of drawn cards
        my_cards = []
        dealers_cards = []

        def draw_card(x):
            x.append(random.choice(cards))

        def sum_cards(x):
            return sum(x)

        def current_score():
            print(f"\n   Your cards: {my_cards}, current score: {my_score}")
            print(f"   Computer's first card: {dealers_cards[0]}")

        def final_score():
            print(f"\n   Your final cards: {my_cards}, final score: {my_score}")
            print(f"   Computer's final cards: {dealers_cards}, final score: {dealer_score}\n")
            if my_score > 21:
                print("You lose!")
            elif dealer_score > 21:
                print("You win.")
            elif my_score > dealer_score:
                print("You win.")
            elif my_score == dealer_score:
                print("Draw.")
            else:
                print("You lose.")
            restart_game = input("Would you like to play another game of Blackjack? Type 'y' or 'n': " )
            if restart_game == "y":
                blackjack()
            elif restart_game == "n":
                print("Goodbye!")
                exit()
        # draw two cards & update score
        draw_card(my_cards)
        draw_card(my_cards)
        my_score = sum_cards(my_cards)

        draw_card(dealers_cards)
        draw_card(dealers_cards)
        dealer_score = sum_cards(dealers_cards)

        # check if user's score if over 21 & if there is an Ace.
        if my_score > 21:
            my_cards[0] = 1
            # update score with the 1.
            my_score = sum_cards(my_cards)
        if dealer_score > 21:
            dealers_cards[0] = 1
            # udpate score with the 1.
            dealer_score = sum_cards(dealers_cards)
        elif my_score == 21 and dealer_score == 21:
            # check if user and dealer both got blackjack
            current_score()
            final_score()
            print("Draw. :/")
        elif my_score == 21:
            # check if user got blackjack
            current_score()
            final_score()
            print("You win! :D")
        elif dealer_score == 21:
            # check if dealer got blackjack
            current_score()
            final_score()
            print("You lose. );")
        else:
            current_score()

            # ask if user wants to draw another card since <21.
        keep_playing = True
        while keep_playing == True:
            hit_or_hold = input("Type 'y' to get another card, type 'n' to pass: ")
            if hit_or_hold == 'n':
                while dealer_score < 17:
                    draw_card(dealers_cards)
                    dealer_score = sum_cards(dealers_cards)
                final_score()
                keep_playing = False
            elif hit_or_hold == 'y':
                draw_card(my_cards)
                my_score = sum_cards(my_cards)
                if my_score < 21:
                    current_score()
                elif my_score == 21:
                    final_score()
                    keep_playing = False
                else:
                    if 11 in my_cards:
                        position = my_cards.index(11)
                        my_cards[position] = 1
                        my_score = sum_cards(my_cards)
                    else:
                        final_score()
                        keep_playing = False


if start_game == "y":
    blackjack()
elif start_game == "n":
    print("Goodbye!")
else:
    print("You did not choose an available option.")