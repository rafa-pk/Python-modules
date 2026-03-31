from typing import Dict, List
from ex0.Card import Card


class SpellCard(Card):

    def __init__(self, name: str, cost: str, rarity: str, 
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: Dict) -> Dict:
        pass

    def resolve_effect(self, targets: List) -> Dict:
        pass
