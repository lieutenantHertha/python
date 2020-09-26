import collections
import random

# Specify what kind of a poker card looks like
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:

    ranks = [str(number) for number in range(2, 11)] +list('JQKA')
    suits = 'hearts spades clubs diamonds'.split()
    suits_value = {'spades':3, 'hearts':2, 'diamonds':1, 'clubs':0}

    def __init__(self):
        self.cards = [Card(single_rank, single_suit) for single_suit in FrenchDeck.suits for single_rank in FrenchDeck.ranks]
    
    def __len__(self):
        return len(self.cards)
    
    def __getitem__(self, position):
        return self.cards[position]

# Set the criterion for sorting those poker cards in order concerning different suits.
def spades_high(poker_card):
    real_position = FrenchDeck.suits_value[poker_card.suit] * len(FrenchDeck.ranks) + FrenchDeck.ranks.index(poker_card.rank)
    return real_position

deck_in_order = sorted(FrenchDeck(), key=spades_high, reverse=True)
poker_set = [random.choice(deck_in_order) for index in range(3)]

for single_card in poker_set:
    print('RANK {}\tSUIT {}'.format(single_card.rank, single_card.suit.upper()))

