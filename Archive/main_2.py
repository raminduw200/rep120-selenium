from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import FirefoxOptions
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import time

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

USER_NAME = os.environ.get("USER_NAME")
PASSWORD = os.environ.get("PASSWORD")

courses = [96, 97, 98, 99, 100, 101, 102, 220, 86]


def rep120_selenium():
    # Driver options
    # ----------------------- Chrome -----------------------
    """
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome("/usr/local/bin/chromedriver", desired_capabilities=chrome_options.to_capabilities())
    # "/usr/local/bin/chromedriver",
    """
    # ------------------------------------------------------

    # ----------------------- Firefox -----------------------
    binary = FirefoxBinary('/usr/bin/firefox')
    driver = webdriver.Firefox(firefox_binary=binary)
    driver.get("https://ugvle.ucsc.cmb.ac.lk/course/view.php?id=96")
    # ------------------------------------------------------

    # Login options
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//input[@name='username']"))).send_keys(USER_NAME)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(PASSWORD)
    driver.find_element_by_id('loginbtn').click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Load course pages and scroll down
    for course in courses:
        driver.get("https://ugvle.ucsc.cmb.ac.lk/course/view.php?id={course_id}".format(course_id=course))
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
    driver.quit()
    print("Execution completed!")


if __name__ == '__main__':
    print("Execution start in main!")
    rep120_selenium()
