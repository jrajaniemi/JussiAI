# Ask JussiAI, your digital twin.

This program is a Python script that interacts with OpenAI's GPT-4 model. It performs the following tasks:

1. Creates a directory named ~/.jussiai if it doesn't already exist.
2. Manages environment variables by creating and loading an .env file within the ~/.jussiai directory.
3. Sanitizes and processes user input for interaction with the GPT-4 model.
4. Sends a user's input message to the GPT-4 model using the OpenAI API.
5. Displays the response generated by the GPT-4 model.

Overall, this script serves as an CLI interface for interacting with the GPT-4 model, allowing users to engage in conversations and receive responses generated by the model.

## Installation

### Option 1: Manual

Follow these instructions to install the Jussi program:

1. **Download:** Download the Jussi-file to your computer.

2. **Dependencies:** This program requires a few dependencies to function. You can install them like this:

  ```bash
  pip install openai dotenv
  ```

  Make sure you're in an activated virtual environment (if needed) before
  installing the dependencies.

3. **Environment Variables:**  The program uses the OPENAI_API_KEY
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

4. **Running the Program:** You can run the program from the command line like this:

  ```bash
  ./Jussi User-provided text
  ```

  Replace "User-provided text" with your actual input.

### Option 2: System-Wide Installation (Advanced) 

Note: This option requires elevated privileges and should be used with caution.

1. Clone this repository to your local machine:

  ```bash
  git clone https://github.com/jrajaniemi/JussiAI.git
  cd Jussi
  ```
  
2. Make sure you have Python 3 and pip3 installed.

3. Run the installation script as a superuser (root):

  ```bash
  sudo ./install_jussi.sh
  ```

  This will install the required libraries and copy Jussi to a system-wide directory (e.g., /usr/local/bin/) that is accessible by all users. You can use Jussi by running Jussi from any directory.

## Usage

To use Jussi, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where Jussi is installed.
3. Run Jussi by executing the following command:

   ```bash
   ./Jussi "Your input text here"
   ```

  System-wide install usage:
  
  ```bash
   Jussi "Your input text here"
   ```

## Example Prompts

  ```bash
  $ git diff | Jussi Create a git commit message for these changes:
  ```
  
  ```bash
  $ cat language_en.json | Jussi Translate this JSON file into German:
  ```

  ```bash
  $ cat captions_en.sbv | Jussi Translate this YouTube subtitle into Finnish: | tee captions_fi.sbv
  0:00:30.038,0:01:00.034
  Et saisi poistaa rengasta tällä tavalla. Ensinnäkin, sinun tulisi katkaista ketjut. Poista sitten takavaihteisto ja lopuksi rengas.

  0:01:15.032,0:01:30.031
  Minulla oli pari desilitraa bensiiniä, joten huuhtelin ensin ketjut sillä.

  0:01:35.030,0:02:00.027
  Seuraavaksi puhdistin ne autonpyörän puhdistusaineella ja huuhtelin sitten ketjut vedellä. Ravistin sitä perusteellisesti ja annoin sen olla 10 minuuttia.

  0:02:20.024,0:02:45.021
  Seuraavaksi puhdistin sen ohentimella. Ravistin sitä ja annoin sen olla 30 minuuttia.

  0:02:50.020,0:03:10.018
  Ulkopuolelta ketjut näyttävät todella puhtailta. Mutta kun taivutat niitä, voit tuntea hiekan ja lian linkkien välissä. Kokeillaan ultraäänipuhdistinta. Nyt ketjut ovat todella puhtaat!

  0:03:18.017,0:03:25.016
  Kytke lämpö päälle ja säädä veden lämpötila 60 asteeseen Celsius.

  0:03:50.012,0:04:05.011
  Takavaihteisto puhdistetaan ultraäänipuhdistimessa. Puhdistusaika on 2h 30 min. Vaihdoin veden joka ½ tunti.

  0:04:15.009,0:04:25.008
  Takavaihteiston ripustin on jumissa. CRC auttaa tässä.

  0:04:50.005,0:05:20.001
  Takarattaiden poistaminen nopeuttaa takavaihteen puhdistusta.

  0:05:30.041,0:05:45.039
  Lisäsin liukupinnoille ohuen kerroksen vaseliinia.
  ...
  ```

# Trim.py Text Cleaner

## Overview

`Text Cleaner` is a Python script designed to clean text based on various parameters. It can remove HTML tags, URLs, and replace tabs, extra spaces, and newline characters with single spaces. The script is highly customizable and can be run from the command line.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/jrajaniemi/JussiAI
    ```

2. Navigate to the directory:

    ```bash
    cd JussiAI
    ```

3. Make the script executable:

    ```bash
    chmod 755 trim.py
    ```

## Usage

To run the script with all cleaning options enabled (default behavior):

```bash
echo "Your text here" | ./trim.py
```

To customize the cleaning process, you can use the following command-line arguments:

--remove_html: To remove HTML tags (enabled by default).
--remove_urls: To remove URLs (enabled by default).
--replace_tabs_spaces: To replace tabs and extra spaces with a single space (enabled by default).
--replace_newlines: To replace newline characters with spaces (enabled by default).
Example:

```bash
echo "Your text here" | ./trim.py --remove_html --remove_urls
```
