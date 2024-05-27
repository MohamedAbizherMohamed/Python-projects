import sys
import random

def randomcard():
    rank = random.randint(2, 14)

    rankstr = ["Jack", "Queen", "King", "Ace"]

    if rank == 11:
        rank = rankstr[0]
    elif rank == 12:
        rank = rankstr[1]
    elif rank == 13:
        rank = rankstr[2]
    elif rank == 14:
        rank = rankstr[3]
    else:
        rank
    
    suit = random.randint(1, 4)

    suitstr = ["Clubs", "Diamonds", "Hearts", "Spades"]

    suit = suitstr[suit - 1]
    
    return f"{rank} of {suit}"

def main():
    if len(sys.argv) != 1:
        print("Please dont input any values")
    
    card = randomcard()
    print(card)

if __name__ == "__main__":
    main()



    
