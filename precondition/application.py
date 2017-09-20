from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import pytest



class Application:

 def __init__(self):
     self.driver = webdriver.Chrome()
     self.driver.implicitly_wait(15)
     self.driver.maximize_window()
 #LOGIN ===
 def login(self):
     self.driver.get("http://schooldata-test.com/")

 #QUIT ===
 def logout(self):
     self.driver.quit()

 # ==============================================================================================================
 #======================================== TEST SEARCH FROM AUTOCOMPLETE ===================================
 # ==============================================================================================================
 def search_daycares(self):
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/input").send_keys("Parkdale Private")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/div/div/span").click()
     time.sleep(5)
     self.driver.get_screenshot_as_file("daycare.png")
     element = self.driver.find_element_by_xpath(".//*[@id='overview']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     self.driver.get_screenshot_as_file("daycare_overview.png")
     element = self.driver.find_element_by_xpath(".//*[@id='diversity']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     self.driver.get_screenshot_as_file("daycare_diversity.png")
     element = self.driver.find_element_by_xpath(".//*[@id='programs']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     self.driver.get_screenshot_as_file("daycare_programs.png")
     element = self.driver.find_element_by_xpath(".//*[@id='finances']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     self.driver.get_screenshot_as_file("daycare_finances.png")
     time.sleep(2)

 def search_schools(self):
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/input").send_keys("Abbott Loop Elementary")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/div/div/span").click()
     time.sleep(5)
     self.driver.get_screenshot_as_file("school.png")
     element = self.driver.find_element_by_xpath(".//*[@id='overview']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     self.driver.get_screenshot_as_file("school_overview.png")
     element = self.driver.find_element_by_xpath(".//*[@id='teachers']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     self.driver.get_screenshot_as_file("school_teachers.png")
     element = self.driver.find_element_by_xpath(".//*[@id='diversity']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     self.driver.get_screenshot_as_file("school_diversity.png")
     element = self.driver.find_element_by_xpath(".//*[@id='programs']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     self.driver.get_screenshot_as_file("school_programs.png")
     element = self.driver.find_element_by_xpath(".//*[@id='finances']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     self.driver.get_screenshot_as_file("school_finances.png")
     time.sleep(2)

 def search_districts(self):
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/input").send_keys("Saratoga Union School")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/div/div/span").click()
     time.sleep(5)
     self.driver.get_screenshot_as_file("district.png")
     element = self.driver.find_element_by_xpath(".//*[@id='overview']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     self.driver.get_screenshot_as_file("district_overview.png")
     element = self.driver.find_element_by_xpath(".//*[@id='teachers']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     self.driver.get_screenshot_as_file("district_teachers.png")
     element = self.driver.find_element_by_xpath(".//*[@id='diversity']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     self.driver.get_screenshot_as_file("district_diversity.png")
     element = self.driver.find_element_by_xpath(".//*[@id='programs']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     self.driver.get_screenshot_as_file("district_programs.png")
     element = self.driver.find_element_by_xpath(".//*[@id='finances']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     self.driver.get_screenshot_as_file("district_finances.png")
     time.sleep(2)

 def search_colleges(self):
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/input").send_keys("Smith College")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/div/div[1]/span").click()
     time.sleep(5)
     self.driver.get_screenshot_as_file("college.png")
     #
     element = self.driver.find_element_by_xpath(".//*[@id='overview']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     self.driver.get_screenshot_as_file("college_overview.png")
     #
     element = self.driver.find_element_by_xpath(".//*[@id='diversity']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     self.driver.get_screenshot_as_file("college_diversity.png")
     #
     element = self.driver.find_element_by_xpath(".//*[@id='teachers']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     self.driver.get_screenshot_as_file("college_teachers.png")
     element = self.driver.find_element_by_xpath(".//*[@id='programs']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     self.driver.get_screenshot_as_file("college_programs.png")


 # ==============================================================================================================
 # ======================================== TEST SEARCH EMPTY TEXT FIELD ===================================
 # ==============================================================================================================
 # with drop down menu (state)
 def search_daycare_empty_field(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-1']").click()
     #check box
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[2]/div[1]/div/label").click()
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     #ASSERT
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[2]/div[1]/div[1]/input")
     self.driver.get_screenshot_as_file("daycare_empty_tfield.png")

 def search_college_empty_field(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-1']").click()
     #check box
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[2]/div[5]/div/label").click()
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[2]/div[1]/div[1]/input")
     self.driver.get_screenshot_as_file("college_empty_tfield.png")

 def search_elementary_empty_field(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-1']").click()
     #check box
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[2]/div[2]/div/label").click()
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[2]/div[1]/div[1]/input")
     self.driver.get_screenshot_as_file("elementary_empty_tfield.png")

 def search_middle_empty_field(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-1']").click()
     # check box
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[2]/div[3]/div/label").click()
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[2]/div[1]/div[1]/input")
     self.driver.get_screenshot_as_file("middle_empty_tfield.png")

 def search_high_empty_field(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-1']").click()
     # check box
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[2]/div[4]/div/label").click()
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[2]/div[1]/div[1]/input")
     self.driver.get_screenshot_as_file("high_empty_tfield.png")

 def search_elementary_middle_empty_field(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-1']").click()
     # check box
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[2]/div[2]/div/label").click()
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[2]/div[3]/div/label").click()
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[2]/div[1]/div[1]/input")
     self.driver.get_screenshot_as_file("elementary_middle_empty_tfield.png")

 def search_elementary_high_empty_field(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-1']").click()
     # check box
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[2]/div[2]/div/label").click()
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[2]/div[4]/div/label").click()
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[2]/div[1]/div[1]/input")
     self.driver.get_screenshot_as_file("elementary_high_empty_tfield.png")

 def search_middle_high_empty_field(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-1']").click()
     # check box
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[2]/div[3]/div/label").click()
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[2]/div[4]/div/label").click()
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[2]/div[1]/div[1]/input")
     self.driver.get_screenshot_as_file("middle_high_empty_tfield.png")

 # ==============================================================================================================
 # ======================================== TEST SEARCH BY *STATE* CRITERION ===================================
 # ==============================================================================================================

 def search_school_state