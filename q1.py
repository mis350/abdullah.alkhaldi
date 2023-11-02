class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def display(self):
        print("Product Name: ", self.name)
        print("Product Price: ", self.price)

    def discount(self, percent):
        self.price = self.price - (self.price * percent / 100)

# Do not change anything above this line
# add you code under this line