import time
import os
from os.path import join, dirname
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

USER_NAME = os.environ.get("USER_NAME")
PASSWORD = os.environ.get("PASSWORD")

courses = [{"ENH": 96}, {"1201": 97}, {"1202": 98}, {"1203": 99}, {"1204": 100},
           {"1205": 101}, {"1206": 102}, {"1207": 220}, {"PP": 86}]


def rep120_selenium(course_no_):
    course_id = 0
    for item in courses:
        if list(item.keys())[0] == course_no_:
            course_id = list(item.values())[0]

    if course_id != 0:
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
        # ------------------------------------------------------

        # Load the course page
        driver.get(f"https://ugvle.ucsc.cmb.ac.lk/course/view.php?id={course_id}")

        # Login options
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@name='username']"))).send_keys(USER_NAME)
        driver.find_element_by_xpath("//input[@name='password']").send_keys(PASSWORD)
        driver.find_element_by_id('loginbtn').click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(30)
        driver.quit()
        print(f"[SUCCESS] Visited the {course_no_} page!")
    else:
        print("[ERROR] COURSE ID NOT FOUND")
