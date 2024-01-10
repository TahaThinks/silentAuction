import os
import art
#HINT: You can call clear() to clear the output in the console.
bidders = {}

def bid ():
    bidder_name = input("What is your name?: ")
    bidder_bid = int(input("What is your bid?: $ "))
    bidders[bidder_name] = bidder_bid

def winner():
    winner_name = max(bidders, key=bidders.get)
    winner_bid = bidders[winner_name]
    print(f"{winner_name} is the winner bidding at ${winner_bid}")

print(art.logo)
print("Welcome to the secret aution program")

isBidActive = True

while isBidActive:
    bid()
    next = input("Are there any other bidders? Type 'yes' or 'no': ")
    if next == 'yes':
        os.system('cls')
    else:
      isBidActive = False
      winner()