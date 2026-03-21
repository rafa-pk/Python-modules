def main() -> None:
    """program orchestrator"""
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    filename = "ancient_fragment.txt"
    try:
        print(f"Accessing Storage Vault: {filename}")
        if filename != "ancient_fragment.txt":
            raise Exception
        else:
            print("Connection established...\n")
        with open(filename, 'r') as file:
            content = file.read()
        print("RECOVERED DATA:")
        print(f"{content}\n")
    except Exception:
        print("ERROR: Storage vault not found. Run data generator first.")
    else:
        print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    """program's entry point"""
    main()
