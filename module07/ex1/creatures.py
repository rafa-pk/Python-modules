from typing import Any
from ex0.creatures import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    """Sproutling abstract class, inheriting from creature and heal cap."""
    def __init__(self, name: str, type: str) -> None:
        """Initialization method for Sproutling class"""
        super().__init__(name, type)

    def attack(self) -> str:
        """Sproutling implementation of attack abstract method"""
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: Any) -> str:
        """Sproutling implementation of heal abstract method"""
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    """Bloomelle abstract class, inheriting from creature and heal cap."""
    def __init__(self, name: str, type: str) -> None:
        """Initialization method for Bloomelle class"""
        super().__init__(name, type)

    def attack(self) -> str:
        """Bloomelle implementation of attack abstract method"""
        return f"{self.name} uses Petal Dance!"

    def heal(self, target: Any) -> str:
        """Sproutling implementation of heal abstract method"""
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    """Shiftling abstract class, inherits from creature and transform cap."""
    def __init__(self, name: str, type: str) -> None:
        """Initialization method for Shiftling class"""
        super().__init__(name, type)
        self.state = "normal"

    def attack(self) -> str:
        """Shiftling implementation of attack abstract method"""
        if self.state == "transformed":
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        """Shiftling implementation of transform abstract method"""
        self.state = "transformed"
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        """Shiftling implementation of revert abstract method"""
        self.state = "normal"
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    """Morphagon abstract class, inheriting from creature and heal cap."""
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)
        self.state = "normal"

    def attack(self) -> str:
        """Morphagon implementation of attack abstract method"""
        if self.state == "transformed":
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        """Shiftling implementation of transform abstract method"""
        self.state = "transformed"
        return f"{self.name} shifts into a dragonic battle form!"

    def revert(self) -> str:
        """Shiftling implementation of revert abstract method"""
        self.state = "normal"
        return f"{self.name} stabilizes its form."
