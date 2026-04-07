# mypy: disable-error-code="attr-defined"
from ex1 import HealingCreatureFactory, TransformCreatureFactory


def main() -> None:
    """Main testing script for ex1"""
    print("Testing Creature with healing capability")

    healing_factory = HealingCreatureFactory()

    print("  base:")
    healing_base = healing_factory.create_base()
    print(healing_base.describe())
    print(healing_base.attack())
    print(healing_base.heal())

    print("  evolved:")
    healing_adv = healing_factory.create_evolved()
    print(healing_adv.describe())
    print(healing_adv.attack())
    print(healing_adv.heal())

    print("\nTesting Creature with transform capability")
    transform_factory = TransformCreatureFactory()
    print("  base:")
    transform_base = transform_factory.create_base()
    print(transform_base.describe())
    print(transform_base.attack())
    print(transform_base.transform())
    print(transform_base.attack())
    print(transform_base.revert())

    print("  evolved:")
    transform_adv = transform_factory.create_evolved()
    print(transform_adv.describe())
    print(transform_adv.attack())
    print(transform_adv.transform())
    print(transform_adv.attack())
    print(transform_adv.revert())


if __name__ == "__main__":
    """ex1 testing script entry point"""
    main()
