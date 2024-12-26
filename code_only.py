import random

def getCardValue():
    return random.randint(2, 14)

def getCardStr(cardValue):
    if 2 <= cardValue <= 9:
        return str(cardValue)
    elif cardValue == 10:
        return "T"
    elif cardValue == 11:
        return "J"
    elif cardValue == 12:
        return "Q"
    elif cardValue == 13:
        return "K"
    elif cardValue == 14:
        return "A"

def getHLGuess():
    while True:
        guess = input("High or Low (H/L)?: ").strip().upper()
        if guess == "H":
            return "HIGH"
        elif guess == "L":
            return "LOW"

def getBetAmount(maximum):
    while True:
        try:
            bet = int(input(f"Input bet amount: "))
            if 1 <= bet <= maximum:
                return bet
            
        except ValueError:
            continue

def playerGuessCorrect(card1, card2, betType):
    if betType == "HIGH":
        return card1 < card2
    elif betType == "LOW":
        return card1 > card2

def main():
    print('''--- Welcome to High-Low ---
Start with 100 points. Each round a card will be drawn and shown.
Select whether you think the 2nd card will be Higher or Lower than the 1st card.
Then enter the amount you want to bet.
If you are right, you win the amount you bet, otherwise you lose.
Try to make it to 500 points within 10 tries.''')

    points = 100
    rounds = 0
    win_rounds = 0

    while 0 < points < 500 and rounds < 10:
        print("\n", end = "")
        print(37*"-")
        print(f"OVERALL POINTS: {points} ROUND {rounds + 1}/10")

        card1 = getCardValue()
        print(f"First card is a [{getCardStr(card1)}]")

        guess = getHLGuess()
        bet = getBetAmount(points)

        card2 = getCardValue()
        print(f"Second card is a [{getCardStr(card2)}]")

        if playerGuessCorrect(card1, card2, guess):
            points += bet
            win_rounds += 1
            print(f"Card1 [{getCardStr(card1)}] Card 2 [{getCardStr(card2)}] - You bet '{guess}' for {bet} - YOU WON")
        else:
            points -= bet
            print(f"Card1 [{getCardStr(card1)}] Card 2 [{getCardStr(card2)}] - You bet '{guess}' for {bet} - YOU LOST")

        rounds += 1


    if points >= 500:
        print("\n", end = "")
        print(16*"-","WIN",16*"-")
        print(f"YOU MADE IT TO *{points}* POINTS IN {rounds} ROUNDS!")
        print(37*"-")
        
    elif points <= 0:
        print("\n", end = "")
        print(16*"-","LOSE",16*"-")
        print(f"YOU HAVE *{points}* POINTS AFTER {rounds} ROUNDS!")
        
        if win_rounds > 1:
            print(f"BUT COULD WIN *{win_rounds}* ROUNDS AFTER {rounds} ROUNDS!")
        elif win_rounds == 1:
             print(f"YOU COULD WIN ONLY *1* ROUND AFTER {rounds} ROUNDS!")
        elif win_rounds == 0:
            print(f"YOU COULD NOT WIN AT LEAST A ROUND AFTER {rounds} ROUNDS!")

        print(37*"-")

    else:
        print("\n", end = "")
        print(16*"-","LOSE",16*"-")
        print(f"ONLY *{points}* POINTS IN {rounds} ROUNDS!")

        if win_rounds > 1:
            print(f"BUT COULD WIN *{win_rounds}* ROUNDS AFTER 10 ROUNDS!")
            
        elif win_rounds == 1:
            print(f"YOU COULD WIN ONLY *1* ROUND AFTER 10 ROUNDS!")
        
        elif win_rounds == 0:      
            print(f"YOU COULD NOT WIN AT LEAST A ROUND AFTER 10 ROUNDS!")
                  
        print(37*"-")


main()
