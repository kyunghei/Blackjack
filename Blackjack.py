import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if start_game == 'y':
    # total score of cards
    my_score = 0
    dealer_score = 0
    # list of drawn cards
    my_cards = []
    dealers_cards = []


    def draw_card(x):
        """draws one card"""
        if x == "user":
            my_cards.append(random.choice(cards))
        elif x == "dealer":
            dealers_cards.append(random.choice(cards))


    def sum_cards(x):
        if x == "user":
            my_total = 0
            for elements in my_cards:
                my_total += elements
            return my_total
        elif x == "dealer":
            dealer_total = 0
            for elements in dealers_cards:
                dealer_total += elements
            return dealer_total


    def current_score():
        print(f"\n   Your cards: {my_cards}, current score: {my_score}")
        print(f"   Computer's first card: {dealers_cards[0]}")


    def final_score():
        print(f"\n   Your final cards: {my_cards}, final score: {my_score}")
        print(f"   Computer's final cards: {dealers_cards}, final score: {dealer_score}")


    def determine_winner():
        if dealer_score > 21:
            print("You win! :D")
            exit()
        elif my_score > dealer_score:
            print("You win!")

        elif dealer_score > my_score:
            print("You lose!")


    # draw two cards & update score
    draw_card("user")
    draw_card("user")
    my_score = sum_cards("user")

    draw_card("dealer")
    draw_card("dealer")
    dealer_score = sum_cards("dealer")

    # check if user's score if over 21 & if there is an Ace.
    if my_score > 21:
        my_cards[0] = 1
        # update score with the 1.
        my_score = sum_cards("user")
    if dealer_score > 21:
        dealers_cards[0] = 1
        # udpate score with 1
        updated_score = 0
        dealer_score = sum_cards("dealer")
    elif my_score == 21 and dealer_score == 21:
        # check if user and dealer both got blackjack
        current_score()
        final_score()
        print("Draw. :/")
        exit()
    elif my_score == 21:
        # check if user got blackjack
        current_score()
        final_score()
        print("You win! :D")
        exit()
    elif dealer_score == 21:
        # check if dealer got blackjack
        current_score()
        final_score()
        print("You lose. );")
        exit()
    else:
        current_score()

        # ask if user wants to draw another card since <21.
    keep_playing = True
    while keep_playing == True:
        hit_or_hold = input("Type 'y' to get another card, type 'n' to pass: ")
        if hit_or_hold == 'n':
            while dealer_score < 17:
                draw_card("dealer")
                dealer_score = sum_cards("dealer")
            final_score()
            determine_winner()
            keep_playing = False
        elif hit_or_hold == 'y':
            draw_card("user")
            my_score = sum_cards("user")
            if my_score < 21:
                current_score()
            elif my_score == 21:
                final_score()
                print("You win!")
                keep_playing = False
            else:
                if 11 in my_cards:
                    position = my_cards.index(11)
                    my_cards[position] = 1
                    my_score = sum_cards("user")
                else:
                    final_score()
                    print("You lose.")
                    keep_playing = False


