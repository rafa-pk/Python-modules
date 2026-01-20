class Plant:
    """Plant blueprint, class holding plant objects,
    storing individual plant characteristics such as name, height or age"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Plant method to initialize a Plant object by
        passing the information it stores"""
        self.name = name
        self.height = height
        self.age = age


def ft_garden_data(name: str, height: int, age: int) -> None:
    """Function which creates and initializes a plant object and
    prints its characteristics"""
    plant = Plant(name, height, age)

    print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    ft_garden_data("Rose", 25, 30)
    ft_garden_data("Sunflower", 80, 45)
    ft_garden_data("Cactus", 15, 120)
