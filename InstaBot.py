import logging
import random
import time
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


def setup_logging():
    log_filename = "scriptLog.log"
    log_level = logging.INFO

    logging.basicConfig(
        filename=log_filename,
        level=log_level,
        format="%(asctime)s [%(levelname)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

def load_config(filename):
    with open(filename, "r", encoding='utf-8') as config_file:
        config = yaml.load(config_file, Loader=yaml.FullLoader)
    return config

def login_to_instagram(driver, username, password):
    driver.get("https://www.instagram.com")
    time.sleep(random.uniform(1, 3))

    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )

    username_field.send_keys(username)
    time.sleep(random.uniform(1, 3))
    password_field.send_keys(password)
    time.sleep(random.uniform(2, 4))

    password_field.send_keys(Keys.ENTER)
    time.sleep(random.uniform(3, 5))

    try:
        save_info_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Not Now')]"))
        )
        save_info_button.click()
    except (NoSuchElementException, TimeoutException):
        logging.info("Unable to find 'Not Now for save info' button or timeout occurred.")
    time.sleep(random.uniform(1, 3))

    try:
        notification_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))
        )
        notification_button.click()
    except (NoSuchElementException, TimeoutException):
        logging.info("Unable to find 'Not Now for notification' button or timeout occurred.")
    time.sleep(random.uniform(1, 3))

    return driver

def get_followers_following_count(driver, username):
    driver.get(f"https://www.instagram.com/{username}/")
    followers_count_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/followers/')]/span"))
    )
    following_count_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/following/')]/span/span"))
    )

    followers_count = followers_count_element.get_attribute("title")
    following_count = following_count_element.get_attribute("innerHTML")

    logging.info("count followers " + followers_count)
    logging.info("count following " + following_count)

def explore_hashtag(driver, hashtag):
    explore_url = f"https://www.instagram.com/explore/tags/{hashtag}"
    driver.get(explore_url)
    time.sleep(random.uniform(1, 3))

def scroll_explore_page(driver):
    SCROLL_PAUSE_TIME = 3
    min_scrolls = 2
    max_scrolls = 15
    num_scrolls = random.randint(min_scrolls, max_scrolls)

    for _ in range(num_scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)

def get_post_links(driver):
    post_elements = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, '_aabd _aa8k  _al3l')]/a"))
    )
    for post in post_elements:
        logging.info('post_elements : ' + post.get_attribute("href"))
    post_links = [post.get_attribute("href") for post in post_elements]
    return post_links

def main():
    setup_logging()
    config = load_config("config.yaml")

    username = config["username"]
    password = config["password"]
    hashtags = config["hashtags"]
    numberToFollow = config["numberToFollow"]
    comment = config["comments"]
    random_hashtag = random.choice(hashtags)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    login_to_instagram(driver, username, password)

    get_followers_following_count(driver, username)

    explore_hashtag(driver, random_hashtag)
    scroll_explore_page(driver)

    post_links = get_post_links(driver)
    selected_post_link = random.choice(post_links)
    logging.info('selected_post_link : ' + selected_post_link)

    driver.get(selected_post_link)
    time.sleep(random.uniform(2, 5))

    for _ in range(numberToFollow):  # Change the number to the desired number of posts to interact with
        follow_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Follow')]"))
        )
        if follow_button.text == "Follow":
            follow_button.click()
            logging.info("Followed an account : " + selected_post_link)
            time.sleep(random.uniform(2, 5))
        else:
            logging.info("Already following the account")

        comment_area = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@aria-label='Add a comment…']"))
        )
        #logging.info("comment post : " + selected_post_link + "with this comment : "+random.choice(comment))
        #comment_area.send_keys(random.choice(comment))
        #logging.info("comment post : " + selected_post_link + "with this comment : "+comment)
        time.sleep(random.uniform(3, 4))

        account_link_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'xt0psk2')]/a"))
        )
        account_link = account_link_element.get_attribute("href")
        logging.info(account_link)
        driver.get(account_link)
        time.sleep(random.uniform(1, 3))

        follow_account_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Follow')]"))
        )
        if follow_account_button.text == "Follow":
            follow_account_button.click()
            logging.info("Followed the account : " + account_link)
            time.sleep(random.uniform(1, 5))
        else:
            logging.info("Already following the account")

        followers_link = f"{account_link}followers"
        logging.info("followers_link : " + followers_link)
        driver.get(followers_link)
        time.sleep(random.uniform(2, 4))

        followed_count = 0
        while followed_count < numberToFollow:
            follow_buttons = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[text()='Follow']"))
            )

            for button in follow_buttons:
                if button.text == "Follow":
                    button.click()
                    logging.info("Followed a follower")
                    time.sleep(random.uniform(1, 3))
                    followed_count += 1
                    if followed_count == numberToFollow:
                        break

    time.sleep(random.uniform(1, 6))
    driver.quit()

if __name__ == "__main__":
    main()