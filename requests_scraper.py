# requests_scraper.py
# Requirements: pip install requests beautifulsoup4
# Usage: python requests_scraper.py

import requests
from bs4 import BeautifulSoup
from typing import List, Dict
import time

BASE_URL = "example.com"          # change if needed
TARGET_PATH = "/wallets"              # example path — replace with actual path

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; wallet-scraper/1.0; +https://github.com/YOURNAME)"
}

def fetch_page(url: str) -> str:
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    return resp.text

def parse_wallets(html: str) -> List[Dict]:
    soup = BeautifulSoup(html, "html.parser")
    wallets = []
    # TODO: update the selector below to match gmgn.ai markup
    for card in soup.select(".wallet-card"):
        address_el = card.select_one(".address")
        balance_el = card.select_one(".balance")
        if not address_el:
            continue
        address = address_el.get_text(strip=True)
        balance = balance_el.get_text(strip=True) if balance_el else None
        wallets.append({"address": address, "balance": balance})
    return wallets

def main():
    url = BASE_URL + TARGET_PATH
    html = fetch_page(url)
    wallets = parse_wallets(html)
    for w in wallets:
        print(f"{w['address']}  |  {w['balance']}")

if __name__ == "__main__":
    main()
