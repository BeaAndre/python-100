# from abc import ABC, abstractmethod

class Coffee:
    def name(self):
        pass
    
    def price(self):
        pass

    def get_ingredients(self):
        pass   


# Coffee types:
   
class Espresso(Coffee):
    def name(self):
        return "espresso"
    
    def price(self):
        return 150
    
    def get_ingredients(self):
        return {'water': 50, 'milk': 0, 'beans': 18}
    
    
class Latte(Coffee):
    def name(self):
        return "latte"
    
    def price(self):
        return 250
    
    def get_ingredients(self):
        return {'water': 200, 'milk': 150, 'beans': 24}
  
    
class Cappuccino(Coffee):
    def name(self):
        return "cappuccino"
    
    def price(self):
        return 300
    
    def get_ingredients(self):
        return {'water': 250, 'milk': 100, 'beans': 24}