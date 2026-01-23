class Plant:
    """parent class, blueprint for an arbitrary plant object"""
    def __init__(self, name: str, height: int) -> None:
        """initialization method for Plant class"""
        self.name = name
        self.height = height

    def grow(self, x: int) -> None:
        """general instance method, which makes a plant grow by x cm and
        prints by how much it has grown"""
        self.height += x
        print(f"{self.name} grew {x}cm")

    def get_info(self) -> str:
        """general instance method which returns the plants info"""
        return f"{self.name}: {self.height}cm"

    @staticmethod
    def val_height(height: int) -> str:
        """static method which validates or rejects height passed as arg"""
        if height > 0:
            return "True"


class FloweringPlant(Plant):
    """child of Plant class, blueprint for a flowering plant"""
    def __init__(self, name: str, height: int, color: str) -> None:
        """initialization method for FloweringPlant child class"""
        super().__init__(name, height)
        self.color = color
        self.status = True

    def get_info(self) -> str:
        """instance method which returns child info"""
        return f"{super().get_info()}, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """child of FloweringPlant, blueprint for a prize flower"""
    def __init__(self, name: str, height: int, color: str,
                 points: int) -> None:
        """initialization method for PrizeFlower child class"""
        super().__init__(name, height, color)
        self.points = points

    def get_info(self) -> str:
        """instance method which returns child info"""
        return f"{super().get_info()}, Prize points: {self.points}"


class GardenManager:
    """manager class, which will manage multiple gardens"""
    total_gardens = 0

    class GardenStats:
        """nested class to keep track of each garden's stats"""
        def __init__(self) -> None:
            """initialization method for tracking class"""
            self.total_plant_count = 0
            self.regular_count = 0
            self.flowering_count = 0
            self.prize_count = 0
            self.total_growth = 0
            self.garden_score = 0

        def track_new_plant(self, new_plant: Plant) -> None:
            """instance method to track addition of plant"""
            self.total_plant_count += 1
            if isinstance(new_plant, PrizeFlower):
                self.prize_count += 1
            elif isinstance(new_plant, FloweringPlant):
                self.flowering_count += 1
            else:
                self.regular_count += 1

        def track_growth(self) -> None:
            """instance method to track plant growth"""
            self.total_growth += 1

        def get_summary(self) -> str:
            """instance method which returns general stats"""
            return (f"Plants added: {self.total_plant_count}, Total growth: "
                    f"{self.total_growth}cm")

        def get_breakdown(self) -> str:
            """instance method which returns the gardens' plant breakdown"""
            return (f"Plant types: {self.regular_count} regular, "
                    f"{self.flowering_count} flowering, {self.prize_count} "
                    f"prize flowers")

    def __init__(self, garden_name: str) -> None:
        """initialization method for the Managing class"""
        self.garden_name = garden_name
        self.garden_plants = []
        self.garden_stats = GardenManager.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, new_plant: Plant) -> None:
        """instance method which adds new_plant to garden_plants and
        prints message"""
        self.garden_plants.append(new_plant)
        self.garden_stats.track_new_plant(new_plant)
        print(f"Added {new_plant.name} to {self.garden_name}'s garden")

    def help_all(self) -> None:
        """instance method to help all plants grow"""
        print(f"\n{self.garden_name} is helping all plants grow...")
        for plant in self.garden_plants:
            plant.grow(1)
            self.garden_stats.track_growth()

    def report(self) -> None:
        """instance method which generates a garden report"""
        print(f"\n=== {self.garden_name}'s Garden Report ===")
        print("Plants in garden:")
        for plants in self.garden_plants:
            print(f"- {plants.get_info()}")
        print(f"\n{self.garden_stats.get_summary()}")
        print(f"{self.garden_stats.get_breakdown()}")

    def calculate_score(self) -> int:
        """instance method to calculate score of garden"""
        score = 0
        for plant in self.garden_plants:
            score += plant.height
            if isinstance(plant, PrizeFlower):
                score += plant.points
        return score

    @classmethod
    def get_total_gardens(cls) -> int:
        """class method which returns the total number of managed gardens"""
        return cls.total_gardens

    @staticmethod
    def compare_gardens(garden1: "GardenManager",
                        garden2: "GardenManager") -> None:
        """static method which compares and prints two garden scores"""
        print(f"Garden Scores - {garden1.garden_name}: "
              f"{garden1.calculate_score()}, {garden2.garden_name}: "
              f"{garden2.calculate_score()}")

    @classmethod
    def create_garden_network(cls, owners:
                              list[str]) -> list["GardenManager"]:
        """class method which initializes a list of instances of
        GardenManager"""
        gardens = []
        for owner in owners:
            gardens.append(cls(owner))
        return gardens


def ft_garden_analytics() -> None:
    """general function where multiple methods are called
    from multiple classes, is called from entry point"""
    gardens = GardenManager.create_garden_network(["Alice", "Bob"])
    oak_tree = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 26, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    print("=== Garden Management System Demo ===\n")
    gardens[0].add_plant(oak_tree)
    gardens[0].add_plant(rose)
    gardens[0].add_plant(sunflower)

    gardens[0].help_all()
    gardens[0].report()
    print(f"\nHeight validation test: {Plant.val_height(oak_tree.height)}")
    GardenManager.compare_gardens(gardens[0], gardens[1])
    print(f"Total gardens managed: {GardenManager.get_total_gardens()}")


if __name__ == "__main__":
    """program's entry point, calls general function"""
    ft_garden_analytics()
