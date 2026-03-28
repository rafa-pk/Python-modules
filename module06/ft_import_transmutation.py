def main() -> None:
    print("\n=== Import Transmutation Mastery ===\n")

    print("Method 1 - Full Module Import:")
    import alchemy.elements
    print(f"alchemy.elements.create_fire(): {alchemy.create_fire()}")

    print("\nMethod 2 - Specific Function Import:")
    from alchemy import create_water
    print(f"create_water(): {create_water()}")

    print("\nMethod 3 - Aliased Import:")
    from alchemy.potions import healing_potion as heal
    print(f"heal(): {heal()}")

    print("\nMethod 4 - Multiple Imports:")
    from alchemy.elements import create_earth, create_fire
    from alchemy.potions import strength_potion
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}")

    print("\nAll import transmutation methods mastered!")


if __name__ == "__main__":
    main()
