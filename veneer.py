class Marketplace:
    def __init__(self):
        self.listings = []

    def add_listing(self, listing):
        self.listings.append(listing)

    def remove_listing(self, listing):
        self.listings.remove(listing)

    def show_listings(self):
        for listing in self.listings:
            print(listing)


class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return f'{self.art.title}, {self.price}.'


class Art:
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return f'{self.artist}. "{self.title}". {self.year}, {self.medium}. {self.owner.name}, {self.owner.location}.'


class Client:
    def __init__(self, name, location, is_museum):
        self.name = name
        self.location = location
        self.is_museum = is_museum

    def sel_artwork(self, artwork, price):
        assert artwork.owner == self
        veneer.add_listing(Listing(artwork, price, self))

veneer = Marketplace()
print(veneer.show_listings())
edytta = Client('Edytta Halpirt', 'Private collection', False)
moma = Client('The MOMA', 'New York', True)
girl_with_mandolin = Art(
    'Picasso, Pablo', 'Girl with a Mandolin (Fanny Tellier)', 'oil on canvas', 1910, edytta)
print(girl_with_mandolin)
edytta.sel_artwork(girl_with_mandolin, '$6M (USD)')
print(veneer.show_listings())
