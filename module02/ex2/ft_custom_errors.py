class GardenError(Exception):
    """main custom exception class, will signal an error about
    the whole garden"""
    pass


class PlantError(GardenError):
    """exception class for plants, inherits from garden exeption,
    will signal an error for plants"""
    pass


class WaterError(GardenError):
    """exception class for water, inherits from garden exception,
    will signal an exception about water"""
    pass


class Plant:
    """Plant blueprint which will be used to test error classes"""
    def __init__(self, name: str, wilting: bool, water_level: int) -> None:
        """initialization method for plant objects"""
        self.name = name
        self.wilting = wilting
        self.water_level = water_level

    def check_plant(self) -> None:
        """method to check if plant is wilting and raise error if it is"""
        if self.wilting:
            raise PlantError(f"The {self.name} plant is wilting!")

    def check_water(self) -> None:
        """method to check if water level is ok, raise error if not"""
        if self.water_level < 1:
            raise WaterError("Not enough water in the tank")


def ft_test_custom_types() -> None:
    """Testing function for the error classes created"""
    test_plant = Plant("Apple", True, 0)

    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        test_plant.check_plant()
    except (PlantError) as error_message:
        print(f"Caught PlantError: {error_message}\n")
    try:
        print("Testing WaterError...")
        test_plant.check_water()
    except (WaterError) as error_message:
        print(f"Caught WaterError: {error_message}\n")
    print("Testing catching all garden errors...")
    for check_errors in (test_plant.check_plant, test_plant.check_water):
        try:
            check_errors()
        except (GardenError) as error_message:
            print(f"Caught a garden error: {error_message}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    ft_test_custom_types()
