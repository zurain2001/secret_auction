from art import logo

secret_auction = True
print(logo)
print("Welcome to the secret auction. ")
print("The person with the highest bid will win.")


def clear():
    print("\n" * 50)

auction = {}
while secret_auction:

    name = input("What is your name? ")
    auction[name] = name
    bid = input("What is your bid? ")
    auction[name] = bid

    next_person = input("Is there another person who wants to bid? ").lower()

    if next_person == "yes":
        clear()
        print(logo)
        secret_auction = True
    elif next_person == "no":
        secret_auction = False

max_key = max(auction, key=auction.get)
max_bid = auction[max_key]

print(f"The highest bid is ${max_bid} by {max_key}.")
