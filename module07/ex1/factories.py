from .creatures import Sproutling, Bloomelle, Shiftling, Morphagon
from ex0.factories import CreatureFactory
from ex0.creatures import Creature


class HealingCreatureFactory(CreatureFactory):
    """HealingCreatureFactory class, child to CreatureFactory"""
    def __init__(self) -> None:
        """Initialization method for HealingCreatureFactory abstract class"""
        super().__init__()

    def create_base(self) -> Creature:
        """Creates instance of base Healing Creature class"""
        return Sproutling("Sproutling", "Grass")

    def create_evolved(self) -> Creature:
        """Creates instance of advanced Healing Creature"""
        return Bloomelle("Bloomelle", "Grass/Fairy")


class TransformCreatureFactory(CreatureFactory):
    """TransformCreatureFactory class, child to CreatureFactory"""
    def __init__(self) -> None:
        """Initialization method for TransformCreatureFactory abstract class"""
        super().__init__()

    def create_base(self) -> Creature:
        """Creates instance of base Transform Creature class"""
        return Shiftling("Shiftling", "Normal")

    def create_evolved(self) -> Creature:
        """Creates instance of advanced Transform Creature class"""
        return Morphagon("Morphagon", "Normal/Dragon")
