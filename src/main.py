from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://bulletin.stanford.edu/programs/CS-BS")

dropdown_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Core Program Requirements')]"))
)

dropdown_element.click()

course_list = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//ul"))
)

course_section = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//span[text()='Complete ALL of the following Courses:']/following-sibling::div"))
)

courses = course_section.find_elements(By.TAG_NAME, "li")
if courses:
    for course in courses:
        try:
            button = course.find_element(By.TAG_NAME, "button")
            course_name = button.text.strip()
            print(f"{course_name}")
        except Exception as e:
            print(f"Error extracting course info: {e}")
else:
    print("No courses found; the dropdown may not have expanded correctly.")

print("Done")

driver.quit()
