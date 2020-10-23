import collections

# Card = collections.namedtuple('Card', 'ranking suit')
# rankings = [str(index) for index in range(2, 11)] + list('JQKA')
# suits = {'spades': 3, 'hearts': 2, 'diamonds': 1, 'clubs': 0}
#
# french_deck = [
#     Card(single_ranking, single_suit) for single_suit in suits
#     for single_ranking in rankings
# ]
#
#
# def card_evaluation(single_card):
#     ranking_value = rankings.index(single_card.ranking) + 1
#     suit_value = suits[single_card.suit] * len(rankings)
#     return ranking_value + suit_value
#
#
# resulting_order = sorted(french_deck, key=card_evaluation, reverse=False)
# for single_card in resulting_order[12::13]:
#     print(single_card)
#

Card = collections.namedtuple('Card', 'ranking category')


class FrenchDeck(metaclass=type):
    rankings = [str(index) for index in range(2, 11)] + list('JQKA')
    categories = {'spades': 3, 'hearts': 2, 'diamonds': 1, 'clubs': 0}

    def __init__(self):
        self.french_deck = [
            Card(single_ranking, single_category)
            for single_category in FrenchDeck.categories.keys()
            for single_ranking in FrenchDeck.rankings
        ]

    def __getitem__(self, position):
        if position >= 1 and position <= 52:
            return self.french_deck[position - 1]
        else:
            print('The Card position not exist in the french deck')
            return None

    def sort(self, criteria=False):
        def card_evaluation(single_card):
            ranking_value = FrenchDeck.rankings.index(single_card.ranking) + 1
            category_value = FrenchDeck.categories[single_card.category] * len(
                FrenchDeck.rankings)
            return ranking_value + category_value

        return sorted(self.french_deck, key=card_evaluation, reverse=criteria)


my_deck = FrenchDeck()
for single_card in my_deck.sort()[12::13]:
    print('{:5}{:10}'.format(single_card.ranking, single_card.category))