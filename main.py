from selenium import webdriver
from tempfile import mkdtemp
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.binary_location = "/opt/chrome/chrome"
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1280x1696")
options.add_argument("--single-process")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-dev-tools")
options.add_argument("--no-zygote")
options.add_argument(f"--user-data-dir={mkdtemp()}")
options.add_argument(f"--data-path={mkdtemp()}")
options.add_argument(f"--disk-cache-dir={mkdtemp()}")
options.add_argument("--remote-debugging-port=9222")


def handler(event=None, context=None):
    chrome = webdriver.Chrome("/opt/chromedriver", options=options)
    chrome.get("https://example.com/")

    noticias = chrome.find_elements(by=By.XPATH, value="//h2[@class='c_t ']/a[2]")
    for x in range(len(noticias)):
        print(noticias[x].text)

    chrome.quit()
    return "OK"
