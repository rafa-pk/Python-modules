class Plant:

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower:

    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
       print(f"{self.name} is blooming beautifully!") 


class Tree:

    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self.name} produces {2 * 3.14 ** ({trunk_diameter} / 10)}
              square meters")


class Vegetable:

    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


def ft_plant_types():

    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer harvest", "vitamin C")
    
    print("=== Garden Plant Types ===")
    print(f"")


