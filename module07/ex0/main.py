from .CreatureCard import CreatureCard


def main() -> None:
    """demo function"""
    print("\n=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:\n")
    creature = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)

    print("CreatureCard Info:")
    print(creature.get_card_info())

    game_state = {
                    "mana": 6,
                    "battlefield": []
            }
    print("\nPlaying Fire Dragon with 6 mana available:")
    print("Playable:", creature.is_playable(game_state["mana"]))
    print("Play result: ", creature.play(game_state))

    print("\nFire Dragon attacks Goblin Warrior:")
    print("Attack result: ", creature.attack_target("Goblin Warrior"))

    print("\nTesting insufficient mana (3 available):")
    print("Playable: ", creature.is_playable(game_state["mana"]))

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
