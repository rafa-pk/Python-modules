def main() -> None:

    print("\n=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    from alchemy.grimoire.validator import validate_ingredients
    print(f'validate_ingredients("fire air"): '
          f'{validate_ingredients("fire air")}')
    print(f'validate_ingredients("dragon scales"): '
          f'{validate_ingredients("dragon scales")}')

    print("\nTesting spell recording with validation:")
    from alchemy.grimoire.spellbook import record_spell
    print(f'record_spell("Lightning", "air"): '
          f'{record_spell("Lightning", "air")}')
    print(f'record_spell("Dark Magic", "shadow"): '
          f'{record_spell("Dark Magic", "shadow")}')

    print("\nTesting late import technique:")
    from alchemy.grimoire.spellbook import record_spell
    print(f'record_spell("Lightning", "air"): '
          f'{record_spell("Lightning", "air"):}')

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely")


if __name__ == "__main__":
    main()
