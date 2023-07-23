from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://fantasy.premierleague.com/fixtures")

driver.quit()
