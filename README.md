
# Python Poker Challenge TC


# List of Files

poker.py. The main file where all base functions are defined
## Models
1) Card Class 
2) Deck class
3) Player Class

## Services
1) Hand_evaluator_service -> Honestly, the main bulk of the functionality exists here. It's where we do all of the various calculations to calculate a poker hands value

## Tests
 a folder with various testing files for all of our different files above!

# Design
In order to decipher a poker hand, there are basically 3 things we need to know. 
1) Is it a Flush?
2) Is it a straight
3) Are there any repeating numbers (4 of a kind, 2 pair, etc)

From there, we can make a series of if statements that check these various factors to see which of the 10 hands it corresponds to.

###

To break tie-breakers, I added additional fractional rankings to the main whole-number rank. 

For example, if two flushes have a rank of 5, we need to find the high card of each hand. a Ace high card will represent a higher fractional percentage than a 6 high card so the new rankings will be 5.88 for the Ace and 5.22 for the 6 high. While these specific numbers dont mean much it allows us to assign a relative value to rank these numbers within a hand.

# Function Descriptions
All function descriptions can be found in the docStrings of their respective functions!

