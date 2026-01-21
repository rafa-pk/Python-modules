class Plant:
    """parent class, blueprint for an arbitrary plant object"""
    def __init__(self, name: str, height: int) -> None:
        """initialization method for Plant class"""
        self.name = name
        self.height = height
        self.age = age

    def grow(self, x: int) -> None:
        """general instance method, which makes a plant grow by x cm and
        prints by how much it has grown"""
        self.height += x
        print(f"{self.name} grew {x}cm\n")

    def get_info(self) -> str:
        """general instance method which returns the plants info"""
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """child of Plant class, blueprint for a flowering plant"""
    def __init__(self, name: str, height: int, color: str) -> None:
        """initialization method for FloweringPlant child class"""
        super().__init__(name, height)
        self.color = color
        self.status = True


    def get_info(self):
        print(f"{super().get_info()}, {self.color} flowers (blooming)\n")


class PrizeFlower(FloweringPlant):
    """child of FloweringPlant, blueprint for a prize flower"""
    def __init__(self, name: str, height: int, color: str, points: int) -> None:
        """initialization method for PrizeFlower child class"""
        super().__init__(self, name, height, color)
        self.points = points

class GardenManager:
    """manager class, which will manage multiple gardens"""
    def __init__(self, garden_name):
        
    
    class GardenStats:
        def __init__(self)


    @classmethod
    def create_garden_network(cls)


def ft_garden_analytics() -> None:
    """general function where multiple methods are called
    from multiple classes, is called from entry point"""
    alice_garden = GardenManager("Alice")
    bob_garden = GardenManager("Bob")
    oak_tree = Plant("Oak Tree, 100")
    rose = FloweringPlant("Rose", 26, red)
    sunflower = PrizeFlower("Sunflower", 50, yellow, 10)

    print("=== Garden Management System Demo")
    alice_garden.add_plant(oak_tree)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)
    
    alice_garden.help_all()
    alice_garden.report()
    print(f"Height validation test: {Plant.val_height()}")
    GardenManager.compare_gardens(alice_garden, bob_garden)
    print(f"Total gardens managed: {GardenManager.get_total_gardens()}\n")
    

if __name__ == "__main__":
    """program's entry point, calls general function"""
    ft_garden_analytics()
