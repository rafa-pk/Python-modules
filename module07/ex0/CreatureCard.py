from .Card import Card
from typing import Dict


class CreatureCard(Card):
    """specific card: Creature, inherits from Card blueprint"""
    def __init__(self, name: str, cost: int, rarity: str, 
                attack: int, health: int) -> None:
        """Constructor method, initalizes class attributes"""
        super().__init__(name, cost, rarity)
        self.type = "Creature"
        try:
            if attack < 0 or health < 0:
                raise ValueError
            self.attack = attack
            self.health = health
        except ValueError:
            print("Error: 'attack' and and 'health' must be positive integers")

    def play(self, game_state: Dict) -> Dict:
        """Custom creature implementation of play abstract method"""
        if game_state["mana"] < self.cost:
            return {
                    "success": False,
                    "reason": "Not enough mana",
                }
        game_state["mana"] -= self.cost
        game_state["battlefield"].append(self)
        return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
            }

    def get_card_info(self) -> Dict:
        info = super().get_card_info()
        info.update({
            "type": "Creature", 
            "attack": self.attack, 
            "health": self.health,
            })
        return info

    def attack_target(self, target: str) -> Dict:
        pass
