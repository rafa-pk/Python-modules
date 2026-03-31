from abc import ABC, abstractmethod
from typing import Dict


class Card(ABC):
    """Abstract class blueprint for a Card"""
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """Constructor method, initializes attributes"""
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: Dict) -> Dict:
        """abstract method definition"""
        pass

    def get_card_info(self) -> Dict:
        """concrete method which returns a dict of card info"""
        return {
                "name": self.name,
                "cost": self.cost,
                "rarity": self.rarity,
            }

    def is_playable(self, available_mana: int) -> bool:
        """concrete method which returns a bool value
        based on available mana"""
        if available_mana > 3:
            return True
        return False
