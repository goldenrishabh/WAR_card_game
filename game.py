# War card_game

# CLASSES
import random

player_user_war_cards = []
player_computer_war_cards = []

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
          "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}


class Cards:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + "of" + self.suit


class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                create_card = Cards(suit, rank)
                self.all_cards.append(create_card)

    def shuffle_deck(self):

        random.shuffle(self.all_cards)

    def choose_card(self):

        return self.all_cards.pop()


class Players:

    def __init__(self, name):

        self.name = name
        self.all_cards = []

    def remove_card(self):

        return self.all_cards.pop()

    def add_cards(self, cards):

        if type(cards) == type([]):
            self.all_cards.extend(cards)
        else:
            self.all_cards.append(cards)

    def __str__(self):

        return f"{self.name} has {len(self.all_cards)} cards"


player_name = input("What is your name ?")
player_user = Players(player_name)
player_computer = Players('computer')

game_deck = Deck()
game_deck.shuffle_deck()

for no in range(26):
    player_user.add_cards(game_deck.choose_card())
    player_computer.add_cards(game_deck.choose_card())


game_on = True
Round_no = 0


while game_on:

    if len(player_user.all_cards) == 0:

        game_on = False
        print("Computer has won!")
        break

    if len(player_computer.all_cards) == 0:

        game_on = False
        print(f"Congratulations {player_name} ! You have won ! This calls for a celebration")
        break

    Round_no += 1
    print(f"Round : {Round_no}")
    print("LET'S BEGIN")

    player_user_card = player_user.remove_card()
    player_computer_card = player_computer.remove_card()

    if player_user_card.rank > player_computer_card.rank:

        player_user.add_cards(player_computer_card)


    elif player_user_card.rank < player_computer_card.rank:

        player_computer.add_cards(player_user_card)


    elif player_user_card.rank == player_computer_card.rank:

        print("This means war ! !")
        war = True

        while war:
            for i in range(5):
                player_user_war_cards.append(player_user.remove_card())
                player_computer_war_cards.append(player_computer.remove_card())

            for i in range(5):
                if player_user_war_cards[-i].rank > player_computer_war_cards[-i].rank:
                    print(f"War of Round : {Round_no} is won by {player_name}")
                    for j in range(5):
                        player_user.add_cards(player_computer_war_cards.pop())
                        player_user.add_cards(player_user_war_cards.pop())
                    war = False
                    break
                if player_user_war_cards[-i].rank < player_computer_war_cards[-i].rank:
                    print(f"War of Round : {Round_no} is won by computer")
                    for j in range(5):
                        player_computer.add_cards(player_computer_war_cards.pop())
                        player_computer.add_cards(player_user_war_cards.pop())
                    war = False
                    break























