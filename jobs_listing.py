from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
import time
from network import rotate_user_agents, rotate_proxy

website = 'https://remoteok.com/'
driver_path = '/home/raksha/Downloads/chromedriver-linux64/chromedriver'

user_agent = rotate_user_agents()
proxy = rotate_proxy()

chrome_options = Options()
chrome_options.add_argument(f'--proxy-server={proxy}')
chrome_options.add_argument(f'user-agent={user_agent}')

with webdriver.Chrome(service=Service(driver_path), options=chrome_options) as driver:
    driver.get(website)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input.search'))
    )

    job = 'engineer'
    search_field = driver.find_element(By.CSS_SELECTOR, 'input.search')
    search_field.clear()
    search_field.send_keys(job)
    print(f'Searching for {job}...')
    search_field.send_keys(Keys.RETURN)
    print(f'Searching for {job}...Done')
    driver.execute_script('location.reload()')

    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'table#jobsboard tbody td.company'))
    )

    jobs = set()

    def get_links(web_driver):
        links = web_driver.find_elements(By.CSS_SELECTOR, 'a[itemprop="url"]')
        for link in links:
            if len(jobs) == 200:
                break
            jobs.add(link.get_attribute('href'))
            print(f'Saved {link.get_attribute("href")}')
            print(f'Total links: {len(jobs)}')

    while True:
        print('Scrolling down...')
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(2)
        if len(jobs) == 200:
            break
        get_links(driver)

    with open('engineer.txt', 'w') as f:
        for job in jobs:
            f.write(job + '\n')