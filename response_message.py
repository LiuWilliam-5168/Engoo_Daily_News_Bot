import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def article_crawler(url: str) -> str:

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Initialize the WebDriver (no need to specify the path to chromedriver)
    driver = webdriver.Chrome(options=chrome_options)

    # Open the webpage
    driver.get(url)

    # Wait for the page to load completely (you can adjust the wait time)
    driver.implicitly_wait(30)

    # Extract all 'a' tags with an 'href' attribute
    links = driver.find_elements(By.XPATH, "//article[@class='css-18b1c79']//a[@href]")

    # Extract the 'href' attribute from each 'a' tag
    href_links = [link.get_attribute('href') for link in links]

    # Close the WebDriver
    driver.quit()

    number = random.randint(0, len(href_links) - 1)
    return href_links[number]

categories_links = ["",
                    "https://engoo.com/app/daily-news/category/Science%20%26%20Technology",
                    "https://engoo.com/app/daily-news/category/Culture%20%26%20Entertainment",
                    "https://engoo.com/app/daily-news/category/Economy%20%26%20Business",
                    "https://engoo.com/app/daily-news/category/Health",
                    "https://engoo.com/app/daily-news/category/Travel%20%26%20Lifestyle",
                    "https://engoo.com/app/daily-news/category/Language%20%26%20Education",
                    "https://engoo.com/app/daily-news/category/Asia%20%26%20Pacific",
                    "https://engoo.com/app/daily-news/category/USA%20%26%20Americas",
                    "https://engoo.com/app/daily-news/category/Europe"]


def get_response(user_input: int) -> str:
    response: str = article_crawler(categories_links[int(user_input)])
    return response