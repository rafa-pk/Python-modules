from .Deck import Deck
from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard

def main() -> None:
    
    print("\n === DataDeck Deck Builder ===\n")

    deck = Deck()
    creature = CreatureCard("Fire Dragon", 5, 'Legendary', 7, 5)
    artifact = ArtifactCard("Mana Crystal", 2, 'Rare', 4,
                            "Permanent: +1 mana per turn")
    spell = SpellCard("Lightning Bolt", 3, 'Damned',
                      "Deal 3 damage to target")

    print("Building deck with different card types...")
    deck.add_card(creature)
    deck.add_card(artifact)
    deck.add_card(spell)
    print("Deck stats: ",deck.get_deck_status())
    
    print("\nDrawing and playing cards:\n")


if __name__ == "__main__":
    main()
