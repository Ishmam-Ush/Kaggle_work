# Working with external libraries
import math # standard library
print('This is Math {}'.format(type(math)))
print(dir(math))
print('This is pi to 5 digits = {:.5}'.format(math.pi))
print(math.log(32,2))
help(math.log)
# Shorter naming of imorts
import math as mt
print(mt.pi)

# Refering from modules by themselves
from math import *
print(pi, log(32,5))

import numpy 
print("this ia a {}".format(type(numpy)))
print("it contains...",
      dir(numpy.random)[-15:]
      )

# Roll Dice
rolls = numpy.random.randint(low= 1, high= 6, size= 10)
print(rolls)
print(rolls.mean)
print(rolls.tolist)
# print(help(rolls.mean))

# Operator Overloading
print(rolls + 10)
print(rolls<=3)
# examples
xl = [[1,2,3],[2,4,6],]
#Create a 2-dimensional array
x = numpy.asarray(xl)
print("xl= {}\nx = \n{}".format(xl,x))
# Tensorflow
import tensorflow as tf
# Create two constants, each with value 1
a = tf.constant(1)
b = tf.constant(1)
# Add them together to get...
a + b
print(a+b)


#from learntools.python import jimmy_slots
# Call the get_graph() function to get Jimmy's graph
#graph = jimmy_slots.get_graph()
#graph
#ex1
def prettify_graph(graph):
    """Modify the given graph according to Jimmy's requests: add a title, make the y-axis
    start at 0, label the y-axis. (And, if you're feeling ambitious, format the tick marks
    as dollar amounts using the "$" symbol.)
    """
    graph.set_title("Results of 500 slot machine pulls")
    # Complete steps 2 and 3 here
    graph.set_ylim(bottom=0)
    graph.set_xlim(left=0)
    graph.set_ylabel('Balanced')
#graph = jimmy_slots.get_graph()
#prettify_graph(graph)
#graph
#ex2

sample = [
    {'name': 'Peach', 'items': ['green shell', 'banana', 'green shell',], 'finish': 3},
    {'name': 'Bowser', 'items': ['green shell',], 'finish': 1},
    {'name': None, 'items': ['mushroom',], 'finish': 2},
    {'name': 'Toad', 'items': ['green shell', 'mushroom'], 'finish': 1},
]
#best_items(sample)

# Import luigi's full dataset of race data
#from learntools.python.luigi_analysis import full_dataset

# Fix me!
def best_items(racers):
    winner_item_counts = {}
    for i in range(len(racers)):
        # The i'th racer dictionary
        racer = racers[i]
        # We're only interested in racers who finished in first
        if racer['finish'] == 1:
            for _ in racer['items']:
                # Add one to the count for this item (adding it to the dict if necessary)
                if i not in winner_item_counts:
                    winner_item_counts[i] = 0
                winner_item_counts[i] += 1

        # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
        if racer['name'] is None:
            print(
                f"WARNING: Encountered racer with unknown name on iteration {i + 1}/{len(racers)} (racer = {racer['name']})"
            )
    return winner_item_counts

#Ex 3(Could'nt Solve myself)
def hand_total(hand):
    """Helper function to calculate the total points of a blackjack hand.
    """
    total = 0
    # Count the number of aces and deal with how to apply them at the end.
    aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            aces += 1
        else:
            # Convert number cards (e.g. '7') to ints
            total += int(card)
    # At this point, total is the sum of this hand's cards *not counting aces*.

    # Add aces, counting them as 1 for now. This is the smallest total we can make from this hand
    total += aces
    # "Upgrade" aces from 1 to 11 as long as it helps us get closer to 21
    # without busting
    while total <= 11 and aces > 0:
        # Upgrade an ace from 1 to 11
        total += 10
        aces -= 1
    return total

def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    total_1 = hand_total(hand_1)
    total_2 = hand_total(hand_2)
    return total_1 <= 21 and (total_1 > total_2 or total_2 > 21)