class CoffeeShop:
    
    def __init__(self):
        self.customers = []

    def add_customer(self, name):
        if len(self.customers) >= 3:
            self.customers.append(name)
        else:
            pass

    def remove_customer_at(self, index):
        print("mewo")
        del self.customers[index]

    def get_customer_at(self, index):
        return self.customers[index]

    def get_num_customers(self):
        return len(self.customers)
