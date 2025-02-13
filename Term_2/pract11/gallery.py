
class Artwork():
    
    def __init__(self, name, artist, cost):
        self.name = name
        self.artist = artist
        self._cost = cost
    
    @property
    def cost(self):
        return self._cost
    
    def increase_cost(self, amount):
            if amount < 0:
                print("Only positive numbers!")
            else:
                self._cost += amount

class Exhibition():
    
    def __init__(self, name):
        self.name = name
        self.exhibition_art = []   
    
    def add_artwork(self, artwork):
        self.exhibition_art.append(artwork)

class Gallery():
    
    def __init__(self):
        self.exhibitions = {}

    def add_exhibitions(self):
        print("--- Add an Exhibitions ---")
        name = input("Name: ")
        new_exhibit = Exhibition(name)
        self.exhibitions[name] = new_exhibit
    
    def add_artwork(self):
        if not self.exhibitions:
            print("There is no exhibitions to add to.")
            return
        print("--- Add artwork ---")
        name = input("Name of art: ")
        artist = input("Artist: ")
        cost = float(input("Cost: "))
        artwork = Artwork(name,artist,cost)
        print("- Select Exhibition -")
        for exhibit in self.exhibitions:
            print(f"- {exhibit}")
        exhibit_choice = input("Exhibit chosen: ")
        select_exhibit = self.exhibitions.get(exhibit_choice)
        select_exhibit.add_artwork(artwork)

    def increase_cost(self):
        print("--- Increase Cost ---")
        for exhibit_name in self.exhibitions:
            print(f"- {exhibit_name}")

        exhibit_choice = input("Exhibit chosen: ")
        exhibit = self.exhibitions.get(exhibit_choice)
        for i, art in enumerate(exhibit.exhibition_art, 1):
            print(f"{i}. {art.name} by {art.artist}, £{art.cost}")
        art_choice = int(input("Select artwork number: ")) - 1
        increase_cost = float(input("Increase amount: "))
        exhibit.exhibition_art[art_choice].increase_cost(increase_cost)

        print(f"New cost: £{exhibit.exhibition_art[art_choice].cost}")

    def view(self):
        print("--- View Gallery ---")
        for exhibit_name, exhibit in self.exhibitions.items():
            total = 0
            print(f"Exhibition: {exhibit_name}")
            for art in exhibit.exhibition_art:
                print(f"    {art.name} by {art.artist}, £{art.cost}")
                total += art.cost
            print("Total for the Exhibition:", total)


def test_gallery():
    gallery = Gallery()

    gallery.add_exhibitions()
    gallery.add_artwork()
    gallery.view()

    gallery.increase_cost()

    gallery.view()

test_gallery()