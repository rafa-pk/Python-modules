class Plant:

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def created(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def ft_plant_factory():

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


def main():
    ft_plant_factory()


if __name__ == "__main__":
    main()
