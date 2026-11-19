
import secrets
import string


def generate_password(length, selected_types):
    characters = ""

    # Character pools
    if "1" in selected_types:
        characters += string.ascii_uppercase

    if "2" in selected_types:
        characters += string.ascii_lowercase

    if "3" in selected_types:
        characters += string.digits

    if "4" in selected_types:
        characters += string.punctuation

    # Ensure at least one character from every selected type
    password = []

    if "1" in selected_types:
        password.append(secrets.choice(string.ascii_uppercase))

    if "2" in selected_types:
        password.append(secrets.choice(string.ascii_lowercase))

    if "3" in selected_types:
        password.append(secrets.choice(string.digits))

    if "4" in selected_types:
        password.append(secrets.choice(string.punctuation))

    # Fill remaining positions
    for _ in range(length - len(password)):
        password.append(secrets.choice(characters))

    # Shuffle password characters securely
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


def main():
    print("=" * 40)
    print("       RANDOM PASSWORD GENERATOR")
    print("=" * 40)

    while True:
        try:
            length = int(input("\nEnter password length (minimum 8): "))

            if length < 8:
                print("Error: Password length must be at least 8.")
                continue

            break

        except ValueError:
            print("Error: Please enter a valid number.")

    print("\nSelect character types:")
    print("1. Uppercase Letters (A-Z)")
    print("2. Lowercase Letters (a-z)")
    print("3. Numbers (0-9)")
    print("4. Symbols (!@#$...)")

    while True:
        choices = input(
            "\nEnter choices separated by commas (e.g. 1,2,3): "
        )

        selected_types = set(
            choice.strip() for choice in choices.split(",")
        )

        valid_types = {"1", "2", "3", "4"}

        if not selected_types.issubset(valid_types):
            print("Error: Please select only options 1, 2, 3, or 4.")
            continue

        if len(selected_types) < 2:
            print("Error: Select at least 2 character types.")
            continue

        break

    while True:
        password = generate_password(length, selected_types)

        print("\n" + "=" * 40)
        print("YOUR GENERATED PASSWORD")
        print("=" * 40)
        print(password)
        print("=" * 40)

        regenerate = input(
            "\nGenerate another password? (yes/no): "
        ).strip().lower()

        if regenerate not in ("yes", "y"):
            print("\nThank you for using Random Password Generator!")
            break


if __name__ == "__main__":
    main()
