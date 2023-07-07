# Blind Auction program . . 
import os

# empty dictionary . .
bids = {}
biding_finished = False

# function for highest bidder . .
def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > str(highest_bid):
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with bid of ${highest_bid}")

# continue loop for auction . .
while not biding_finished:
    name = input("Enter your name : ")
    price = input("What is your bid : $")
    bids[name] = price
    should_continue = input("Are there any other bidders ? 'yes' or 'no' ")
    if should_continue == 'no':
        biding_finished = True
        highest_bidder(bids)
    elif should_continue == 'yes':
        os.system('cls') 