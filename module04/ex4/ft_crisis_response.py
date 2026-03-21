def main() -> None:
    """program orchestrator"""
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    vault = ['lost_archive.txt',
             'classified_vault.txt',
             'standard_archive.txt']
    for file in vault:
        try:
            if file != 'standard_archive.txt':
                print(f"CRISIS ALERT: Attempting to access '{file}'...")
            else:
                print(f"ROUTINE ACCESS: Attempting to access '{file}'...")
            with open(file, 'r') as current_file:
                data = current_file.read()
                print(f"SUCCESS: Archive recovered - ''{data}''")
        except FileNotFoundError:
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable\n")
        except PermissionError:
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained\n")
        else:
            print("STATUS: Normal operations resumed\n")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    """program entry point"""
    main()
