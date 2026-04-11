from functools import reduce, partial, lru_cache, singledispatch
import operator
from collections.abc import Callable
from typing import Any


def enchantment(power: int, element: str, target: str) -> str:
    """base enchantment function, will be passed into partial_enchanter"""
    return f"Enchanting {target} with {element} with power {power}"


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    try:
        if operation == "add":
            return reduce(operator.add, spells)
        elif operation == "multiply":
            return reduce(operator.mul, spells)
        elif operation == "max":
            return max(spells)
        elif operation == "min":
            return min(spells)
        raise ValueError(f"Operation not supported: '{operation}'")
    except Exception as message:
        print(f"{message}")
        return -1


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """Take a base enchantment function and return 3 specialized versions"""
    return {
            "fire": partial(base_enchantment, element="fire", power=50),
            "ice": partial(base_enchantment, element="ice", power=50),
            "thunder": partial(base_enchantment, element="thunder", power=50),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Fibonacci whic uses lru_cache for memoization"""
    if n < 0:
        return -1
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """Uses decorator singledispatch to create a spell system"""
    @singledispatch
    def spell(spell_type: Any) -> str:
        return "Unknown spell type"

    @spell.register(int)
    def _(damage: int) -> str:
        return f"Damage spell: {damage} damage"

    @spell.register(str)
    def _(enchantment: str) -> str:
        return f"Enchantment: {enchantment}"

    @spell.register(list)
    def _(multi_cast: list[Any]) -> str:
        return f"Multi-cast: {len(multi_cast)} spells"

    return spell


def main() -> None:
    """main function, tests the implementations"""
    print("\nTesting spell reducer...")
    print("Sum: ", spell_reducer([0, 1, 1, 2, 3, 5], "add"))
    print("Product: ", spell_reducer([1, 4, 8, 9, 2], "multiply"))
    print("Max: ", spell_reducer([40, 9, 8, 38, 1], "max"))

    print("\nTesting partial enchanter...")
    enchanter = partial_enchanter(enchantment)
    print("Fire :", enchanter["fire"](target="rvaz-da"))
    print("Ice: :", enchanter["ice"](target="rvaz-da"))
    print("Thunder :", enchanter["thunder"](target="rvaz-da-"))

    print("\nTesting memoized fibonacci...")
    print("Fib(0): ", memoized_fibonacci(0))
    print("Fib(1): ", memoized_fibonacci(1))
    print("Fib(10): ", memoized_fibonacci(10))
    print("Fib(15): ", memoized_fibonacci(15))
    print(memoized_fibonacci.cache_info())

    print("\nTesting spell dispatcher...")
    spell = spell_dispatcher()
    print(spell(42))
    print(spell("fireball"))
    print(spell(["spell 1", "spell 2", "spell 3"]))
    print(spell((1, 2)))


if __name__ == "__main__":
    main()
