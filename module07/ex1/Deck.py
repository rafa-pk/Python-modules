from typing import Dict
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from.SpellCard import SpellCard
from .ArtifactCard import ArtifactCard


class Deck:

    def __init__(self) -> None:
        
        self.deck: List[Card] = []
        self.total_cards: int = 0

    def add_card(self, card: Card) -> None:
        
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:

        for card in deck:
            if card.name == card_name:
                self.deck.remove("card_name")
                return True
        else:
            return False

    def shuffle(self) -> None:
        pass

    def draw_card(self) -> Card:
        pass
    
    def get_deck_status(self) -> Dict:
        return {
                    "total_cards": len(self.deck),
                    "creatures": len([c for c in self.deck 
                                      if isinstance(c, CreatureCard)]),
                    "spells": len([c for c in self.deck
                                   if isinstance(c, SpellCard)]),
                    "artifacts": len([c for c in self.deck
                                      if isinstance(c, ArtifactCard)]),
                    "avg_cost": round((sum(c.cost for c in self.deck) /
                                       len(self.deck) if len(self.deck) > 0 
                                       else 0.00), 1),
                }
