from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('file:///C:/Users/Karan/Projects/DSA%20Prac/index.html')

search_field = driver.find_element(By.ID, 'search-box')

search_field.send_keys('Goa')

search_button = driver.find_element(By.ID, 'search-button')
search_button.click()

time.sleep(3)

results = driver.find_elements(By.CLASS_NAME, 'destination-name')
assert any('Goa' in result.text for result in results), "Destination not found in results"

print("Search functionality test passed successfully!")

driver.quit()