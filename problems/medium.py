# Circular Buffer

class CircularBuffer:
    def __init__(self, size) -> None:
        self.size = size
        self.buffer = [ None
            for _ in range(size)
        ]
        self.oldest_idx = 0
        self.next_idx = 0

    def put(self, new_obj):
        self.buffer[self.next_idx] = new_obj
        self.increment_idx('next')
        if not self.has_opening(): # is full
            self.oldest_idx = self.next_idx

    def get(self):
        if self.buffer[self.oldest_idx] is not None:
            value = self.buffer[self.oldest_idx]
            self.buffer[self.oldest_idx] = None
            self.increment_idx('old')
            return value
        return None
    
    def increment_idx(self, type):
        if type == 'old':
            self.oldest_idx = (self.oldest_idx + 1) % self.size
        elif type == 'next':
            self.next_idx = (self.next_idx + 1) % self.size

    def has_opening(self):
        return any([obj == None for obj in self.buffer])

    # def info(self):
    #     print(f'{self.buffer = }')
    #     print(f'{self.next_idx = }')
    #     print(f'{self.oldest_idx = }')
        

buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True

# Number Guesser

import random
import os
class GuessingGame:
    
    def __init__(self) -> None:
        os.system('clear')
        pass
    
    def play(self):
        self.remaining_guesses = 7
        self.set_answer()

        while self.remaining_guesses > 0:
            self.display_guesses()
            self.get_guess()
            print(self.check_guess())
            print()
            if self.guess == self.answer:
                print('You won!')
                return
            self.remaining_guesses -= 1
        
        print('You have no more guesses. You lost!')
        return

    def set_answer(self):
        self.answer = random.randint(1, 100)
    
    def display_guesses(self):
        print(f'You have {self.remaining_guesses} guesses remaining.')
    
    def get_guess(self):
        prompt = 'Enter a number between 1 and 100: '
        while True:
            try:
                self.guess = int(input(prompt))
                return
            except:
                prompt = 'Invalid guess. Enter a number between 1 and 100: '
    
    def check_guess(self):
        if self.guess > self.answer:
            return 'Your guess is too high.'
        elif self.guess < self.answer:
            return 'Your guess is too low'
        else:
            return 'That\'s the number!'

game = GuessingGame()
game.play()
'''
You have 7 guesses remaining.
Enter a number between 1 and 100: 104
Invalid guess. Enter a number between 1 and 100: 50
Your guess is too low.

You have 6 guesses remaining.
Enter a number between 1 and 100: 75
Your guess is too low.

You have 5 guesses remaining.
Enter a number between 1 and 100: 85
Your guess is too high.

You have 4 guesses remaining.
Enter a number between 1 and 100: 0
Invalid guess. Enter a number between 1 and 100: 80
Your guess is too low.

You have 3 guesses remaining.
Enter a number between 1 and 100: 81
That's the number!

You won!

game.play()

You have 7 guesses remaining.
Enter a number between 1 and 100: 50
Your guess is too high.

You have 6 guesses remaining.
Enter a number between 1 and 100: 25
Your guess is too low.

You have 5 guesses remaining.
Enter a number between 1 and 100: 37
Your guess is too high.

You have 4 guesses remaining.
Enter a number between 1 and 100: 31
Your guess is too low.

You have 3 guesses remaining.
Enter a number between 1 and 100: 34
Your guess is too high.

You have 2 guesses remaining.
Enter a number between 1 and 100: 32
Your guess is too low.

You have 1 guess remaining.
Enter a number between 1 and 100: 32
Your guess is too low.

You have no more guesses. You lost!
'''

# number guesser 2

import random
import math

