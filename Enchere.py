from replit import clear
from logo_Enchere import logo

print(logo)

print("Welcom to the secret auction program.")

auction = {}
continue_bidder = False

def highest_auction(bidding_record):
  highest_bid = 0
  winner = ""
  for bidding in bidding_record:
    bid_amount = bidding_record[bidding]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidding
  print(f"The winner is {winner} with a bid of $ {highest_bid}.")
  

while not continue_bidder:
  name_first = input("What is your name? : ")
  bid_first = int(input("What's your bid? : $ "))
  auction[name_first] = bid_first
  final_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if final_bidder == "no":
    continue_bidder = True
    highest_auction(auction)
  elif final_bidder == "yes":
    clear()