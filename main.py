class Building:
    def __init__(self, material, color, number=0):
        self.material = material
        self.color = color
        self.number = number
        self.place = self._calculate_place()

    def _calculate_place(self):
        if self.number < 0:
            return "out of stock"
        elif 0 <= self.number < 100:
            return "warehouse"
        else:
            return "Remote warehouse"

    def plus(self, count):
        self.number += count
        self.place = self._calculate_place()

    def minus(self, count):
        self.number -= count
        self.place = self._calculate_place()

    @staticmethod
    def MarketFactory():
        white_brick = Building("white brick", "white", 100)
        brown_plank = Building("brown plank", "brown", 10)
        return [white_brick, brown_plank]

# Create objects using the MarketFactory
market_objects = Building.MarketFactory()

# Print the objects
for obj in market_objects:
    print(f"Material: {obj.material}, Color: {obj.color}, Number: {obj.number}, Place: {obj.place}")
