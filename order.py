class Order:
    def __init__(self) -> None:
        self.items = {} #eta dictionary

    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity # jodi cart e already thaake
        else:
            self.items[item] = item.quantity # cart e na thakle
    
    def remove(self, item):
        if item in self.items:
            del self.items[item]

    @property
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())
    
    def clear(self):
        self.items = {}