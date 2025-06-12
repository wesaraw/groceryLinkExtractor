import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def main():
    url = input("Enter the Stop & Shop search URL: ").strip()
    if not url:
        print("No URL provided")
        return

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # comment out to see the browser

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-grid-cell_price-tag--full-tile"))
        )
    except Exception:
        print("Timed out waiting for page to load.")
        driver.quit()
        return

    products = driver.find_elements(By.CLASS_NAME, "product-grid-cell_price-tag--full-tile")
    results = []
    for product in products:
        try:
            name = product.find_element(By.CLASS_NAME, "sr-only").text.strip()
            price = product.find_element(By.CLASS_NAME, "product-grid-cell_main-price").text.strip()
            results.append((name, price))
        except Exception:
            continue

    output_file = "product_prices.csv"
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Price"])
        writer.writerows(results)

    print(f"Saved {len(results)} items to {output_file}")
    driver.quit()


if __name__ == "__main__":
    main()
