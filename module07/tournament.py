from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (BattleStrategy, NormalStrategy,
                 AggressiveStrategy, DefensiveStrategy)
from typing import List, Tuple


def battle(opponents: List[Tuple[CreatureFactory, BattleStrategy]]) -> None:
    """battle simulating function, called in testing script"""
    print("*** Tournament ***")
    print(f"{len(opponents)} opponnents involved")

    fighters = [(factory.create_base(), strategy)
                for factory, strategy in opponents]
    for i in range(len(fighters)):
        for j in range(i + 1, len(fighters)):
            f1, s1 = fighters[i]
            f2, s2 = fighters[j]

            print("\n* Battle *")
            print(f1.describe())
            print("  vs.")
            print(f2.describe())
            print("  now fight!")
            try:
                s1.act(f1)
                s2.act(f2)
            except Exception as message:
                print(f"Battle error, aborting tournament: {message}")


def main() -> None:
    """ex3 testing script"""
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()
    normal_strategy = NormalStrategy()
    aggressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(flame_factory, normal_strategy),
            (healing_factory, defensive_strategy)])

    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(flame_factory, aggressive_strategy),
            (healing_factory, defensive_strategy)])

    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([(aqua_factory, normal_strategy),
            (healing_factory, defensive_strategy),
            (transform_factory, aggressive_strategy)])


if __name__ == "__main__":
    main()
