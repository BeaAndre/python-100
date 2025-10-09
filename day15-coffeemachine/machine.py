from coffee import Coffee

class Machine:
    def __init__(self, water = 200, milk = 200, beans = 200):
        self.resources = {'water': water,
                          'milk': milk,
                          'beans': beans
                          }
        self.balance = 0
    
    def report(self):
        print(f"Water: {self.resources['water']} ml")
        print(f"Milk: {self.resources['milk']} ml")
        print(f"Beans: {self.resources['beans']} g")
        
    def show_balance(self):
        print(f"Balance: €{self.balance / 100}")
        
    def has_enough_resources(self, ingredients):
        for resource, amount in ingredients.items():
            if(amount > self.resources.get(resource, 0)):
                print(f"Sorry, the machine doesn't have enough {resource}.")
                return False
        return True
            
    def make_coffee(self, coffee: Coffee): 
        ingredients = coffee.get_ingredients()
        
        if(self.has_enough_resources(ingredients)):
            for resource, amount in ingredients.items():
                self.resources[resource] -= amount
            
            self.balance += coffee.price()
            print(f"Here's your {coffee.name()}! Enjoy!")
            return True
        return False

    def refill(self):
        self.resources = {'water': 300,
                          'milk': 200,
                          'beans': 100}
        print("Refill successful!")