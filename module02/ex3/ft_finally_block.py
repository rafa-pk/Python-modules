class InvalidPlant(Exception):
    """custom error class"""
    pass


class Plant:
    """plant class, blueprint for plant object"""
    def __init__(self, name) -> None:
        """initialization method for plant class"""
        self.name = name

    def check_name(self) -> None:
        """method which checks name and raises error if it is not valid"""
        if not self.name:
            raise InvalidPlant(f"Cannot water {self.name} - invalid plant!")


def water_plants(plant_list: list[Plant]) -> None:
    """function which opens a watering system and makes
    sure it is always closed"""
    success = True
    print("Opening watering system")
    try:
        for plant in plant_list:
            try:
                plant.check_name()
                print(f"Watering {plant.name}")
            except InvalidPlant as error:
                success = False
                print(f"Error: {error}")
    finally:
        print("Closing watering system (cleanup)")
    if success:
        print("Watering completed successfully!")


def test_watering_system() -> None:
    """testing function"""
    normal_watering = ["tomato", "lettuce", "carrots"]
    error_watering = ["tomato", None]
    new_plants = []

    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    for plant in normal_watering:
        new_plants.append(Plant(plant))
    water_plants(new_plants)
    print("\nTesting with error...")
    new_plants = []
    for plant in error_watering:
        new_plants.append(Plant(plant))
    water_plants(new_plants)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
