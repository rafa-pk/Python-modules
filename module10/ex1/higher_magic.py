from collections.abc import Callable
from typing import Any


def fireball(target: str, power: int) -> str:
    return f"Fireball thrown at '{target}' with {power} intensity"


def heal(target: str, power: int) -> str:
    return f"'{target}' was healed by {power} intensity"


def condition(target: str, power: int) -> bool:
    if power < 10:
        return True
    return False


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Returns a new function that calls both spells"""
    def combined(*args: str) -> tuple[str, str]:
        """returns both spells in tup"""
        return (spell1(*args), spell2(*args))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Returns a function with the same signature as the original"""
    def mega_fireball(**kwargs: Any) -> str:
        """returns a new function with power multiplied"""
        kwargs["power"] *= multiplier
        return base_spell(**kwargs)
    return mega_fireball


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Returns a new spell that only casts if a condition is true"""
    def caster(**kwargs: Any) -> str:
        """conditional cast function"""
        if condition(**kwargs):
            return spell(**kwargs)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    """Return a function that casts all spells in order"""
    def cast_all(*args: str) -> list:
        """cast all spells in order"""
        for spell in args:
            return [spell(*args) for spell in spells]
    return cast_all


def main() -> None:
    """main script to test the implemented functions"""
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    print("Combined spell result: ", combined('Dragon', 20))

    print("\nTesting power amplifier...")
    amplifier = power_amplifier(fireball, 10)
    print("Original: ", fireball('Goblin', 3),
          ", Amplified:", amplifier(target='Goblin', power=3))

    print("\nTesting conditional caster...")
    conditional = conditional_caster(condition, heal)
    print("Conditional is True: ", conditional(target='Wizard', power=6),
          ", Conditional is False: ", conditional(target='Wizard', power=14))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal])
    print(sequence("Knight", 80))


if __name__ == "__main__":
    main()
