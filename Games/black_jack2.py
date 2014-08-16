import random

class Deck:
    """
    The deck of cards
    """
    
    def __init__(self):
        suits = {'C','S','H','D'}
        cards = {2,3,4,5,6,7,8,9,10,'J','Q','K','A'}
        self.deck = [(suit, card) for suit in suits for card in cards]
        
    def __str__(self):
        return str(self.deck)
        
    def __len__(self):
        return len(self.deck)
        
    def deal_init_hands(self, player, dealer):
        
        # Pick 4 cards randomly from deck
        init_cards=[]
        for i in range(4):
            card = random.choice(self.deck)
            init_cards.append(card)
            self.deck.remove(card)
        
        # Deal first 2 to dealer
        dealer.add_card(init_cards[0])
        dealer.add_card(init_cards[1])
        
        # Deal second 2 to player
        player.add_card(init_cards[2])
        player.add_card(init_cards[3])
            

    def deck_deal_card(self):
        """
        Chooses a random card in deck, removes from deck, returns card
        """
        
        deal_card = random.choice(self.deck)
        self.deck.remove(deal_card)
        return deal_card
        
    

class Hand:
    """
    A hand in the game
    """

    def __init__(self):
        self.held_hand = []

    def __str__(self):
        return str(self.held_hand)

    def add_card(self, card):
        self.held_hand.append(card)

    # def score_hand(self):
        
    #     self.score = 0
        
    #     # find all permutations of cards with ace being 1 and 11
    #     # choose best score that is less than 21

        
    #     for card in self.held_hand:
    #         if type(card[1])==int:
    #             self.score+=card[1]
    #         elif card[1] == 'J' or card[1] == 'Q' or card[1] == 'K':
    #             self.score+=10
    #         elif card[1] == 'A':
    #             if self.score + 11 <= 21:
    #                 self.score+=11
    #             elif self.score + 11 > 21:
    #                 self.score+=1
        
    #     return self.score
    
    def score_hand(self):
        
        card_values = []
        num_aces = 0
        
        for card in self.held_hand:
            if type(card[1]) == int:
                card_values.append(card[1])
            elif card[1] == 'J' or card[1] == 'Q' or card[1] == 'K':
                card_values.append(10)
            elif card[1] == 'A':
                card_values.append(11)
                num_aces +=1
        
        
        if sum(card_values)<=21:
            return sum(card_values)
        elif sum(card_values)>21 and num_aces>2:
            return (sum(card_values)-10*(num_aces-1))
        else:
            return sum(card_values)
                
        
        
        # if self.score == 0:
        #     poss_scores = []
        #     for index in range(len(self.held_hand)):
        #         if type(self.held_hand[index])==int:
        #             poss_scores[index]+=self.held_hand[index]
        #         elif self.held_hand[index] == 'J' or self.held_hand[index] == 'Q' or self.held_hand[index] == 'K':
        #             poss_scores[index]+=10
        #         elif self.held_hand[index] == 'A':
        #             if poss_scores[index]+11<=21:
        #                 poss_scores[index]+=11
        #                 poss_scores[index+1]+=1
        #             elif poss_scores[index]+1<=21:
        #                 poss_scores[index]+1
                        
                
                
                
                
                

    def discard(self, card):
        self.held_hand.remove(card)

    def hit_me(self, deck):
        
        if self.score_hand() >= 21:
            print self.score_hand()
            print "Too bad!"
        else:
            self.add_card(deck.deck_deal_card())
    
    def stay(self):
        pass

    def split(self, card):
        pass
    
    def show_up_card(self):
        return self.held_hand[1]
        
    def show_deal_hand(self):
        return self.held_hand[1:]


def run_game():
    
	#create dealer and player hand and deck
	dealer = Hand()
	player = Hand()
	game_deck = Deck()
	
	#deal cards to dealer and player
	game_deck.deal_init_hands(player, dealer)
	
	#print dealer's hand
	print "Dealer's up card is ", dealer.show_up_card()
	#print "Dealer's full hand ", dealer
	
	#print player's hand
	print "Your hand is ", player
	
# 	print "player's score is ", player.score_hand()
# 	print "dealer's score is ", dealer.score_hand()
	
	#check for player's blackjack
	if player.score_hand() == 21:
	    return "Player has Blackjack!"
	
	if dealer.score_hand() == 21:
	    return "Dealer has Blackjack!"
	    
	#ask user for an action
	while player.score_hand() < 21 and dealer.score_hand() < 21:
	    
	    
	    action = raw_input("What do you want to do? Hit or Stay? ")
	    if action.lower() == "hit":
	        player.hit_me(game_deck)
	        print "After a hit, your hand is ", player
	        run_dealer(dealer, game_deck)
	        if player.score_hand() >=21:
	            print "You're finished and your score is ", player.score_hand()
	            print "Dealer's score is ", dealer.score_hand()
	            print win_round(dealer, player)
	    elif action.lower() == "stay":
	        run_dealer(dealer, game_deck)
	        print "You're done and your score is ", player.score_hand()
	        print "Dealer's score is ", dealer.score_hand()
	        print win_round(dealer, player)
	        break
	   
	   
def run_dealer(dealer, deck):
    # dealer hits a card if score < 13
    if dealer.score_hand() < 13:
        dealer.hit_me(deck)
        print "The dealer hit and his up hand is ", dealer.show_deal_hand()

def win_round(dealer, player):
    
    play_score = player.score_hand()
    deal_score = dealer.score_hand()
    
    if play_score<=21 and deal_score<=21:
        if deal_score >= play_score:
            return "Dealer wins hand"
        else:
            return "Player wins hand"
    elif deal_score<=21 and play_score>21:
        return "Dealer wins, you busted!"
    elif deal_score>21 and play_score>21:
        return "You both busted!"
    elif deal_score>21 and play_score<=21:
        return "Dealer busted, you win!"

def win_game():
    pass


run_game()


# player = Hand()
# player.add_card(('D','A'))
# player.add_card(('C','A'))
# player.add_card(('S','A'))
# print player
# print player.score_hand()