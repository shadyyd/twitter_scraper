#usernames = ['Mr_Derivatives','warrior_0719','ChartingProdigy','allstarcharts','yuriymatso','TriggerTrades','AdamMancini4','CordovaTrades','Barchart']
import json
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# Read configuration from a file
with open('input.json') as input_file:
    input = json.load(input_file)

usernames = input['usernames']
WAIT_TIME = input['wait_time_sec'] # Time to wait for each page to load (seconds)
SCRAPE_INTERVAL = input['scrape_interval_min'] # Time between scrapes (minutes)

# Dictionary to store stock symbol counts
stock_symbols_counts = {}

def scrape_user(username):
    # Build the target URL
    target_url = f'https://twitter.com/{username}'

# Initialize Chrome webdriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
    driver = webdriver.Chrome(options=options)

    try:
        # Get the webpage content
        driver.get(target_url)
        time.sleep(WAIT_TIME)  # Wait for the page to load

        # Parse the HTML content with BeautifulSoup
        resp = driver.page_source
        soup = BeautifulSoup(resp, 'html.parser')

        # Find the section containing tweets
        tweets_section = soup.find('section', class_='css-175oi2r')

        # Extract stock symbols from tweet links
        if tweets_section:
            symbols = tweets_section.find_all('a', class_='css-1qaijid r-bcqeeo r-qvutc0 r-poiln3 r-1loqt21')

            for symbol_link in symbols:
                stock_symbol = symbol_link.text.upper()

                # Check if symbol starts with '$'
                if stock_symbol.startswith('$'):
                    # Update stock symbol count
                    if stock_symbol in stock_symbols_counts:
                        stock_symbols_counts[stock_symbol] += 1
                    else:
                        stock_symbols_counts[stock_symbol] = 1
    except Exception as e:
        print(f"Error encountered while processing {username}: {e}")  # Handle potential errors

    finally:
        # Always close the browser window
        driver.quit()

while True:
    # Scrape each user
    for username in usernames:
        scrape_user(username)

    # Print current stock symbol counts
    for word, count in stock_symbols_counts.items():
        print(f"'{word}' was mentioned {count} times in the last {SCRAPE_INTERVAL} minutes.")
    print('-------------------------------------------')
    
    # Clear the dictionary
    stock_symbols_counts = {}
    
    # Wait for the specified scrape interval
    time.sleep(SCRAPE_INTERVAL * 60)  # Convert minutes to seconds
