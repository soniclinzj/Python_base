# 1.1 一摞Python风格的纸牌

import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self.cards = [Card(rank, suit)
                      for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        return self.cards[position]


beer_card = Card('7', 'diamonds')

deck = FrenchDeck()

print(len(deck))

print(deck[0])

print(deck[-1])

print("1",choice(deck))
print("2",choice(deck))
print("3",choice(deck))
print("4",choice(deck))

print(deck[:3])
print(deck[12::13])

print("  ***  "*10)

for card in deck:
    print(card)

print(" ==== "*10)

for card in reversed(deck):
    print(card)

print(" ==== " * 10)

suit_values = dict(spades=3,hearts=2,diamonds=1,clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck,key=spades_high):
    print(card)