from collections.abc import Callable


def mage_counter() -> Callable:
    """Return a function that counts how many times it’s been called"""
    call_counter: int = 0

    def counter() -> int:
        nonlocal call_counter
        call_counter += 1
        return call_counter

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    """Return a function that accumulates power over time"""
    total: int = initial_power

    def accumulator(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    """Return a function that applies the specified enchantment"""
    def enchantor(item: str) -> str:
        return f"{enchantment_type} {item}"

    return enchantor


def memory_vault() -> dict[str, Callable]:
    """Return a dict with ’store’ and ’recall’ functions"""
    memories: dict[str, int] = {}

    def store(key: str, value: int) -> None:
        memories[key] = value

    def recall(key: str) -> int | str:
        return memories.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    """main function which tests the implemented functions"""
    print("Testing mage counter...")
    counting = mage_counter()
    for i in range(0, 3):
        print(f"counter a call {i}:", counting())
    counting_b = mage_counter()
    print("counter b call 1:", counting_b())

    print("\nTesting spell accumulator...")
    accumulating = spell_accumulator(100)
    print("Base 100, add 20: ", accumulating(20))
    print("Base 100, add 30: ", accumulating(30))

    print("\nTesting enchantment factory...")
    factory = enchantment_factory("Flaming")
    factory2 = enchantment_factory("Frozen")
    print(factory("Sword"))
    print(factory2("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"]("secret", 42)
    print("Store 'secret' = 42")
    print("Recall 'secret': ", vault["recall"]("secret"))
    print("Recall 'unknown': ", vault["recall"]("unkown"))


if __name__ == "__main__":
    main()
