# Twitter Stock Symbol Scraper (with Input File)
This Python script scrapes stock symbols mentioned in Twitter profiles and tracks their frequency over time.

## Features:

Scrapes multiple Twitter usernames specified in an Input file.

Tracks the frequency of stock symbol mentions within tweets.

Allows for configuration of scraping parameters like wait time and scrape interval.

Exits the script when any letter is pressed during execution.

## Requirements:

Python 3.x

bs4 library (pip install bs4)

selenium library (pip install selenium)

A compatible WebDriver for your browser (e.g., ChromeDriver for Chrome) - download from https://chromedriver.chromium.org/downloads

## Usage:

Run the script using python script.py .

The script will continue scraping usernames from the input file at the specified interval until terminate the terminal.
