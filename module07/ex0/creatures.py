from abc import ABC, abstractmethod


class Creature(ABC):
    """Abstract base class for future creatures"""
    def __init__(self, name: str, type: str) -> None:
        """Initialization method for abstract base class"""
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self) -> str:
        """Abstract method definition in base-class"""
        pass

    def describe(self) -> str:
        """Concrete generic method, common to every child-class"""
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):
    """Flameling abstract class, inherits from Creature base class"""
    def __init__(self, name: str, type: str) -> None:
        """Initialization method for Flameling class"""
        super().__init__(name, type)

    def attack(self) -> str:
        """Abstract method implementation in Flameling class"""
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    """Pyrodon abstract class, inherits from Creature base class"""
    def __init__(self, name: str, type: str) -> None:
        """Initialization method for Pyrodon class"""
        super().__init__(name, type)

    def attack(self) -> str:
        """Abstract method implementation in Pyrodon class"""
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):
    """Aquabub abstract class, inherits from Creature base class"""
    def __init__(self, name: str, type: str) -> None:
        """Initialization method for Aquabub class"""
        super().__init__(name, type)

    def attack(self) -> str:
        """Abstract method implementation in Aquabub class"""
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    """Aquabub abstract class, inherits from Creature base class"""
    def __init__(self, name: str, type: str) -> None:
        """Initialization method for Torragon class"""
        super().__init__(name, type)

    def attack(self) -> str:
        """Abstract method implementation in Torragon class"""
        return f"{self.name} uses Hydro Pump!"
