# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

price={}
def clear_screen():
    print("\n" * 10)
while True:
    clear_screen()
    name=input("What is your name?:")
    bid=int(input("What is your bid?:$"))
    price[name]=bid
    text=input("Are there any other bidders?Type 'yes' or 'no'\n").lower()
    if text !='yes':
        break
# TODO-4: Compare bids in dictionary
highest_bid = max(price, key=price.get)
print(f"\nThe winner is {highest_bid} with a bid of ${price[highest_bid]}")



