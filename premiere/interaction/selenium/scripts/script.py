#importation
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#raccourci
driver = webdriver.Chrome(executable_path="chromedriver.exe")

#ouvrir le navigateur
driver.get("https://chrome.google.com/webstore/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn")
driver.maximize_window()

#télécharger metamask
driver.find_element_by_xpath("/html/body/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div/div/button").click()
driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div[2]/div[2]/div").click()

"""driver.find_element_by_xpath().sendKeys(Keys.TAB)
driver.sendKeys(Keys.ENTER)
#driver.execute_script("window.scrollBy(0,2000)","")"""