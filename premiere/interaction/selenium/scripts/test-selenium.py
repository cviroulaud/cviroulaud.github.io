from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox(executable_path="./geckodriver")
# browser = webdriver.Chrome(executable_path="./chromedriver")


def selection(browser, adresse, selecteur):
    browser.get(adresse)
    return browser.find_element(By.CSS_SELECTOR, selecteur)

"""
bouton = selection(browser, "https://chrome.google.com/webstore/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn",
                   ".h-e-f-Ra-c > div:nth-child(1)")
"""
bouton = selection(browser, "http://jay.info.free.fr/", "input[type='submit']")
bouton.click()
# browser.quit()
