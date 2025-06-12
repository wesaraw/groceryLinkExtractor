# Grocery Link Extractor

This repository provides a simple script that uses Selenium to extract product
names and prices from a Stop & Shop search results page. The extracted data is
saved to `product_prices.csv`.

## Requirements

- Python 3.8+
- Google Chrome or Chromium browser installed
- ChromeDriver (automatically handled by `webdriver-manager`)

Install Python dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

Run the script and provide a Stop & Shop search URL when prompted:

```bash
python scrape_products.py
```

The script opens the page in a headless browser, waits for product tiles to
appear, and then collects the name and price for each product. Results are saved
in `product_prices.csv` in the current directory.

## Notes

- If you want to see the browser actions, remove the `--headless` option inside
  `scrape_products.py`.
- Network issues or missing browsers may prevent Selenium from running.
