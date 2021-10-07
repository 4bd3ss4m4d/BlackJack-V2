# Black Jack Game

from BlackJackASCIIArt import logo
import random


# Function that creates a deck of cards
def create_deck():
    deck = {
        'Ace of Spades': [11, 1], '2 of Spades': 2, '3 of Spades': 3, "4 of Spades": 4, '5 of Spades': 5,
        '6 of Spades': 6, '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9, '10 of Spades': 10,
        'Jack of Spades': 10, 'King of Spades': 10, 'Queen of Spades': 10,

        'Ace of Hearts': [11, 1], '2 of Hearts': 2, '3 of Hearts': 3, "4 of Hearts": 4, '5 of Hearts': 5,
        '6 of Hearts': 6, '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9, '10 of Hearts': 10,
        'Jack of Hearts': 10, 'King of Hearts': 10, 'Queen of Hearts': 10,

        'Ace of Clubs': [11, 1], '2 of Clubs': 2, '3 of Clubs': 3, "4 of Clubs": 4, '5 of Clubs': 5,
        '6 of Clubs': 6, '7 of Clubs': 7, '8 of Clubs': 8, '9 of Clubs': 9, '10 of Clubs': 10,
        'Jack of Clubs': 10, 'King of Clubs': 10, 'Queen of Clubs': 10,

        'Ace of Diamonds': [11, 1], '2 of Diamonds': 2, '3 of Diamonds': 3, "4 of Diamonds": 4, '5 of Diamonds': 5,
        '6 of Diamonds': 6, '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9, '10 of Diamonds': 10,
        'Jack of Diamonds': 10, 'King of Diamonds': 10, 'Queen of Diamonds': 10,
    }
    return deck
# Function that checks if the input is a number
def check_user_input(input):
    try:
        # Convert it into integer
        value = int(input)
        return True
    except ValueError:
        try:
            value = float(input)
            return True
        except ValueError:
            return False


# Function that checks whether there is a BlackJack!
def check_if_blackjack(deck, chosen_cards):
    score = 0
    for card in chosen_cards:
        # Check whether the value of the keys are list because only Aces contain a list as a value
        if type(deck[card]) == list:
            # Access the elements of the dictionary of Ace cards
            score += deck[card][0]
        else:
            score += deck[card]
    if score == 21:
        return True
    else:
        return False

# Get the score of cards
def get_score(deck, chosen_cards):
    # Check whether its a Blackjack!
    if len(chosen_cards) == 2 and check_if_blackjack(deck, chosen_cards):
        return 21
    #
    else:
        score = 0
        # Get the score of all kind of cards except Ace cards
        for card in chosen_cards:
            if type(deck[card]) != list:
                score += deck[card]

        # In case there are Ace cards, choose whether they will be equal to 1 or 11
        for card in chosen_cards:
            if type(deck[card]) == list:
                if (score + deck[card][0]) <= 21:
                    score += deck[card][0]
                else:
                    score += deck[card][1]
    return score


# Function that returns the game status and the winner
def check_winner(user_score, dealer_score, dealer_cards, user_cards, deck):
    # Check if Both of them got a BlackJack
    if (len(user_cards) == 2 and check_if_blackjack(deck, user_cards)) and (
            len(dealer_cards) == 2 and check_if_blackjack(deck, user_cards)):
        message = 'Its a Draw! Both you and the Dealer Got a blackJack! What a Coincidence!!'
        return message, 'Draw'
    # Check if the user got a BlackJack
    elif len(user_cards) == 2 and check_if_blackjack(deck, user_cards):
        message = "You've Got a BlackJack!! Congrats!"
        return message, 'User'
    # Check if the dealer got a Blackjack
    elif len(dealer_cards) == 2 and check_if_blackjack(deck, dealer_cards):
        message = "The Dealer Got a BlackJack!! You lost!"
        return message, 'Dealer'
    # In case both of them have a score <= 21
    elif user_score <= 21 and dealer_score <= 21:
        if user_score == dealer_score:
            message = "Its a Draw!"
            return message, 'Draw'
        elif user_score > dealer_score:
            message = "You've won! Congrats!"
            return message, 'User'
        elif user_score < dealer_score:
            message = "You've lost, the Dealer wins! Congrats to him!"
            return message, 'Dealer'
    # In case both of them have a score > 21
    elif user_score > 21 and dealer_score > 21:
        message = "You and the dealer both lost!"
        return message, 'Draw'
    # In case user has a score > 21 and the dealer has a score <= 21
    elif user_score > 21 and dealer_score <= 21:
        message = "The dealer wins! Congrats to him!"
        return message, "Dealer"
    # In case the user has a score <= 21 and the dealer has a score > 21
    elif user_score <= 21 and dealer_score > 21:
        message = "The dealer won! You lost!"
        return message, "Dealer"


