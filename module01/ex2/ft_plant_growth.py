class Plant:
    
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    
    def grow(self):
        self.height += 1

    def older(self):
        self.age += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


def ft_plant_growth(name: str, height: int, age: int, time: int) -> None:

    plant = Plant(name, height, age)

    print(f"=== Day 1 ===")
    print(plant.get_info())
    for _ in range(1, time):
        plant.grow()
        plant.older()
    print(f"=== Day {time} ===")
    print(plant.get_info())
    print(f"Growth this week: +{plant.height - height}cm")


def main():
    ft_plant_growth("Rose", 25, 30, 7)
    ft_plant_growth("Zoe", 174, 20, 7)


if __name__ == "__main__":
    main()
