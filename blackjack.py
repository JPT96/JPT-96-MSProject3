import random
#card making process
class card:
    def __init__(self,value,suit):
        self.price = value
        self.value = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"][value -1]
        self.suit = "♥♦♠♣" [suit]
    
    def card (self):
        print('┌───────┐')
        print(f'| {self.value:<2}    |')
        print('|       |')
        print(f'|   {self.suit}   |')
        print('|       |')
        print(f'|    {self.value:>2} |')
        print('└───────┘') 
    
    def cost (self):
        if self.price >= 10 :
            return 10
        elif self.price == 1:
           return 11
        return self.price 
#deck making process
class deck:

    def __init__ (self):
        self.cards = []
        
    def full_deck(self):
        for i in range(1,14):
            for x in range(4):
                self.cards.append(card(i,x))

    def draw (self,iteration):
        cards = []
        for i in range(iteration):
            card = random.choice(self.cards)
            self.cards.remove(card)
            cards.append(card)

    def counter(self):
        return len(self.cards)

# player/dealer making process

class player_dealer:
    def __init__(self, dealer, deck):
        self.cards = []
        self.dealer = dealer
        self.deck = deck
        self.score = 0

    def hit(self):
        self.cards.extend(self.deck.draw(1))
        self.score_checker()
        if self.score > 21:
            return 1
        return 0

    def deal(self):
        self.cards.extend(self.deck.draw(2))
        self.score_checker()
        if self.score == 21:
            return 1
        return 0

    def score_checker(self):
        a_counter = 0
        self.score = 0
        for card in self.cards:
            if card.price() == 11:
                a_counter += 1
            self.score += card.price()

        while a_counter != 0 and self.score > 21:
            a_counter -= 1
            self.score -= 10
        return self.score

    def show(self):
        if self.dealer:
            print("Dealer's Cards")
        else:
            print("Player's Cards")

        for i in self.cards:
            i.show()

        print("Score: " + str(self.score))


class the_game():
    def __init__(self):
        self.deck = deck()
        self.deck.full_deck()
        self.dealer = player_dealer(True, self.deck)
        self.player = player_dealer(False, self.deck)
    
    def round(self):
        player_status = self.player.deal()
        dealer_status = self.dealer.deal()
        self.player.show()
        if player_status ==1:
            print("Player got Black Jack WOW!")
            if dealer_status ==1:
                print("IT'S A BLACK JACK DRAW!!!")
            return 1
        command = ""
        while command != "Hold":
            bust = 0
            command = input("Hit or Hold")
            

