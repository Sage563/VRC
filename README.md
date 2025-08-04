# VRC - Voice-Controlled Authentication

A proof-of-concept application demonstrating user authentication (sign-up and sign-in) controlled entirely by voice commands.

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)

---

## Features

*   **Voice-Driven Account Creation:** Register a new user account using only your voice.
*   **Voice-Driven Sign-In:** Securely access an existing account with voice commands.
*   **Interactive CLI:** A simple command-line interface guides you through the process with voice prompts and feedback.

## Prerequisites

Before you begin, ensure you have the following installed:

*   Python 3.8+
*   `pip` (Python package installer)
*   A working microphone connected to your system.

> **Note:** This project likely depends on libraries for speech recognition and text-to-speech.DO not install the packages when run it auto installs
## Installation

1.  **Clone the repository :**
    ```bash
    git clone https://github.com/Sage563/VRC.git
    cd VRC
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```


## Usage

To start the application, run the main Python script from the project's root directory.

```bash
python main.py
```

Follow the audible prompts to either create a new account or sign in.

## How It Works

The application utilizes a speech recognition library to capture and interpret voice commands. It guides the user through the sign-up or sign-in flow, prompting for information like a username and password\voice. It then uses text-to-speech to provide feedback and instructions and uses a voice regnoztion ai model to
see if its the thing as the users voice and words.

## License 
Vist Licencense File


## The api
We use a model from remsembler or faster-whispher to check your voice and words


## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
