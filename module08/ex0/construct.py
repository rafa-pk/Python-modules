import sys
import os
import site


def main() -> None:
    """main function, will execute the code"""
    if sys.prefix != sys.base_prefix:
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print("Current Python: ", sys.executable)
        print("Virtual Environment: ", os.path.basename(sys.prefix))
        print("Environment Path: ", sys.prefix)
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print("\nPackage installation path:")
        print(site.getusersitepackages())
    else:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print("Current Python: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env\\Scripts\\activate  # On Windows")
        print("\nThen run this program again")


if __name__ == "__main__":
    """program entry point"""
    main()
