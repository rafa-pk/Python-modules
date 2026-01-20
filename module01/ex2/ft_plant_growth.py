class Plant:
    """Plant blueprint, class holding information about a plant object and
    methods that make it grow, age, or that print its characteristics"""    
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
    """initializer method, assigns plant characteristics to newly created object"""
    def grow(self) -> None:
        self.height += 1
    """method which makes plant object grow by 1 cm"""
    def older(self) -> None:
        self.age += 1
    """method which makes plant age by 1 day"""
    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"
    """method which prints plant characteristics to stdout"""


def ft_plant_growth(name: str, height: int, age: int, time: int) -> None:
    """function which takes characteristics and a timeframe, creates and initializes a plant
    object with the characteristics and makes them grow for that timeframe"""
    plant = Plant(name, height, age)

    print(f"=== Day 1 ===")
    print(plant.get_info())
    for _ in range(1, time):
        plant.grow()
        plant.older()
    print(f"=== Day {time} ===")
    print(plant.get_info())
    print(f"Growth this week: +{plant.height - height}cm")


def main() -> None:
    ft_plant_growth("Rose", 25, 30, 7)
    ft_plant_growth("Zoe", 174, 20, 7)


if __name__ == "__main__":
    main()