class GuessingGame:
    
    RESULT_OF_GUESS_MESSAGE = {
        'high':  "Your number is too high.",
        'low':   "Your number is too low.",
        'match': "That's the number!",
    }

    WIN_OR_LOSE = {
        'high':  'lose',
        'low':   'lose',
        'match': 'win',
    }

    RESULT_OF_GAME_MESSAGE = {
        'win':  "You won!",
        'lose': "You have no more guesses. You lost!",
    }

    def __init__(self, low, high):
        self.secret_number = None
        self.MAX_GUESSES = int(math.log2(high - low + 1)) + 1
        self.GUESSES_REMAINING = range(self.MAX_GUESSES, 0, -1)
        self.SECRET_RANGE = range(low, high + 1)

    def play(self):
        self.reset()
        game_result = self.play_game()
        self.show_game_end_message(game_result)

    def reset(self):
        self.secret_number = random.choice(self.SECRET_RANGE)

    def play_game(self):
        for remaining_guesses in self.GUESSES_REMAINING:
            self.show_guesses_remaining(remaining_guesses)
            result = self.check_guess(self.get_one_guess())
            print(self.RESULT_OF_GUESS_MESSAGE[result])
            if result == 'match':
                return self.WIN_OR_LOSE[result]

        return self.WIN_OR_LOSE[result]

    def show_guesses_remaining(self, remaining):
        print()
        if remaining == 1:
            print('You have 1 guess remaining.')
        else:
            print(f"You have {remaining} guesses remaining.")

    def get_one_guess(self):
        while True:
            prompt = ("Enter a number between "
                      f"{self.SECRET_RANGE[0]} and "
                      f"{self.SECRET_RANGE[-1]}: ")

            guess = input(prompt)
            if guess.isdigit():
                guess = int(guess)
                if guess in self.SECRET_RANGE:
                    return guess

            print("Invalid guess. ", end="")

    def check_guess(self, guess_value):
        if guess_value == self.secret_number:
            return 'match'
        elif guess_value < self.secret_number:
            return 'low'
        else:
            return 'high'

    def show_game_end_message(self, result):
        print("\n", self.RESULT_OF_GAME_MESSAGE[result])

game = GuessingGame(501, 1500)
game.play()






# --------------------------------
# Highest and lowest ranked cards
# ---------------------------------

class Card:
    CARD_RANK = {
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        'Jack': 11,
        'Queen': 12,
        'King': 13,
        'Ace': 14
    }

    def __init__(self, rank, suit) -> None:
        self.rank = rank
        self.value = self.CARD_RANK[rank]
        self.suit = suit

    def __lt__(self, other):
        return self.value < other.value
    
    def __le__(self, other):
        return self.value <= other.value
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __ne__(self, other):
        return self.value != other.value
    
    def __ge__(self, other):
        return self.value >= other.value
    
    def __gt__(self, other):
        return self.value > other.value

    def __str__(self):
        return f'{self.rank} of {self.suit}'


# tests

card = Card('Queen', 'Hearts')
card.rank

# tests
cards = [Card(2, 'Hearts'),
         Card(10, 'Diamonds'),
         Card('Ace', 'Clubs')]
print(min(cards) == Card(2, 'Hearts'))             # True
print(max(cards) == Card('Ace', 'Clubs'))          # True
print(str(min(cards)) == "2 of Hearts")            # True
print(str(max(cards)) == "Ace of Clubs")           # True

cards = [Card(5, 'Hearts')]
print(min(cards) == Card(5, 'Hearts'))             # True
print(max(cards) == Card(5, 'Hearts'))             # True
print(str(Card(5, 'Hearts')) == "5 of Hearts")     # True

cards = [Card(4, 'Hearts'),
         Card(4, 'Diamonds'),
         Card(10, 'Clubs')]
print(min(cards).rank == 4)                        # True
print(max(cards) == Card(10, 'Clubs'))             # True
print(str(Card(10, 'Clubs')) == "10 of Clubs")     # True

cards = [Card(7, 'Diamonds'),
         Card('Jack', 'Diamonds'),
         Card('Jack', 'Spades')]