def main():
    # Control the game
    status = 'yes'
    while status == 'yes':

        # Welcoming message and logo
        print("Welcome to the BlackJack Game!")
        print(logo)

        # Create a deck of cards
        deck = create_deck()
        cards = deck.copy()

        # Get user's bet input
        user_bet = input('Place your bet: $')
        # Check whether user bet is an int or an integer
        user_bet_status = check_user_input(user_bet)
        while user_bet_status == False:
            user_bet = input('Wrong input! Place your bet: $')
            user_bet_status = check_user_input(user_bet)

        # Choose two random cards for the user
        user_card1 = random.choice(list(cards))
        del cards[user_card1]
        user_card2 = random.choice(list(cards))
        del cards[user_card2]

        # Create a list containing user cards
        user_cards = [user_card1, user_card2]
        # Print the user_cards
        print(f'Your cards: [{user_card1}], [{user_card2}]')

        # Get the score of the two randomly selected cards of the user
        user_score = get_score(deck, user_cards)
        # Print user score
        print(f'Your score: {user_score}')

        # Choose two random cards for the user
        dealer_card1 = random.choice(list(cards))
        dealer_card2 = random.choice(list(cards))

        # Create a list containing dealer cards
        dealer_cards = []
        dealer_cards = [dealer_card1, dealer_card2]

        # Print the dealer cards
        print(f'Dealer cards: [{user_card1}], [X]')

        # Get the score of the two randomly selected cards of the user
        dealer_score = get_score(deck, dealer_cards)

        # Delete the two randomly selected cards from the deck of cards
        del cards[dealer_card1]
        del cards[dealer_card2]

        # Ask the user to hold or hit
        choice = input("\nType 'hold' to hold or 'hit' to take another card: ").lower()

        # In case the user types an invalid input
        while choice != 'hold' and choice != 'hit':
            choice = input("\nWrong input! Type 'hold' to hold or 'hit' to take another card: ").lower()

        while choice == 'hold' or 'hit':
            while user_score <= 21 and choice == 'hit':
                if choice == 'hit':
                    if len(cards) == 0:
                        print("There are no more cards left!")
                        break
                    # Get another card for the user
                    another_card = random.choice(list(cards))
                    user_cards.append(another_card)
                    del cards[another_card]

                    # Print user cards:
                    print('Your cards: ' + '[' + ' ,'.join(str(x) for x in user_cards) + ']')

                    # Print user score:
                    user_score = get_score(deck, user_cards)
                    print(f"Your score {user_score}")

                    # Decide dealer's move
                    if dealer_score < 17:
                        # Get another card for the user
                        another_card = random.choice(list(cards))
                        dealer_cards.append(another_card)
                        del cards[another_card]

                    # Create a list that only shows the dealer's first card
                    hidden_dealer_cards = []
                    for i in range(len(dealer_cards)):
                        if i == 0:
                            hidden_dealer_cards.append(dealer_cards[i])
                        else:
                            hidden_dealer_cards.append('X')
                    # Print only the dealer's first card
                    print('Dealer\'s cards: ' + '[' + ' ,'.join(str(x) for x in hidden_dealer_cards) + ']')
                    dealer_score = get_score(deck, dealer_cards)

                    # Ask the user to hold or hit
                    if user_score <= 21:
                        choice = input("\nType 'hold' to hold or 'hit' to take another card: ").lower()

                    # In case the user types an invalid input
                    while choice != 'hold' and choice != 'hit':
                        choice = input("\nWrong input! Type 'hold' to hold or 'hit' to take another card: ").lower()
            if choice == 'hold' or user_score > 21:
                # Call the check winner function to check the game status and the winner
                (game_result, winner) = check_winner(user_score, dealer_score, user_cards, dealer_cards, deck)
                print('\nYour cards: ' + '[' + ' ,'.join(str(x) for x in user_cards) + ']')
                print(f"Your score is : {user_score}")
                print('Dealer\'s cards: ' + '[' + ' ,'.join(str(x) for x in dealer_cards) + ']')
                print(f"Dealer's score is : {dealer_score}")
                print(game_result)

                # Prompt the user about his first bet
                if winner == "User":
                    print(f"Congrats! You've won ${user_bet * 2}. Enjoy!")
                elif winner == "Dealer":
                    print(f"Your ${user_bet} is gone! You should consider quitting gambling! It'll ruin your life.")
                else:
                    print(f"Your ${user_bet} will be returned to you.")
                break
            break

        # Prompt the user whether he wants to play again or quit
        status = input('\nWould you like to play again? Type \'yes\' to replay or \'no\' to quit: ').lower()

        while status != 'yes' and status != 'no':
            status = input('\nWrong input! Type \'yes\' to replay or \'no\' to quit: ').lower()


main()
