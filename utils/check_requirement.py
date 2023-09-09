try:
    with open('requirements.txt', 'r') as file:
        for line in file:
            # Remove leading/trailing whitespaces and comments
            package_name = line.strip().split('#')[0].strip()
            
            if package_name:
                try:
                    # Attempt to import the package
                    __import__(package_name)
                    print(f"{package_name} is installed.")
                except ImportError:
                    print(f"{package_name} is not installed.")
except FileNotFoundError:
    print("requirements.txt file not found.")


