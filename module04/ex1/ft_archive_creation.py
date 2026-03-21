def main() -> None:
    """program's orchestrator'"""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    try:
        print("Initializing new storage unit: new_discovery.txt")
        with open("new_discovery.txt", 'w') as file:
            print("Storage unit created successfully...\n")
            print("Inscribing preservation data...")
            data = ("[ENTRY 001] New quantum algorithm discovered\n"
                    "[ENTRY 002] Efficiency increased by 347%\n"
                    "[ENTRY 003] Archived by Data Archivist trainee\n")
            file.write(data)
            print(f"{data}")
    except Exception:
        print("Error managing new storage unit.")
    else:
        print("Data inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    """program entry point"""
    main()
