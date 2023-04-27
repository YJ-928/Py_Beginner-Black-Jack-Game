# NOTE:- -------- Our Blackjack House Rules ----------
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.


import os
from os import path
from art import logo
from time import sleep
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,]


def deal_card():
    """Returns a Random card from the deck of cards"""
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Returns the total sum of deck of cards given as input"""
    # BlackJack returns score of 0
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    else:
        return sum(cards)


def display_score(cards, score, computer):
    """Displays cards and current score for user/player
    and computer's/dealer's first card"""
    print(f"Your cards: {cards}, current score: {score}")
    return print(f"Computer's first card: {computer[0]}")


def compare_scores(user_score, computer_score):
    """Compares scores of user and
    computer and gives the final result"""
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    """Function to Play the game"""
    print(logo)

    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    display_score(cards=user_cards, score=user_score, computer=computer_cards)

    user_wants_to_deal = True

    while user_wants_to_deal:
        if input("\nType 'y' to get another card, type 'n' to pass: ") == 'y':
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            if user_score == 0 or computer_score == 0 or user_score > 21:
                user_wants_to_deal = False
        else:
            user_wants_to_deal = False

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(
        f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_scores(user_score, computer_score))


while input("\n\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    sleep(1)
    os.system('cls')
    play_game()
