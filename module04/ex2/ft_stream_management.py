import sys


def main() -> None:
    """program's orchestrator"""
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    archivist_id = input("Input stream active. Enter archivist ID: ")
    status_report = input("Input stream active. Enter status report: ")
    sys.stdout.write(f"\n[STANDARD] Archive status from {archivist_id}: "
                     f"{status_report}\n")
    sys.stderr.write('[ALERT] System diagnostic: '
                     'Communication channels verified\n')
    sys.stdout.write('[STANDARD] Data transmission complete\n')
    print("\nTree-channel communication test successful.")


if __name__ == "__main__":
    """program's entry point"""
    main()
