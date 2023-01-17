from py_d9_blind_auction_logo import logo

print(logo)
print("Welcome to the Blind Bidding Auction")
flag = False
all_bids = {}
highest=0
highest_bidder_name=""

while flag == False:
    name = input("Enter name: ")
    bid = int(input("Enter bid value: $"))
    all_bids[name] = bid
    progress = input("Type 'yes' to enter another bid. Type 'no' to exit.\n").lower()
    if progress == 'no':
        flag = True

for item in all_bids:
    value = all_bids[item]
    if value > highest:
        highest = value
        highest_bidder_name = item

print(f"The highest bid is ${highest}. It was placed by {highest_bidder_name}.")
