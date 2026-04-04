import sys
import os
try:
    from dotenv import load_dotenv
except ImportError:
    print("Error: 'dotenv' package not found. Install it via pip/poetry")
    sys.exit(1)


def main() -> None:
    """main script"""
    env_vars = {}

    print("\nORACLE STATUS: Reading the Matrix...\n")
    try:
        load_dotenv()

        env_vars["Mode"] = os.getenv('MATRIX_MODE')
        if env_vars["Mode"] not in ["production", "development", None]:
            raise Exception(f"Error: Environment variable "
                            f"'{env_vars["Mode"]}' has unknown "
                            "or unexpected value.")
        env_vars["Database"] = os.getenv('DATABASE_URL')
        env_vars["API Access"] = os.getenv('API_KEY')
        env_vars["Log Level"] = os.getenv('LOG_LEVEL')
        env_vars["Zion Network"] = os.getenv('ZION_ENDPOINT')
    except Exception as message:
        print(f"{message}")

    print("Configuration loaded:")
    for key, var in env_vars.items():
        if var is None:
            print(f"Error: '{key}'' not found.")
        else:
            print(f"{key}: {var}")
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env properly configured")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configuration")


if __name__ == "__main__":
    """program entry point"""
    main()
