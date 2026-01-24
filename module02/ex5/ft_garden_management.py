class GardenError(Exception):
    """general garden error custom class"""
    pass


class PlantError(GardenError):
    """plant error custom class"""
    pass


class WaterError(GardenError):
    """water error custom class"""
    pass


class Plant:
    """general plant blueprint for garden"""
    def __init__(self, name: str, water_level: int, sun_expo: int) -> None:
        """general initialization method for plant objects"""
        self.name = name
        self.water_level = water_level
        self.sun_expo = sun_expo

    def validation_error(self) -> None:
        """instance method which raises validation errors"""
        if not self.name:
            raise PlantError("Plant name cannot be empty!")

    def watering_error(self) -> None:
        """instance method which raises watering error"""
        if self.water_level > 10:
            raise WaterError(f"Cannot water {self.name} - water "
                             f"level is too high (max 10)")

    def health_error(self) -> str | None:
        """instance method which raises general plant health errors or
        returns a success message"""
        if self.water_level < 1:
            raise WaterError(f"Water level {self.water_level} "
                             f"is too low (min 1)")
        elif self.water_level > 14:
            raise WaterError(f"Water level {self.water_level} "
                             f"is too high (max 10)")
        elif self.sun_expo < 2:
            raise PlantError(f"Sunlight hours {self.sun_expo} "
                             f"is too low (min 2)")
        elif self.sun_expo > 12:
            raise PlantError(f"Sunlight hours {self.sun_expo} "
                             f"is too high (max 12)")
        else:
            return (f"{self.name}: healthy (water: {self.water_level}, "
                    f"sun: {self.sun_expo})")

    def general_errors(self) -> None:
        """instance method to catch general garden errors"""
        if self.water_level < 1:
            raise GardenError("Not enough water in tank")
        elif self.water_level > 14:
            raise GardenError("Too much water in tank")
        elif self.sun_expo < 2:
            raise GardenError("Not enough sunlight hours")
        elif self.sun_expo > 12:
            raise GardenError("Too many sunlight hours")


class GardenManager:
    """main class which manages gardens"""
    def __init__(self) -> None:
        """initialization method for GardenManager"""
        self.garden_plants = []

    def add_plant(self, new_plant: Plant):
        """instance method to add plants to garden"""
        try:
            new_plant.validation_error()
            self.garden_plants.append(new_plant)
            print(f"Added {new_plant.name} successfully")
        except (PlantError) as message:
            print(f"Error adding plant: {message}")

    def water_plants(self) -> None:
        """instance method to water plants"""
        print("\nWatering plants...")
        print("Opening watering system")
        try:
            for plant in self.garden_plants:
                try:
                    plant.watering_error()
                    plant.water_level += 5
                    print(f"Watering {plant.name} - success")
                except (WaterError) as message:
                    print(f"Error: {message}")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self) -> None:
        """instance method to check plants health"""
        print("\nChecking plant health...")
        try:
            for plant in self.garden_plants:
                print(plant.health_error())
        except (PlantError, WaterError) as message:
            print(f"Error checking {plant.name}: {message}")

    def error_recovery(self) -> None:
        """instance method to check if any errors are triggered"""
        print("\nTesting error recovery...")
        try:
            for plant in self.garden_plants:
                plant.general_errors()
        except (GardenError) as message:
            print(f"Caught GardenError: {message}")
        finally:
            print("System recovered and continuing...")


def test_garden_management() -> None:
    """tester function for garden management"""
    garden = GardenManager()
    tomato = Plant("tomato", 0, 8)
    lettuce = Plant("lettuce", 10, 5)
    error_plant = Plant("", 5, 6)

    print("=== Garden Management System ===\n")
    print("Adding plants to garden...")
    garden.add_plant(tomato)
    garden.add_plant(lettuce)
    garden.add_plant(error_plant)
    garden.water_plants()
    garden.check_health()
    lettuce.water_level = 0
    garden.error_recovery()
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
