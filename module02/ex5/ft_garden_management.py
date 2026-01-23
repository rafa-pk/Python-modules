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


class GardenManager:


def test_garden_management() -> None:
    """tester function for garden management"""
    garden = GardenManager()
    
    print("=== Garden Management System ===\n")
    print("Adding plants to garden...")
    garden.add_plant("tomato", 5, 6)
    garden.add_plant("lettuce", 6, 5)
    garden.add_plant("", 5, 6)

    
