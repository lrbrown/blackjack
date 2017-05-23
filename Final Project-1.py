#Author: Lauren Brown
#Assignment: Final Project
#Date: 9 May 2016
#Description: User vs Computer game of Blackjack
import random
import itertools


def deal(DECK):
        return random.sample(DECK, 1)

#assign value to any J, Q, K, A
def facecard(i):
        
        if i == 'Jack':
                i = 10
        elif i == 'Queen':
                i = 10
        elif i == 'King':
                i = 10
        elif i == 'Ace':
                i = 11
        else:
                i = int(i)
                
        return i

#change face cards and strings to numeric and add up total
def evaluateValue(CARDS):

        #strip values to only numeric values
        total = 0
        for x in CARDS:
                #remove suit symbol
                x = x[:-2]
                #Convert card from list object to string
                x = ''.join(x)
                #if facecard, convert to numeric value
                value = facecard(x)
                #add up total of cards
                total += value           
        return total

#compute what to do next for player
def checkValue(totalValue, CARDS):
        if totalValue == 21:
                print('You got BLACKJACK!')
                totalValue = 21

        elif totalValue > 21:
                print('You BUST!')
                        
        #if not a bust or blackjack, ask if they want to hit again
        elif totalValue < 21:
                totalValue = input ('Do you want to hit again? Hit = "H"')
                      
        return totalValue

#compute what to do next for dealer
def checkDealerValue(totalDealerValue, DEALER):

        if totalDealerValue == 21:
                print('Dealer got BLACKJACK')
                totalDealerValue = 21
        #check if there's an ace that can converted to a 1
        elif totalDealerValue > 21:
                print('Dealer BUSTED')
                
        return totalDealerValue


#create a list of suits and facess
SUITS = [ '♣', '♦', '♥', '♠']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

#combine suits and faces and use itertools to generate each card
DECK = tuple(' '.join(x) for x in itertools.product(RANKS, SUITS))

global CARDS
global DEALER

#delve out a random set of cards to you and one for the dealer to show
CARDS = deal(DECK)+ deal(DECK)
DEALER = deal(DECK)
print('Your hand:', CARDS)
#calculate numeric value of your hand
score = evaluateValue(CARDS)
print (score)
#reveal dealers first card
print('The dealer shows:', DEALER)

#determine if blackjack, bust or still in play
playerResult = checkValue(score, CARDS)

#while still in play & player wants to hit, deal new card
while playerResult == 'H':
        #deal another card
        newCard = deal(DECK)
        print('Your new card', newCard)
        #display full deck
        print(CARDS + newCard)
        CARDS = CARDS + newCard
        #convert cards to numeric value
        score = evaluateValue(CARDS)
        print(score)
        #determine if it's blackjack, bust or if player wants to hit again
        playerResult = checkValue(score, CARDS)

#after player is no longer in play
#deal dealer's second card
DEALER2 = deal(DECK)
print ("The dealer's hand", DEALER + DEALER2)
DEALER = DEALER + DEALER2
#compute numeric value of hand
totalDealerValue = evaluateValue(DEALER)
#determine if it's blackjack, bust, or if dealer must hit
dealerResult = checkDealerValue(totalDealerValue, DEALER)
#dealer must continue hitting if total hand < 17
while totalDealerValue < 17:
        newDealerCard = deal(DECK)
        print("Dealer drew", newDealerCard)
        #add new card to preexisting hand
        DEALER = DEALER + newDealerCard
        print('Added',newDealerCard)
        print (DEALER)
        #convert new hand to numeric value
        totalDealerValue = evaluateValue(DEALER)
        #determine if you need to continue hitting
        dealerResult = checkDealerValue(totalDealerValue, DEALER)
        print(totalDealerValue)
        


#check Dealer hands against players to print outcome
if dealerResult == score:
        print('TIE GAME')
elif dealerResult > 21 and score < 21 :
        print ('CONGRATULATIONS! You win!')
elif dealerResult > 21 and score > 21:
        print ('NO WINNER')
elif dealerResult == 21 and score != 21:
        print ('DEALER wins')
elif dealerResult == 21 and score == 21:
        print ('TIE GAME')
elif dealerResult != 21 and score == 21:
        print ('CONGRATULATIONS! You win!')
elif dealerResult < score and score < 21:
        print ('CONGRATULATIONS! You win!')
else:
        print('DEALER wins')
  


        
        
        

        
