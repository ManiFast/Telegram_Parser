# Telegram_Parser
A simple Python script to extract plain text messages from a Telegram channel export JSON file and save them to a TXT file.

# Telegram Channel Text Extractor

## Description
A simple Python script to extract plain text messages from a Telegram channel export JSON file and save them to a TXT file.

## Installation
pip install -r requirements.txt  # No extra requirements needed beyond standard json library

## Usage
1. Place your Telegram export JSON file (e.g., `result.json`) in the project directory.
2. Run the script:
   python extract_text.py 'result.json' 'output.txt'
3. The output TXT will contain message IDs and their plain text content.

## Example Output
2: ёу
4: Wake up Mani ...
The Matrix has you
Follow the white rabbit ...
Knock knock.

Сверкающие буквы на экране монитора оказались для меня реальным открытием. ...

## License
MIT License
