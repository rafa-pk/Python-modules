class Player:
    """blueprint for Player"""
    def __init__(self, name: str, score: int, status: bool,
                 achievements: tuple[str, ...], regions: str) -> None:
        """initialisaton method for Player class"""
        self.name = name
        self.score = score
        self.status = status
        self.achievements = achievements
        self.regions = regions


def main() -> None:
    """program's orchestrator function"""
    alice = Player("alice", 2300, True,
                   ("collector", "first_kill", "treasure_hunter",
                    "speed_demon", "achievement"), "north")
    bob = Player("bob", 1800, True,
                 ("caca", "level_10", "super_evil"), "east")
    charlie = Player("charlie", 2150, True,
                     ("collector", "boss_slayer",
                      "speed_demon", "achievement", "treasure_hunter",
                      "caca", "super_evil"), "central")
    diana = Player("diana", 2050, False,
                   ("collector", "caca", "treasure_hunter"), "be")
    players = [alice, bob, charlie, diana]

    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")
    high_scorers = [player.name for player in players if player.score > 2000]
    print(f"High scorers (>2000): {high_scorers}")
    doubles = [player.score*2 for player in players]
    print(f"Scores doubled: {doubles}")
    actives = [player.name for player in players if player.status]
    print(f"Active players: {actives}\n")

    print("=== Dict Comprehension Examples ===")
    scores = {player.name: player.score for player in players
              if player.status}
    print(f"Player scores: {scores}")
    categories = {"high": 3, "medium": 2, "low": 1}
    print(f"Score categories: {categories}")
    achievement_count = {player.name: len(player.achievements) for player in
                         players if player.status}
    print(f"Achievement counts: {achievement_count}\n")

    print("=== Set Comprehension Examples ===")
    unique_players = {player.name for player in players}
    print(f"Unique players: {unique_players}")
    count = {}
    all_achievements = [achievement for player in players for achievement
                        in player.achievements]
    for achievement in all_achievements:
        count[achievement] = count.get(achievement, 0) + 1
    unique_achievements = {achievement for achievement, ct in count.items()
                           if ct == 1}
    print(f"Unique achievements: {unique_achievements}")
    active_regions = {player.regions for player in players if player.status}
    print(f"Active regions: {active_regions}\n")

    print("=== Combined Analysis ===")
    print(f"Total players: {len(players)}")
    print(f"Total unique achievements: {len(set(all_achievements))}")
    all_scores = [player.score for player in players]
    print(f"Average score: {sum(all_scores) / len(all_scores)}")
    top = max(players, key=lambda p: p.score)
    print(f"Top performer: {top.name} ({top.score} points, "
          f"{len(top.achievements)} achievements)")


if __name__ == "__main__":
    """entry point"""
    main()
