# wallet-scrapers

# gmgn-scrapers (sample)

Three short example scrapers targeting gmgn.ai wallet listing pages.

Contents:
- `scrapers/requests_scraper.py` — requests + BeautifulSoup (static)
- `scrapers/selenium_scraper.py` — Selenium for JS-rendered pages
- `scrapers/puppeteer_scraper.js` — Node.js + Puppeteer

**Reminder:** Update CSS selectors and target URLs to match the real site markup. Respect `robots.txt` and terms of service.

## Quick start (Python)
1. Create venv:

 python -m venv venv
source venv/bin/activate # or venv\Scripts\activate on Windows
pip install -r requirements.txt

2. Run:

python scrapers/requests_scraper.py




