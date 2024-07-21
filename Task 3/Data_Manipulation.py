from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Path to the ChromeDriver
driver_path = '/usr/local/bin/chromedriver'  # Default path for Homebrew installation

# Initialize the WebDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Define the URL of the static web page
    url = 'https://www.mainflow.in/'

    # Open the URL
    driver.get(url)

    # Wait for the page to load completely
    time.sleep(5)

    # Get the page source
    html_content = driver.page_source

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract and print the relevant information

    # Example: Extract all text
    text = soup.get_text()
    print("Page Text:\n", text)

    # Example: Extract all links
    links = soup.find_all('a')
    for link in links:
        print("Link:", link.get('href'))

    # Example: Extract all image URLs
    images = soup.find_all('img')
    for image in images:
        print("Image URL:", image.get('src'))

    # Example: Extract specific divs or paragraphs
    divs = soup.find_all('div', class_='specific-class')
    for div in divs:
        print("Div Content:", div.get_text())

    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        print("Paragraph:", paragraph.get_text())

finally:
    # Close the WebDriver
    driver.quit()
