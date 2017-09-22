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


 def sign_in(self):
     self.driver.get("http://schooldata-test.com/")
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div/div/ul/li[3]/div/div[2]/a").click()
     self.driver.find_element_by_id("email").send_keys("test@gmail.com")
     self.driver.find_element_by_id("password").send_keys("123123")
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/form/div[2]/button").click()
     self.driver.implicitly_wait(2)
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div/div/div/a[1]").click()
     self.driver.implicitly_wait(2)

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
     element = self.driver.find_element_by_xpath(".//*[@id='diversity']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     element = self.driver.find_element_by_xpath(".//*[@id='programs']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     element = self.driver.find_element_by_xpath(".//*[@id='finances']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)

 def search_schools(self):
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/input").send_keys("Abbott Loop Elementary")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/div/div/span").click()
     time.sleep(5)
     self.driver.get_screenshot_as_file("school.png")
     element = self.driver.find_element_by_xpath(".//*[@id='overview']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     element = self.driver.find_element_by_xpath(".//*[@id='teachers']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     element = self.driver.find_element_by_xpath(".//*[@id='diversity']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     element = self.driver.find_element_by_xpath(".//*[@id='programs']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     element = self.driver.find_element_by_xpath(".//*[@id='finances']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)


 def search_districts(self):
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/input").send_keys("Saratoga Union School")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/div/div/span").click()
     time.sleep(5)
     self.driver.get_screenshot_as_file("district.png")
     element = self.driver.find_element_by_xpath(".//*[@id='overview']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     element = self.driver.find_element_by_xpath(".//*[@id='teachers']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     element = self.driver.find_element_by_xpath(".//*[@id='diversity']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     element = self.driver.find_element_by_xpath(".//*[@id='programs']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     element = self.driver.find_element_by_xpath(".//*[@id='finances']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)

 def search_colleges(self):
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/input").send_keys("Smith College")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/div/div[1]/span").click()
     time.sleep(5)
     self.driver.get_screenshot_as_file("college.png")
     element = self.driver.find_element_by_xpath(".//*[@id='overview']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     element = self.driver.find_element_by_xpath(".//*[@id='diversity']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     element = self.driver.find_element_by_xpath(".//*[@id='teachers']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     element = self.driver.find_element_by_xpath(".//*[@id='programs']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)



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
 # ======================================== TEST SEARCH WITH ONE LETTER(Input) AND STATE, ZIPCODE ===============
 # ==============================================================================================================

 def search_d_letter_allstates(self):
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/input").send_keys("d")
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     #ASSERT
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[1]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[2]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[3]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[4]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[5]/div")
     self.driver.get_screenshot_as_file("d_letter_allstates.png")

 def search_daycare_s_letter_state(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-1']").click()
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/input").send_keys("s")
     # check box
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[2]/div[1]/div/label").click()
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     # ASSERT
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label/div")
     self.driver.get_screenshot_as_file("s_letter__daycare_state.png")

 def search_elementary_a_letter_state(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-37']").click()
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/input").send_keys("a")
     # check box
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[2]/div[2]/div/label").click()
     time.sleep(1)
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     # ASSERT
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[1]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[2]/div")
     self.driver.get_screenshot_as_file("a_letter__elementary_state.png")

 def search_middle_b_letter_state(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-7']").click()
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/input").send_keys("j")
     # check box
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[2]/div[3]/div/label").click()
     time.sleep(1)
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     # ASSERT
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[1]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[2]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[3]/div")
     self.driver.get_screenshot_as_file("j_letter__middle_state.png")

 def search_high_s_letter_state(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-7']").click()
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/input").send_keys("s")
     # check box
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[2]/div[4]/div/label").click()
     time.sleep(1)
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     # ASSERT
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[1]/div")
     self.driver.get_screenshot_as_file("s_letter__high_state.png")

 def search_college_s_letter_state(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-6']").click()
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/input").send_keys("s")
     # check box
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[2]/div[5]/div/label").click()
     time.sleep(1)
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[1]/div")
     self.driver.get_screenshot_as_file("s_letter__college_state.png")

 def search_elem_middle_s_letter_state(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-6']").click()
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/input").send_keys("s")
     # check box
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[2]/div[2]/div/label").click()
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[2]/div[3]/div/label").click()
     time.sleep(1)
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     # ASSERT
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[1]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[2]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[3]/div")
     self.driver.get_screenshot_as_file("s_letter__elem_middle_state.png")

 def search_elem_high_s_letter_d_letter_state(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-6']").click()
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/input").send_keys("d")
     # check box
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[2]/div[2]/div/label").click()
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[2]/div[4]/div/label").click()
     time.sleep(1)
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     # ASSERT
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[1]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[2]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[3]/div")
     self.driver.get_screenshot_as_file("d_letter__elem_high_state.png")

 def search_midl_high_s_letter_state(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-6']").click()
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/input").send_keys("s")
     # check box
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[2]/div[3]/div/label").click()
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[2]/div[4]/div/label").click()
     time.sleep(1)
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     # ASSERT
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[1]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[2]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[3]/div")
     self.driver.get_screenshot_as_file("s_letter__middle_high_state.png")

 def search_zip_code_with_state(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-6']").click()
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/input").send_keys("90005")
     time.sleep(1)
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     # ASSERT
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[1]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[2]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[3]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[4]/div")
     self.driver.get_screenshot_as_file("zipcode_with_state.png")

 def search_zip_code_no_criteria(self):
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/input").send_keys("90005")
     time.sleep(1)
     # ASSERT
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[1]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[2]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[3]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[4]/div")
     self.driver.get_screenshot_as_file("zipcode_no_criteria.png")

 def search_city_no_state(self):
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/input").send_keys("Los Angeles")
     time.sleep(1)
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/div/div[1]/span").click()
     time.sleep(1)
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[1]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[2]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[3]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[4]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[5]/div")
     self.driver.get_screenshot_as_file("city_no_state.png")


 #===============================================================================================================
 #===============================================================================================================
 #===============================================================================================================

 #self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/div/div/div[1]/table/tbody/tr[6]/td[1]/a[1]/p").click()
 #===============================================================================================================
 #======================================== TEST SAVE INSTITUTION ================================================
 #===============================================================================================================

 # save school,daycare,college,district 11
 def save_institutions_from_result_page(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.implicitly_wait(2)
     self.driver.find_element_by_css_selector("#react-select-4--option-2").click()
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/input").send_keys("Saratoga")
     time.sleep(1)
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div/div/div/a[1]").click()
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     #ASSERT
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[1]/div")
     element = self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/div/div/div[1]/table/tbody/tr[6]/td[1]/a[1]/p")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/div/div/div[1]/table/tbody/tr[6]/td[6]/button").click()
     self.driver.implicitly_wait(5)
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/div/div/div[1]/table/tbody/tr[6]/td[6]/button").click()
     self.driver.find_element_by_xpath("//button[@type=’button’]").click()
     self.driver.implicitly_wait(5)
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div/div/div/div[1]/table/tbody/tr[9]/td[6]/button")
     self.driver.implicitly_wait(5)