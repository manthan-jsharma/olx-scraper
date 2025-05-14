from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import csv


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

URL = "https://www.olx.in/items/q-car-cover"

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=chrome_options)
driver.get(URL)

time.sleep(5)

for _ in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)


items = driver.find_elements("css selector", "li.EIR5N")


results = []
for item in items:
    try:
        title = item.find_element("css selector", "span._2tW1I").text
        price = item.find_element("css selector", "span._89yzn").text
        location = item.find_element("css selector", "span._2uEFU").text
        results.append([title, price, location])
    except:
        continue


driver.quit()

with open("olx_car_cover_results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Location"])
    writer.writerows(results)

print(f"Saved {len(results)} results to 'olx_car_cover_results.csv'")
