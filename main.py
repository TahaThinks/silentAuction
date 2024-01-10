import os
import art
#HINT: You can call clear() to clear the output in the console.
bidders = {}

def bid ():
    bidder_name = input(print("What is your name?: "))
    bidder_bid = int(input(print("What is your bid?: $ ")))
    bidders = {bidder_name : bidder_bid}


print(art.logo)
print("Welcome to the secret aution program")