print(min(cards) == Card(7, 'Diamonds'))           # True
print(max(cards).rank == 'Jack')                   # True
print(str(Card(7, 'Diamonds')) == "7 of Diamonds") # True

cards = [Card(8, 'Diamonds'),
         Card(8, 'Clubs'),
         Card(8, 'Spades')]
print(min(cards).rank == 8)                        # True
print(max(cards).rank == 8)                        # True


## 
# Cleaned cards
import random
class Card:
    VALUES = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    @property
    def value(self):
        return Card.VALUES.get(self.rank, self.rank)

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self) -> None:
        self.deal_cards()

    def deal_cards(self):
        self.cards = [Card(rank, suit) 
                            for rank in Deck.RANKS
                            for suit in Deck.SUITS]
        random.shuffle(self.cards)

    def draw(self):
        if self.cards:
            return self.cards.pop()
        else:
            self.deal_cards()
            return self.cards.pop()
    
    def __str__(self) -> str:
        card_strs = []
        for card in self.cards:
            card_strs.append(str(card))
        return "\n".join(card_strs)

# Tests

deck = Deck()
print(deck.cards[1])
print(deck)
drawn = []
for _ in range(52):
    drawn.append(deck.draw())

count_rank_5 = sum([1 for card in drawn if card.rank == 5])
count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

print(count_rank_5 == 4)      # True
print(count_hearts == 13)     # True

drawn2 = []
for _ in range(52):
    drawn2.append(deck.draw())

print(drawn != drawn2)        # True (Almost always).

#----------------
# Poker
#-----------------


from random import shuffle

class Card:
    VALUES = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    @property
    def value(self):
        return Card.VALUES.get(self.rank, self.rank)

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

class Deck:


    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self._reset()

    def draw(self):
        if not self._deck:
            self._reset()

        return self._deck.pop()

    def _reset(self):
        self._deck = [Card(rank, suit)
                      for rank in Deck.RANKS
                      for suit in Deck.SUITS]

        shuffle(self._deck)

class PokerHand:
    def __init__(self, deck):
        self._hand = [deck.draw() for _ in range(5)]

        self._hand.sort(key=lambda card: card.value) # = sorted([card for card in ], key=lambda card: card.value)
        
        self._vals = [card.value for card in self._hand]
        self._uniq_vals = set(self._vals)
        self._freq = [self._vals.count(val) for val in self._uniq_vals]

    def print(self):
        for card in self._hand:
            print(str(card))

    def evaluate(self):
        vals = [card.value for card in self._hand]
        uniq_vals = set(vals)
        freq = [vals.count(val) for val in uniq_vals]

        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"

    def _is_royal_flush(self):
       return self._hand[-1].value == 14 and self._is_straight_flush()

    def _is_straight_flush(self):
       return self._is_flush() and self._is_straight()

    def _is_four_of_a_kind(self):
       return ((max(self._freq) == 4) and (len(self._uniq_vals) == 2))

    def _is_full_house(self):
       return ((max(self._freq) == 3) and (len(self._uniq_vals) == 2))

    def _is_flush(self):
       suit = self._hand[0].suit 
       return all([self._hand[i].suit == suit for i in range(1,5)])

    def _is_straight(self):
       min_val = self._hand[0].value
       max_val = self._hand[-1].value
       diff = max_val - min_val

       return ((diff == 4) and len(self._uniq_vals) == 5)

    def _is_three_of_a_kind(self):
       return ((max(self._freq) == 3) and (len(self._uniq_vals) == 3))

    def _is_two_pair(self):
       return ((max(self._freq) == 2) and (len(self._uniq_vals) == 3))

    def _is_pair(self):
       return ((max(self._freq) == 2) and (len(self._uniq_vals) == 4))

# Testing
hand = PokerHand(Deck())
hand.print()
print(hand.evaluate())
print()

# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self._deck = cards

# All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")


