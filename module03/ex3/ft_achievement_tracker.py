class Player:
    """Class meant to represent a player and its achievements"""
    def __init__(self, name: str) -> None:
        """initialization method"""
        self.name = name
        self.achievements = set()

    def add_achievements(self, *achievements: str) -> None:
        """method to add achievements to player"""
        for achievement in achievements:
            self.achievements.add(achievement)

    def display_achievements(self) -> None:
        """method to display player's achievements"""
        print(f"Player {self.name} achievements: {self.achievements}")


def main() -> None:
    """main function, program orchestrator"""
    alice = Player("Alice")
    alice.add_achievements('first_kill', 'level_10', 'treasure_hunter',
                           'speed_demon')
    bob = Player("Bob")
    bob.add_achievements('first_kill', 'level_10', 'boss_slayer', 'collector')
    charlie = Player("Charlie")
    charlie.add_achievements('level_10', 'treasure_hunter', 'boss_slayer',
                             'speed_demon', 'perfectionist')

    print("=== Achievement Tracker System ===\n")
    alice.display_achievements()
    bob.display_achievements()
    charlie.display_achievements()

    unique = alice.achievements.union(bob.achievements, charlie.achievements)
    inter = alice.achievements.intersection(bob.achievements,
                                            charlie.achievements)
    inter2 = alice.achievements.intersection(bob.achievements)
    diff = alice.achievements.difference(bob.achievements)
    diff2 = bob.achievements.difference(alice.achievements)
    shared = (alice.achievements & bob.achievements |
              alice.achievements & charlie.achievements |
              bob.achievements & charlie.achievements)

    print("\n=== Achievement analytics ===")
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}")
    print(f"\nCommon to all players: {inter}")
    print(f"Rare achievements (1 player): {unique - shared}")
    print(f"\nAlice vs Bob common: {inter2}")
    print(f"Alice unique: {diff}")
    print(f"Bob unique: {diff2}")


if __name__ == "__main__":
    """program entry-point"""
    main()
