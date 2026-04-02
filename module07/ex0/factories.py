from abc import ABC, abstractmethod
from .creatures import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    """Creature Factory abstract base class"""
    def __init__(self) -> None:
        """Initialization method for the CreatureFactory Base Class"""
        super().__init__()

    @abstractmethod
    def create_base(self) -> Creature:
        """Abstract method declaration for create_base"""
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Abstract method declaration for create_evolved"""
        pass


class FlameFactory(CreatureFactory):
    """FlameFactory abstract class, inherits from CreatureFactory"""
    def __init__(self) -> None:
        """Initialization method for the FlameFactory Abstract Class"""
        super().__init__()

    def create_base(self) -> Creature:
        """Creates instance of base flame creature"""
        return Flameling("Flameling", "Fire")

    def create_evolved(self) -> Creature:
        """Creates instance of advanced flame creature"""
        return Pyrodon("Pyrodon", "Fire/Flying")


class AquaFactory(CreatureFactory):
    """AquaFactory abstract class, inherits from CreatureFactory"""
    def __init__(self) -> None:
        """Initialization method for the AquaFactory"""
        super().__init__()

    def create_base(self) -> Creature:
        """Creates instance of base aquatic creature"""
        return Aquabub("Aquabub", "Water")

    def create_evolved(self) -> Creature:
        """Creates instance of advanced aquatic creature"""
        return Torragon("Torragon", "Water")
