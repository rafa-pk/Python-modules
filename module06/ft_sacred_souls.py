def main() -> None:
    print("\n=== Sacred Scroll Mastery===\n")

    from alchemy.elements import (create_fire, create_water, create_earth,
                                  create_air)
    print("Trying direct module access:")
    print(f"alchemy.elements.create_fire(): {create_fire()}")
    print(f"alchemy.elements.create_water(): {create_water()}")
    print(f"alchemy.elements.create_earth(): {create_earth()}")
    print(f"alchemy.elements.create_air(): {create_air()}")
    
    import alchemy
    print("\nTrying package-level access (controlled by __init__.py):")
    print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    print(f"alchemy.create_water(): {alchemy.create_water()}")
    try:
        alchemy.create_earth()
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")
    try:
        alchemy.create_air()
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
