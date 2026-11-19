# Random Password Generator

A secure and user-friendly Random Password Generator developed using Python as part of the Oasis Infobyte Python Programming Internship.

## Features

- Generate secure random passwords.
- Set a custom password length (minimum 8 characters).
- Select uppercase letters, lowercase letters, numbers, and symbols.
- Select at least two character types.
- Validate invalid inputs.
- Ensure every selected character type is represented.
- Regenerate passwords without restarting the application.
- Uses Python's built-in `secrets` module.

## Technologies Used

- Python 3.12
- secrets
- string

## Project Structure

```text
Python-Task3-RandomPasswordGenerator/
│
├── password_generator.py
├── README.md
└── screenshots/
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/Amirkhan786-coder/OIBSIP.git
```

2. Navigate to the project directory:

```bash
cd OIBSIP/Python-Task3-RandomPasswordGenerator
```

3. Run the application:

```bash
python password_generator.py
```

## Character Options

| Option | Character Type |
|---|---|
| 1 | Uppercase (A-Z) |
| 2 | Lowercase (a-z) |
| 3 | Numbers (0-9) |
| 4 | Symbols (!@#$...) |

## Security

The application uses Python's `secrets` module for secure random selection. Generated passwords are displayed in the terminal and are not intentionally saved to a file.

## Internship Details

**Organization:** Oasis Infobyte  
**Internship:** Python Programming Internship  
**Task:** Task 3 – Random Password Generator

**GitHub:** https://github.com/Amirkhan786-coder/OIBSIP

---

Developed by **Md Amir Khan**