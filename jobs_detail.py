from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from network import rotate_user_agents
from dotenv import load_dotenv
import os

load_dotenv()

driver_path = '/home/raksha/Downloads/chromedriver-linux64/chromedriver'

user_agent = rotate_user_agents()
proxy = f"http://scrapeops:{os.getenv('SCRAPEOPS_API_KEY')}@residential-proxy.scrapeops.io:8181"

chrome_options = Options()
chrome_options.add_argument(f'--proxy-server={proxy}')
chrome_options.add_argument(f'user-agent={user_agent}')

with webdriver.Chrome(service=Service(driver_path), options=chrome_options) as driver:
    print("Opened driver")
    with open('engineer.txt', 'r') as jobs_list:
        for job in jobs_list:
            print(job)
            driver.get(job)
            print("Driver running...")
            print("Waiting for page to load...")

            WebDriverWait(driver, 600).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'table#jobsboard tbody'))
            )

            print("Loaded page...")
            print("Started scraping...")
            company_image_url = driver.find_element(By.CSS_SELECTOR, 'td.has-logo img.logo').get_attribute('src')
            job_title = driver.find_element(By.CSS_SELECTOR, 'h2[itemprop="title"]').text
            company_title = driver.find_element(By.CSS_SELECTOR, 'h3[itemprop="name"]').text
            location = driver.find_element(By.CSS_SELECTOR, 'div.location a').text
            salary_range = driver.find_element(By.XPATH, '//*[@id="job-1059136"]/td[2]/div[2]').text
            description = driver.find_element(By.CSS_SELECTOR, 'div.description').text
            application_posted = driver.find_element(By.CSS_SELECTOR, 'td.time time').get_attribute('datetime')
            scraped_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            print(f'Company image URL: {company_image_url}')
            print(f'Job title: {job_title}')
            print(f'Company title: {company_title}')
            print(f'Location: {location}')
            print(f'Salary range: {salary_range}')
            print(f'Description: {description}')
            print(f'Application posted: {application_posted}')
            print(f'Scraped at: {scraped_at}')