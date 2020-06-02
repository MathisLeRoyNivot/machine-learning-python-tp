class Material:
    def __init__(self, name, mass, young_mod, poisson_ratio):
        self.name = name
        self.mass = mass
        self.young_mod = young_mod
        self.poisson_ratio = poisson_ratio


AVAILABLE_MATERIALS = [
    Material("Steel", 7850, 210, 0.27),
    Material("Aluminium", 2700, 62, 0.28),
    Material("Silver", 10500, 78, 0),
    Material("Concrete", 2350, 30, 0.2),
    Material("Wood", 800, 12, 0),
    Material("Bronze", 8740, 110, 0),
    Material("Copper", 8920, 128, 0.33),
    Material("Diamond", 3517, 1220, 0),
    Material("Iron", 7860, 208, 0.25),
    Material("Gold", 18900, 78, 0.42)
]