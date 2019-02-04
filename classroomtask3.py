class Card(object):

	def __init__(self, rank =2,suit = 0):
		self.rank = rank
		self.suit = suit


	def __str__(self):
		return "%s of %s" %(Card.rank_names[self.rank], Card.suit_names[self.suit])


	suit_names = ["Clubs", "Diamond", "Hearts", "Spades"]
	rank_names = [None, "Ace","2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]



	def __lt__(self, other):
		t1 = (self.suit, self.rank)
		t2 = (other.suit, other.rank)
		return t1 < t2

card1 = Card(5,3)
card2 = Card(6,3)

print("1st card is :", card1)
print("2nd card is :", card2)

print("The 1st card is less than 2nd or not: ",card1.__lt__(card2))





class Deck(object):
	def __init__(self):
		self.cards = []
		for suit in range(0,4):
			for rank in range(1,14):
				card = Card(rank, suit)
				self.cards.append(card)

	def __str__(self):
		res = []

		for card in self.cards:
			res.append(str(card))

		return "\n".join(res)
