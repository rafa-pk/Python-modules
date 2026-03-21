def main() -> None:
    """program's orchestrator"""
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    try:
        with open('classified_data.txt', 'r') as file:
            print("Vault connection established with failsafe protocols")
            file1 = file.read()
            print("\nSECURE EXTRACTION:")
            print(f"{file1}\n")
        with open('security_protocols.txt', 'r') as file:
            file2 = file.read()
            print("SECURE PRESERVATION:")
            print(f"{file2}")
    except Exception as error:
        print(f"Vault connection error: {error}. Vault sealed.")
    finally:
        print("Vault automatically sealed upon completion")

    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    """program's entry point"""
    main()
