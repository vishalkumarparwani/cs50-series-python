import random

cards = ["jack", "queen", "king"]

def main():
    # Use random.seed(0) for debugging 
    print(random.choices(cards, weights=[75, 20, 5], k=2))


main()