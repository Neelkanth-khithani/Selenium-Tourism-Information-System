from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('file:///C:/Users/Karan/Projects/DSA%20Prac/feedback.html')

driver.find_element(By.ID, "rating").send_keys("4")  # Select a rating
driver.find_element(By.ID, "comment").send_keys("Great place!")
driver.find_element(By.ID, "submit_feedback").click()
time.sleep(3)
assert "Thank you for your feedback!" in driver.page_source
driver.quit()
