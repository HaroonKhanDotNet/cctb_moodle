

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from datetime import datetime

with open('logs/auto_sel_kb_searchbox_google.log', 'a') as log_file:

    import json
    json.dumps()

    log_file.write(f'starting: {datetime.now()} \n')
    log_file.write('tester: haroon khan \n')

    log_file.write('creating: Chrome browser... \n')
    browser_chrome = webdriver.Chrome()
    log_file.write('created: Chrome browser... \n')
    #browser_edge = webdriver.Edge()

    log_file.write('maximizing: Chrome browser... \n')
    browser_chrome.maximize_window()
    log_file.write('maximized: Chrome browser... \n')
    # browser_edge.maximize_window()

    log_file.write('loading: https://www.google.com/... \n')
    browser_chrome.get('https://www.google.com/')
    log_file.write('loaded: https://www.google.com/... \n')
    # browser_edge.get('https://www.selenium.dev/')

    log_file.write('creating: ActionChains(browser_chrome) \n')
    chromeAction = ActionChains(browser_chrome)
    log_file.write('created: ActionChains(browser_chrome) \n')

    log_file.write('sending keys: "action" \n')
    chromeAction.send_keys('action').perform()
    log_file.write('sent keys: "action" \n')

    log_file.write('key_down: ActionChains(browser_chrome) \n')
    chromeAction.key_down(Keys.ARROW_DOWN).key_down(
        Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
    log_file.write('key_down done: ActionChains(browser_chrome) \n')

    # ActionChains(browser_chrome).key_down(Keys.ESCAPE).perform()
    # ActionChains(browser_chrome).send_keys("action").perform()
    # .key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()

    # WebElement
    # target_searchbutton_chrome = browser_chrome.find_element(
    #    By.ID, 'docsearch-input')
    # target_searchbutton_chrome.send_keys('action')

    # target_searchbutton_edge = browser_edge.find_element(
    #    By.CLASS_NAME, 'DocSearch-Button')

    # target_searchbutton_chrome.click()
    # target_searchbutton_edge.click()

    #target_searchbutton_chrome.send_keys('Selenium Test Automation on Chrome')
    #target_searchbutton_edge.send_keys('Selenium Test Automation on Edge')

    # target_searchbox_chrome.submit()
    # target_searchbox_edge.submit()

    # target_element = browser.find_element(
    #    By.XPATH, '/html/body/div[1]/div[4]/main/div[1]/div[2]/div/div/div[2]/div[2]/form')
    # email_textbox = target_element.find_element(By.TAG_NAME, 'input')
    # email_textbox.send_keys('haroon.khan@canctb.ca')

    # log_file.write('waiting: user input on console \n')
    # input()
    log_file.write('shutting down: browser_chrome \n')
    browser_chrome.quit()
    log_file.write('shutdown done: browser_chrome \n')
    # browser_edge.quit()


# By.XPATH
# By.ID
# By.CLASS-NAME
# By.TAG_NAME
# By.NAME
# By.CSS_SELECTOR


# //*[@id="user_email"]
