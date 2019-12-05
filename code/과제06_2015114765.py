'''
파이썬 과제06
카드게임
'''

import random

card_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
card_suit = ["♠", "♥", "♣", "◆"]

player1 = [0, 0, 0]
player2 = [0, 0, 0]

card = [0 for x in range(52)]

def initialcard() :
    print("초기 카드 생성")
    for i in range(len(card_suit)) :
        for j in range(len(card_number)) :
            card[i*13 + j] = (card_suit[i], card_number[j])

            
def shufflecard() :
    print("Shuffle Card")
    random.shuffle(card)

    
def printcard() :
    for i in range(len(card)) :
        print(card[i],end = " ")
        if((i +1) % 13 == 0) :
            print("")


def dealing(player1, player2) :
    print("Dealing three cards")
    player1 = list(card[0:3])
    player2 = list(card[3:6])
    return player1, player2


def score(playercard) :
    playerscore = 0
    for i in range (3) :
        if(playercard[i][0] == "♠") :
            playerscore += 3 * playercard[i][1]
        elif(playercard[i][0] == "♥") :
            playerscore += 1 * playercard[i][1]
        elif(playercard[i][0] == "♣") :
            playerscore += 4 * playercard[i][1]
        elif(playercard[i][0] == "◆") :
            playerscore += 2 * playercard[i][1]

    return playerscore


def printresult(player1, player2) :
    score1, score2 = score(player1), score(player2)
    print("Player1: {0}, Player2: {1}".format(score1, score2))
    if(score1 > score2) :
        print("Player1 Win")
    elif (score1 == score2) :
        print("Draw")
    else :
        print("Player2 Win")
          

# main


initialcard()
printcard()


shufflecard()
printcard()


player1, player2 = dealing(player1, player2)
print("Player1: ", player1)
print("Player2: ", player2)
printresult(player1, player2)



