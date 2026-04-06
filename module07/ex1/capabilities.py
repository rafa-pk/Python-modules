from abc import ABC, abstractmethod


class HealCapability(ABC):
    """Abstract Base Class for the Healing Capability"""
    def __init__(self) -> None:
        """Initialization method for HealCapability ABC"""
        super().__init__()

    @abstractmethod
    def heal(self, target) -> str:
        """Healing abstract method"""
        pass


class TransformCapability(ABC):
    """Abstract Base Class for the Transform Capability"""
    def __init__(self) -> None:
        """Initialization method for TransformCapability ABC"""
        super().__init__()

    @abstractmethod
    def transform(self) -> str:
        """transform abstract base class"""
        pass

    @abstractmethod
    def revert(self) -> str:
        """reverst abstract base class"""
        pass
