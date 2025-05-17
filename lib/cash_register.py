#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount = 0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.items += [title for _ in range(quantity)]
        self.last_transaction = price * quantity
        self.total += self.last_transaction
        
    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")    
            
    def void_last_transaction(self):
        self.total -= self.last_transaction
        pass
  
