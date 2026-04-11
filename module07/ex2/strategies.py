from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.capabilities import TransformCapability, HealCapability


class BattleStrategy(ABC):
    """Abstract base class implementation for battle strategies"""
    def __init__(self) -> None:
        """Initialization method for the BattleStrategy ABC"""
        super().__init__()

    @abstractmethod
    def act(self, creature: Creature) -> str:
        """act abstract method definition"""
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """is_valid abstract method definition"""
        pass


class NormalStrategy(BattleStrategy):
    """Abstract class inheriting from BattleStrategy"""
    def __init__(self) -> None:
        """Initialization method for NormalStrategy abstract class"""
        super().__init__()

    def act(self, creature: Creature) -> str:
        """act method for NormalStrategy"""
        print(creature.attack())
        return ""

    def is_valid(self, creature: Creature) -> bool:
        """is_valid method for NormalStrategy"""
        return True


class AggressiveStrategy(BattleStrategy):
    """Abstract class inheriting from BattleStrategy"""
    def __init__(self) -> None:
        """Initialization method for AggressiveStrategy abstract class"""
        super().__init__()

    def act(self, creature: Creature) -> str:
        """act method for AggressiveStrategy"""
        if not self.is_valid(creature):
            raise Exception(f"Invalid Creature '{creature.name}' "
                            f"for this aggressive strategy")
        print(creature.transform())  # type: ignore[attr-defined]
        print(creature.attack())
        print(creature.revert())  # type: ignore[attr-defined]
        return ""

    def is_valid(self, creature: Creature) -> bool:
        """is_valid method for AgressiveStrategy"""
        if isinstance(creature, TransformCapability):
            return True
        return False


class DefensiveStrategy(BattleStrategy):
    """Abstract class inheriting from DefensiveStrategy"""
    def __init__(self) -> None:
        """Initialization method for DefensiveStrategy"""
        super().__init__()

    def act(self, creature: Creature) -> str:
        """act method for DefensiveStrategy"""
        if not self.is_valid(creature):
            raise Exception(f"Invalid Creature '{creature.name}' "
                            f"for this defensive strategy")
        print(creature.attack())
        print(creature.heal(None))  # type: ignore[attr-defined]
        return ""

    def is_valid(self, creature: Creature) -> bool:
        """is_valid method for DefensiveStrategy"""
        if isinstance(creature, HealCapability):
            return True
        return False
