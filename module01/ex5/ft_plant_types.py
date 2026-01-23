class Plant:
    """Plant blueprint, parent class, defines plant object with
    base characteristics"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """initalization method, associates base characteristics
        to new object"""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Flower blueprint, inherits from Plant but adds a color
    characteristic"""
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """initalization method, associates characteristics of
        parent class and Flower class to object"""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """method which prints the name of a flower object
        blooming well"""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """Tree blueprint, inherits from Plant and adds a trunk
    diameter characteristic"""
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """initialization method, associates characteristics of
        parent class and Tree class to object"""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """method which calculates the area of produced shade by the Tree
        and prints it"""
        radius = self.trunk_diameter / 10
        print(f"{self.name} provides "
              f"{(3.14 * (radius ** 2)):.0f} square meters of shade")


class Vegetable(Plant):
    """Vegetable blueprint, inherits from Plan and adds harvest season
    and nutritional value characteristics"""
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        """initalizer method, associates characteristics of parent class and
        Vegetable method to object"""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutritional_v(self) -> None:
        """method which prints nutritional value to stdout"""
        print(f"{self.name} is rich in {self.nutritional_value}")


def ft_plant_types() -> None:
    """function which initializes instances of multiple objects
    inheriting from Plant and prints their characteristics"""
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
    """main function, called in entry point"""
    ft_plant_types()


if __name__ == "__main__":
    main()
