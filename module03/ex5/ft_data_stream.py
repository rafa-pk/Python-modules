from typing import Generator
import random
import time


def event_generator(events_to_generate: int) -> Generator[dict, None, None]:
    """function which generates events and yields a dict"""
    players = ["alice", "bob", "charlie"]
    events = ["killed monster", "found treasure", "leveled up"]
    
    for _ in range(1, events_to_generate + 1):
        event_tp = random.choice(events)
        lvl = random.randint(1, 20)
        yield({"player": random.choice(players), "level": lvl, "type": event_tp})


def fibonnaci() -> Generator[int, None, None]:
    """fibonnaci generator"""
    num1, num2 = 0, 1
    while True:
        yield(num1)
        num1, num2 = num2, num1 + num2


def primes() -> Generator[int, None, None]:
    """prime number generator"""
    num = 2
    while True:
        is_prime = True
        for i in range(2, int(num**0,5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield(num)
        num += 1
    

def demo(fib_len: int, prime_len: int) -> None:
    """function to demonstrate fibonacci sequence and prime numbers"""
    fib = []
    prime = []

    for _ in range(fib_len):
        fib.append(next(fibonnaci()))
    for _ in range(prime_len):
        prime.append(next(primes()))
    print("=== Generator Demonstration ===")
    print("Fibonnaci sequence (first ({fib_len}): {fib}")
    print("Prime numbers (first {prime_len}): {primes(prime)}")


def main() -> None:
    """program orchestrator"""
    events_to_generate = 1000
    total_events = 0
    high_lv = 0
    treasure = 0
    lv_up = 0

    print("=== Game Data Stream Processor ===\n")
    print(f"Processing {events_to_generate} game events...\n")
    start = time.time()
    for event in event_generator(events_to_generate):
        if total_events < 3:
            print(f"Event {total_events + 1}: Player {event['player']} (level {event['level']}) {event['type']}")
        elif total_events == 3:
            print("...\n")
        if event["level"] > 10:
            high_lv += 1
        if event["type"] == "found treasure":
            treasure += 1
        elif event["type"] == "leveled up":
            lv_up += 1
        total_events += 1
    end = time.time()
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_lv}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {lv_up}\n")
    runtime = end - start
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {runtime:.3f} seconds\n")
    demo(10, 5)


if __name__ == "__main__":
    main()
