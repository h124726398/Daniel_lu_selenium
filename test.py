from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time,getpass,configparser,math
from PIL import Image


options = webdriver.ChromeOptions()
#options.add_argument('--headless')
config = configparser.ConfigParser()
config.read('config.ini')
pic_number = 0

options.use_chromium = True
options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])

driver = webdriver.Chrome(options=options, executable_path='./chromedriver')
login = 1
driver.get("http://10.20.1.21:8080/business-central")
driver.maximize_window()


def is_element_present(by, value):
    try:
        driver.find_element(by, value)
    except:
        return False
    return True

while(login):
    try:
        inputname = driver.find_element(By.XPATH, "//*[@id=\"login-content\"]/form/fieldset/input[1]")
        inputpassword = driver.find_element(By.XPATH, "//*[@id=\"login-content\"]/form/fieldset/input[2]")
        account = "admin"
        password = "admin"
        inputname.send_keys(account)
        inputpassword.send_keys(password)
        inputname.submit()
        login=0
        time.sleep(5)

        # click design
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"home-action-design\"]/div[2]/div/a[1]"))).click()
        # click add_space_button
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div/div[3]/div/div[11]/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/button"))).click()

        # add_sapce
        space_name = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div/div[3]/div/div[11]/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div[2]/div[1]/input")))
        # space_name = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div[3]/div/div[11]/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div[2]/div[1]/input")
        space_description = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div[3]/div/div[11]/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/input")
        space_name_input = "test18"
        space_description_input = "test18"
        space_name.send_keys(space_name_input)
        space_description.send_keys(space_description_input)
        time.sleep(5)
        # click add_button
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div/div[3]/div/div[11]/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/button[2]"))).click()
        time.sleep(3)
        # click new space
        title = WebDriverWait(driver,5).until(EC.visibility_of_all_elements_located((By.XPATH,"//h2[contains(@class,'card-pf-title')]")))
        for number, data in enumerate(title, start=1):
            if data.text == space_name_input:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div/div[3]/div/div[11]/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[%s]/div" % number))).click()
                break

        # click import_pj_button
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div/div[3]/div/div[11]/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]"))).click()
        # import pj
        repository_url = driver.find_element(By.XPATH, "//*[@id=\"panel-id\"]/div/div/div[2]/div/div[2]/input")
        repository_url_input = 'https://github.com/kanic1111/cc-limit-approval-app-step1'
        repository_url.send_keys(repository_url_input)
        time.sleep(3)
        # click import_button
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"panel-id\"]/div/div/div[3]/button[2]"))).click()
        # click pj
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div/div[3]/div/div[11]/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[2]/div/div/div"))).click()
        # click ok button
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div/div[3]/div/div[11]/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/button[2]"))).click()
        # click deploy_button
        time.sleep(5)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'deploy'))).click()
        time.sleep(3)

        # get to module name
        module_name = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div[3]/div/div[11]/div/div/div[2]/div/div[2]/div/div[4]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div[1]").text
        # waited deploy successful
        while(True):
            data = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div[3]/div/div[11]/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div[2]/div/div/table/tbody").text
            time.sleep(3)
            if "Build of module '{module_name}' (requested by admin) completed. Build: SUCCESSFUL".format(module_name=module_name) in data:
                time.sleep(3)
                driver.close()
                break
    except Exception as e:
        print("Exception", e)
        print(driver.current_url)

