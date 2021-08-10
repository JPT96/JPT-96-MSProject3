import random

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

        