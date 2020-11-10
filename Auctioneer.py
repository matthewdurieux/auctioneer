from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
clear()
print(art.logo)
outstandingBids = True
bidList = {}
def add_new_bid(bidderName, bidAmount):
    bidList[bidderName] = int(bidAmount)

while outstandingBids == True:
    add_new_bid(bidderName = input("What is your name? "), bidAmount = int(input("What is your bid? $")))
    #print(bidList[bidderName])
    if input("More Bids? (yes / no) ") == "no":
        outstandingBids = False
    else:
        clear()
        
highestBid = 0
winningBidder = ''
for bids in bidList:
    bidAmount = bidList[bids]
    bidder = bids
    #print(bidder)
    if bidAmount > highestBid:
        highestBid = bidAmount
        winningBidder = bidder
clear()
print(f"The winner is {winningBidder} with a bid of {highestBid}")
