from random import shuffle

# Create a Deck of Cards class.
# Internally, the deck of cards should use another class, a Card class.
# Your requirements are:
# •   The Deck class should have a deal method to deal a single card from the deck.
#     After a card is dealt, it is removed from the deck.
# •   There should be a shuffle method which makes sure the deck of cards has all 52 cards and
#     then rearranges them randomly.
# •   The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K).
# Hint: Use the random.shuffle(list) function to randomly reorganize items inside a list.


class Card:
    def __init__(self, suit, value) -> None:
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.value + ' ' + self.suit


class Deck:
    values = ('A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K')
    suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')

    def __init__(self):
        self.deck = [Card(suit, value if type(value) == 'string' else str(value))
                     for suit in self.suits for value in self.values]
        self.shuff()
        self.removed = []

    def deal(self, card_n):
        if card_n < 52:
            self.removed.append(self.deck[card_n])
            self.deck[card_n: card_n + 1] = []
            self.shuff()
        else:
            print('not enough cards')
        pass

    def shuff(self):
        shuffle(self.deck)


deck = Deck()
for c in deck.deck:
    print(c)
print('----------------------')
deck.deal(1)
for c in deck.deck:
    print(c)
print('removed')
for c in deck.removed:
    print(c)
