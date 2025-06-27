class Address:

    def __init__(self, index, cit, street, house, apart):
        self.index = index
        self.cit = cit
        self.street = street
        self.house = house
        self.apart = apart

    def __str__(self):
        return (f"{self.index}, {self.cit}, {self.street}, {self.house}, {self.apart}")
