class Plant:
    """Plant blueprint, class containing characteristics of a plant object
    and a method to display a newly created object's characteristics"""
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
    """method to initialize plant object with given characteristics"""
    def created(self) -> None:
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")
    """method to print characteristics of created object"""

def ft_plant_factory() -> None:
    """function which creates a list of Plant objects, tracks the number
    of instances created and prints all information"""
    creation_counter = 0

    plants = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
        ("zoe", 174, 20)
    ]
    print("=== Plant Factory Output ===")
    for name, height, age in plants:
        new_plant = Plant(name, height, age)
        new_plant.created()
        creation_counter += 1
    print(f"Total plants created: {creation_counter}")


def main() -> None:
    """main function, called in entry point"""
    ft_plant_factory()


if __name__ == "__main__":
    main()
