import sys


def main() -> None:
    """main function to take player scores"""
    ac = len(sys.argv)
    print("=== Player Score Analytics ===")
    if ac == 1:
        print(f"No scores provided. Usage: python3 "
              f"{sys.argv[0]} <score1> <score2> ...")
    else:
        scores = []
        for arg in sys.argv[1:]:
            try:
                scores.append(int(arg))
            except ValueError as message:
                print(f"Error: argument is not a valid score: {message}")
        print(f"Scores processed: {scores[0:]}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
