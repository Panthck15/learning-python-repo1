# Nouns: bag, dice, game
# Verbs: roll, draw, sum

import random
class Die:    
    def __init__(self, num_sides):        
        if num_sides > 20:            
            raise ValueError("You can't have more than a 20 sided die!")        
        if num_sides % 2 != 0:            
            raise ValueError("You can't have an odd-sided die")        
        self._num_sides = num_sides

    def roll(self):        
        return random.randint(1, self._num_sides)
    
class Bag:    
    def __init__(self, dice_dictionary):
        self.bag =[]
        for sides, count in dice_dictionary.items():
            for _ in range(count):
                self.bag.append(Die(num_sides=sides)) 
        #return self.bag = bag     

    def draw(self, num_things):
            drawn=[]
            for _ in range(num_things):
                random.shuffle(self.bag)
                popped=self.bag.pop()
                drawn.append(popped)
            return drawn

if __name__ == '__main__':    
            b = Bag({4:1, 6:2, 8:4, 10:2, 12:1, 20:3})    
            set_aside = b.draw(num_things=3)    
            drawn = b.draw(num_things=2)    
            s = sum([die.roll() for die in drawn])
            print("We drew {} ".format(s))
    #It has: 1d4, 2d6, 4d8, 2d10, 1d12, 3d20. 