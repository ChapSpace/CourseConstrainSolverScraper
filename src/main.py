from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://bulletin.stanford.edu/programs/CS-BS")

dropdown_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Core Program Requirements')]"))
)

dropdown_element.click()

course_list = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//ul"))
)

courses = course_list.find_elements(By.XPATH, ".//li[contains(@class, 'm-0 p-0')]")

for course in courses:
    try:
        link = course.find_element(By.TAG_NAME, "a")
        course_name = link.text
        
        print(f"{course_name}")
    except Exception as e:
        print(f"Error extracting course info: {e}")

print("Done")

driver.quit()