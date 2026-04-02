from ex0 import CreatureFactory, AquaFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    """Testing function for testing script"""
    base_creature = factory.create_base()
    advanced_creature = factory.create_evolved()

    print(base_creature.describe())
    print(base_creature.attack())
    print(advanced_creature.describe())
    print(advanced_creature.attack())


def test_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    """Testing function for testing script"""
    base1 = factory1.create_base()
    base2 = factory2.create_base()

    print(base1.describe())
    print("  vs.")
    print(base2.describe())
    print("  fight!")
    print(base1.attack())
    print(base2.attack())


def main() -> None:
    """Main testing script"""
    aquatic = AquaFactory()
    fire = FlameFactory()

    print("Testing Factory")
    test_factory(fire)

    print("\nTesting Factory")
    test_factory(aquatic)

    print("\nTesting battle")
    test_battle(fire, aquatic)


if __name__ == "__main__":
    """Testing script entry point"""
    main()
