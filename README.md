# Jussi

This is the installation guide for the Jussi program. The program is designed
to do something specific.

## Installation

Follow these instructions to install the Jussi program:

1. **Download:** Download the Jussi file to your computer.

2. **Dependencies:** This program requires a few dependencies to function.
You can install them like this:

```bash
pip install openai dotenv
```

Make sure you're in an activated virtual environment (if needed) before
installing the dependencies.

1. **Environment Variables:**  The program uses the OPENAI_API_KEY
environment variable to set the OpenAI API key. Create a .env file in the root
directory of the program. If you prefer to store the .env file in a specific
directory, such as ~/.jussiai/.env, you can do the following:

Create the ~/.jussiai directory if it doesn't exist:

```bash
mkdir -p ~/.jussiai
```

Create or edit the .env file in that directory and add your key like this:

```bash
OPENAI_API_KEY=YOUR_KEY_HERE
```

1. **Running the Program:** You can run the program from the command line like
this:

```bash
./Jussi User-provided text
```

Replace "User-provided text" with your actual input.
