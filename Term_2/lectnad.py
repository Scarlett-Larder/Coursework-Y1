class SmartPlug:

    def __init__(self, consumtion_rate):
        if consumtion_rate > 150:

        self.switched_on = False
        self.consumtion_rate = consumtion_rate

    def toggle_switch(self):
         self.switched_on = not self.switched_on
    
    def __str__(self):
        print(f"SmartPlug is {self.switched_on} with a consumtion rate of {self.consumtion_rate}")