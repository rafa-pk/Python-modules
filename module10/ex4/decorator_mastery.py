from collections.abc import Callable
from functools import wraps
import time
from typing import Any


def spell_timer(func: Callable) -> Callable:
    """Decorator that measures function execution time"""
    @wraps(func)
    def wrapper(*args: Any) -> Any:
        print(f"Casting function {func.__name__}...")
        start = time.time()
        call = func(*args)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return call
    return wrapper


def power_validator(min_power: int) -> Callable:
    """Decorator that validates power levels"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs: Any) -> Any:
            power = kwargs.get("power")
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Decorator that retries failed spells"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any) -> Any:
            for n in range(1, max_attempts):
                try:
                    return func(*args)
                except Exception:
                    print(f"Spell failed, retrying... (attempt {n}/"
                          f"{max_attempts})")
            print(f"Spell casting failed after {max_attempts} attempts")
            return None
        return wrapper
    return decorator


class MageGuild:
    """MageGuild class"""
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """static method that checks if name is valid"""
        if len(name) >= 3 and all(char.isalpha()
                                  or char == " " for char in name):
            return True
        return False

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    time.sleep(0.5)
    return "Fireball cast!"


@retry_spell(max_attempts=3)
def retrying_func(value: int) -> None:
    global attempts
    attempts += 1
    if attempts < value:
        raise ValueError
    print("Waaaaaaagh spelled !")


def main() -> None:
    """main function, used mainly to test implementations"""
    global attempts
    print("Testing spell timer...")
    print("Result: ", fireball())

    print("\nTesting retrying spell...")
    retrying_func(3)
    attempts = 5
    retrying_func(3)

    print("\nTesting MageGuild...")
    mage = MageGuild()
    print(mage.validate_mage_name("Robbe Griffith"))
    print(mage.validate_mage_name("Roy 123"))
    print(mage.cast_spell("Lightning", power=15))
    print(mage.cast_spell("Caca", power=8))


if __name__ == "__main__":
    main()
