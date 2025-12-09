class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


def ft_garden_data(name: str, height: int, age: int) -> None:

    plant = Plant(name, height, age)

    print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Resgistry ===")
    ft_garden_data("Rose", 25, 30)
    ft_garden_data("Sunflower", 80, 45)
    ft_garden_data("Cactus", 15, 120)
