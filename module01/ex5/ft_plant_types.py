class Plant:

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):

    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
       print(f"{self.name} is blooming beautifully!") 


class Tree(Plant):

    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        radius = self.trunk_diameter / 10
        print(f"{self.name} provides "
              f"{(3.14 * (radius ** 2)):.0f} square meters")


class Vegetable(Plant):

    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutritional_v(self):
        print(f"{self.name} is rich in {self.nutritional_value}")

 
def ft_plant_types():

    rose = Flower("Rose", 25, 30, "red")
    marguerite = Flower("Marguerite", 15, 10, "white")
    oak = Tree("Oak", 500, 1825, 50)
    bush = Tree("Bush", 100, 928383, 800)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    avocado = Vegetable("Avocado", 50, 80, "summer", "bons lipides")
    
    print("=== Garden Plant Types ===")
    print(f"\n{rose.name} ({rose.__class__.__name__}): {rose.height}cm, "
          f"{rose.age} days {rose.color} color")
    rose.bloom()
    print(f"\n{marguerite.name} ({marguerite.__class__.__name__}): "
        f"{marguerite.height}cm, {marguerite.age} days {marguerite.color} "
        f"color")
    marguerite.bloom()
    print(f"\n{oak.name} ({oak.__class__.__name__}): {oak.height}cm, {oak.age}"
          f" days, {oak.trunk_diameter}cm diameter")
    oak.produce_shade()
    print(f"\n{bush.name} ({bush.__class__.__name__}): {bush.height}cm, "
           f"{bush.age} days, {bush.trunk_diameter}cm diameter")
    bush.produce_shade()
    print(f"\n{tomato.name} ({tomato.__class__.__name__}): {tomato.height}cm,"
          f" {tomato.age} days, {tomato.harvest_season} harvest")
    tomato.nutritional_v()
    print(f"\n{avocado.name} ({avocado.__class__.__name__}): "
        f"{avocado.height}cm, {avocado.age} days, {avocado.harvest_season}"
        f" harvest")
    avocado.nutritional_v()


def main():
    ft_plant_types()


if __name__ == "__main__":
    main()
