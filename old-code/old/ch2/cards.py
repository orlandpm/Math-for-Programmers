class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __eq__(self, other):
        return (self.suit == other.suit and self.rank == other.rank) #<1>
    def __hash__(self):
        return hash((self.suit, self.rank)) #<2>
    def __repr__(self):
        return ("%s of %ss" % (self.rank, self.suit))

suits = {"club", "diamond", "heart", "spade"}

ranks = {2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace"}

deck = { Card(suit,rank) for suit in suits for rank in ranks }

def is_flush(hand):
    hand_suits = {card.suit for card in hand} #<1>
    return (len(hand_suits) == 1)

ordered_ranks = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace"]

straight_lists = [ordered_ranks[i:i+5] for i in range(10)]

straight_set_list = [set(ordered_ranks[i:i+5]) for i in range(10)]

def is_straight(hand):
    hand_ranks = {card.rank for card in hand}
    return (hand_ranks in straight_set_list)

# straight_sets = {set(ordered_ranks[i:i+5]) for i in range(10)}

straight_set = {frozenset(ordered_ranks[i:i+5]) for i in range(10)}

{2,3,4,5,6} in straight_set
