
#Question 1

class Laptop:

    ram_options = {
        4: 0,
        8: 50,
        16: 100,
        32: 200
    }

    ssd_options = {
        256: 0,
        512: 30,
        1024: 100
    }

    def __init__(self, brand, base_price):
        self.brand = brand
        self.base_price = base_price
        self._ram = 4
        self._ssd = 256

    @property
    def ram(self):
        return self._ram

    @ram.setter
    def ram(self, new_ram):
        if new_ram in self.ram_options:  # Use class variable
            self._ram = new_ram

    @property
    def ssd(self):
        return self._ssd
    
    @ssd.setter
    def ssd(self, new_ssd):
        if new_ssd in self.ssd_options:
            self._ssd = new_ssd

    def calculate_price(self):
        ram_price = self.ram_options[self.ram]
        total_price = self.base_price + ram_price
        ssd_price = self.ssd_options[self.ssd]
        total_price = self.base_price + ssd_price
        return total_price

    def __str__(self):
        output = f"{self.brand} Laptop with {self.ram} GB RAM"
        output += f" priced at £{self.calculate_price()}"
        return output

def test_laptop():
    laptop = Laptop("Dell", 999.99)
    print(f"Laptop's brand is {laptop.brand}")
    print(f"Laptop's RAM is {laptop.ram} GB")
    print(f"Laptop's SSD is {laptop.ssd} GB")
    print(f"Laptop's price is £{laptop.calculate_price()}")
    laptop.ram = 99  # 'Laptop' has no attribute 'ram'
    print(f"Laptop's RAM is {laptop.ram} GB")
    laptop.ssd = 512
    print(f"Laptop's SSD is {laptop.ssd} GB")

    print(f"Laptop's price is £{laptop.calculate_price()}") # 999.99

    print(laptop)

#Question 2

