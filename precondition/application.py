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
from faker import Faker
f = Faker()
#wait = WebDriverWait(webdriver, 10)


class Application:

 def __init__(self):
     self.driver = webdriver.Chrome()
     self.driver.implicitly_wait(15)
     self.driver.maximize_window()

 #LOGIN ============
 def login(self):
     self.driver.get("http://schooldata-test.com/")

 def sign_in(self):
     self.driver.get("http://schooldata-test.com/login")
     self.driver.find_element_by_id("email").send_keys("test@gmail.com")
     self.driver.find_element_by_id("password").send_keys("123456")
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/form/div[2]/button").click()
     self.driver.implicitly_wait(2)
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[3]/div/form/div[1]/div[2]/input")

 # SIGN UP REGISTRATION ==========
 def sign_up(self):
     self.driver.get("http://schooldata-test.com/register")
     self.driver.find_element_by_id("name").send_keys("AutotestBot")
     mail = self.driver.find_element_by_id("email")
     mail.send_keys(f.email())
     self.driver.find_element_by_id("password").send_keys("NewUser123456")
     self.driver.find_element_by_id("passwordConfirmation").send_keys("NewUser123456")
     self.driver.find_element_by_css_selector(".geosuggest__input").send_keys("Dallas")
     try:
         address = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".geosuggest__suggests.addressautocomplete__list___2XxOe")))
     finally:
         self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[6]/div/div[2]/ul/li[1]/span").click()
         time.sleep(1)

 def sign_up_student(self):
     self.driver.get("http://schooldata-test.com/register")
     self.driver.find_element_by_id("name").send_keys("AutotestBot")
     self.driver.find_element_by_id("email").send_keys("alexander.tunick@itrexgroup.com")
     self.driver.find_element_by_id("password").send_keys("NewUser123456")
     self.driver.find_element_by_id("passwordConfirmation").send_keys("NewUser123456")
     self.driver.find_element_by_css_selector(".geosuggest__input").send_keys("Dallas")
     try:
         address = WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable((By.CSS_SELECTOR, ".geosuggest__suggests.addressautocomplete__list___2XxOe")))
     finally:
         self.driver.find_element_by_xpath(
             ".//*[@id='root']/div/div[2]/div/form/div[1]/div[6]/div/div[2]/ul/li[1]/span").click()
         time.sleep(1)

 #QUIT ==============
 def log_out(self):
     self.driver.quit()

 def assort5(self):
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[1]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[2]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[3]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[4]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[5]/div")

 #DELETE
 def delete_saved(self):
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[2]/div[1]/button").click()
     time.sleep(1)
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[2]/div[1]/button").click()
     try:
         element = WebDriverWait(self.driver, 10).until(
             EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".watchList__no-saved-ins-message___216CE"), "No saved items...")
         )
     finally:
         self.driver.get_screenshot_as_file("saved_deleted.png")
#  ===== ===== ===== ===== ===== ===== ===== =============== ===== ===== ===== ========== =====
    # === PRECONDITION PRECONDITION PRECONDITION PRECONDITION PRECONDITION PRECONDITION PRECONDITION PRECONDITION ===
#===== ======  ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== =====


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
     #Assort5
     self.driver.get_screenshot_as_file("city_no_state.png")

 def search_with_magnifying_glass(self):
     time.sleep(1)
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-6']").click()
     f = Faker()
     field = self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/input")
     field.send_keys(f.random_element(elements=('los', 'los', 'los')))
     time.sleep(1)
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     self.driver.implicitly_wait(5)
     self.driver.find_element_by_xpath("//a[text()='Saddleback Valley Unified SD']")
     #Assert
     N = 2
     actions = ActionChains(self.driver)
     actions.send_keys(Keys.SPACE * N)
     actions.perform()

 #===============================================================================================================
 #===============================================================================================================
 #===============================================================================================================


 #===============================================================================================================
 #======================================== TEST Saved search ================================================
 #===============================================================================================================

 #activate diactivate watchlist
 def open_close_watchlist(self):
     self.driver.find_element_by_css_selector(".button__button___JTdqz.watchList__watch-list__btn--open___lM8w_").click()
     time.sleep(1)
     self.driver.find_element_by_css_selector(".button__button___JTdqz.watchList__watch-list__btn--close___2xU3A").click()
     time.sleep(1)

 # save school,daycare,college,district 11
 def save_school(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-3--option-6']").click()
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[3]/div/form/div[1]/div[2]/input").send_keys("saratoga")
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     self.driver.implicitly_wait(5)
     time.sleep(2)
     actions = ActionChains(self.driver)
     actions.send_keys(Keys.SPACE)
     actions.perform()
     time.sleep(1)
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div/div/div/div[1]/table/tbody/tr[5]/td[6]/button").click()
     time.sleep(6)
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div/div/div/div[1]/table/tbody/tr[6]/td[6]/button").click()
     self.driver.implicitly_wait(5)
     try:
         element = WebDriverWait(self.driver, 10).until(
             EC.text_to_be_present_in_element((By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/div/a/h3"), "Los Gatos High School")
         )
     finally:
         self.driver.implicitly_wait(5)
     try:
         element = WebDriverWait(self.driver, 10).until(
             EC.text_to_be_present_in_element((By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/div[2]/a/h3"),"Saratoga High School")
             )
     finally:
      time.sleep(1)
      self.driver.get_screenshot_as_file("saved_schools.png")
     #DELETE SAVED

 def save_from_product_page(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-3--option-6']").click()
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[3]/div/form/div[1]/div[2]/input").send_keys("saratoga union")
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(2)
     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
     time.sleep(1)
     self.driver.find_element_by_xpath("//*[p/text()='Saratoga Union School District']").click()
     time.sleep(2)
     N = 5
     actions = ActionChains(self.driver)
     actions.send_keys(Keys.ARROW_UP * N)
     actions.perform()
     time.sleep(2)
     self.driver.find_element_by_css_selector(".button__button___JTdqz.institutionPanel__save-btn___2SKd5").click()
     try:
         element = WebDriverWait(self.driver, 10).until(
             EC.text_to_be_present_in_element((By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/div/a/h3"), "Saratoga Union School District")
         )
     finally:
      self.driver.get_screenshot_as_file("saved_from_product_page.png")
      self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[2]/div[1]/button").click()
     try:
           myElem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".watchList__watch-list___31MkF.watchList__watch-list--open___QwSLh")))
           print("OPENED SAVED SEARCH IS PRESENT")
     except TimeoutException:
           print('OPENED SAVED SEARCH IS NOT PRESENT')
     finally:
           self.driver.implicitly_wait(10)
           self.driver.find_element_by_css_selector(".button__button___JTdqz.watchList__watch-list__btn--open___lM8w_")
           time.sleep(2)

 def activate_link_in_watchlist(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-3--option-6']").click()
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[3]/div/form/div[1]/div[2]/input").send_keys("saratoga")
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     self.driver.implicitly_wait(5)
     time.sleep(2)
     actions = ActionChains(self.driver)
     actions.send_keys(Keys.SPACE)
     actions.perform()
     time.sleep(1)
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div/div/div/div[1]/table/tbody/tr[5]/td[6]/button").click()
     try:
           myElem = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[h3/text()='Los Gatos High School']")))
           print("OPENED ")
     except TimeoutException:
           print('DIDNT OPENED')
     finally:
      self.driver.find_element_by_xpath("//*[h3/text()='Los Gatos High School']").click()
      time.sleep(1)
      self.driver.get_screenshot_as_file("link_in_watchlist.png")
      self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[2]/div[1]/button").click()
      time.sleep(1)

 def all_schools_link(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-6']").click()
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[2]/input").send_keys("Saratoga Union")
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(2)
     element = self.driver.find_element_by_xpath("//*[p/text()='Saratoga Elementary School']")
     element.send_keys(Keys.SPACE + Keys.SPACE)
     time.sleep(1)
     self.driver.find_element_by_css_selector(".searchResultsTable__link___3Q335.searchResultsTable__allSchools___vK2YH").click()
     try:
         elem = WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//*[p/text()='Argonaut Elementary School']"), "Argonaut Elementary School"))
         print("OPENED ")
     except TimeoutException:
         print('DIDNT OPENED')
     finally:
         #ASSERT
      self.driver.find_element_by_xpath("//*[p/text()='Argonaut Elementary School']")
      self.driver.get_screenshot_as_file("all_schools_link.png")

#===============================================================================================================
 #===============================================================================================================
 #===============================================================================================================


 #===============================================================================================================
 #======================================== TEST REGISTRATION ================================================
 #===============================================================================================================

 def register_student(self):
     time.sleep(1)
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/form/div[2]/button").click()
     try:
      student = WebDriverWait(self.driver, 0).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".reviewPage__panel___36xzG.panel")))
     finally:
      self.driver.get_screenshot_as_file("register_student.png")

 def register_parent(self):
     time.sleep(1)
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[1]/div[3]/div/div/label").click()
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/form/div[2]/button").click()
     try:
      parent = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".homePage__welcome___PPNOA")))
     finally:
      self.driver.get_screenshot_as_file("register_parent.png")

 def register_other(self):
     time.sleep(1)
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[1]/div[4]/div/div/label").click()
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/form/div[2]/button").click()
     try:
      parent = WebDriverWait(self.driver, 10).until(
         EC.presence_of_element_located((By.CSS_SELECTOR, ".homePage__welcome___PPNOA")))
     finally:
      self.driver.get_screenshot_as_file("register_other.png")

 def register_member(self):
     time.sleep(1)
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[1]/div[5]/div/div/label").click()
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/form/div[2]/button").click()
     try:
         parent = WebDriverWait(self.driver, 10).until(
             EC.presence_of_element_located((By.CSS_SELECTOR, ".homePage__welcome___PPNOA")))
     finally:
         self.driver.get_screenshot_as_file("register_member.png")

 def register_teacher_em1_em2ver(self):
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[1]/div[2]/div/div/label").click()
     time.sleep(1)
     got = ActionChains(self.driver)
     got.send_keys(Keys.SPACE)
     got.perform()
     self.driver.find_element_by_id("workEmail").send_keys("alexdrakeua@gmail.com") #===== Work EMAIL =====
     time.sleep(1)
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/form/div[2]/button").click()
     try:
         parent = WebDriverWait(self.driver, 10).until(
             EC.presence_of_element_located((By.CSS_SELECTOR, ".panel.verifiedEducatorPage__panel___1V7VW")))
     finally:
         time.sleep(1)
         self.driver.get_screenshot_as_file("register_teacher_em1_em2Ver.png")

 def register_teacher_em1_em2unver(self):
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div[1]/div[2]/div/div/label").click()
     time.sleep(1)
     got = ActionChains(self.driver)
     got.send_keys(Keys.SPACE)
     got.perform()
     self.driver.find_element_by_id("workEmail").send_keys("noneteacher@mail.ua")  # ===== Work EMAIL =====
     time.sleep(1)
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/form/div[2]/button").click()
     try:
         parent = WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".popup__popup__body___UKUmr>div>p"),
                                                                                    "We have registered your personal email address, but we are unable to verify your school email address against our database of active educators. Please try re-entering your school email or click here to submit a request for us to verify your email."))
     finally:
         time.sleep(1)
         self.driver.get_screenshot_as_file("register_teacher_em1_em2UnVer.png")

 def register_student_verified_email(self):
     time.sleep(1)
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/form/div[2]/button").click()
     try:
         student = WebDriverWait(self.driver, 0).until(
             EC.presence_of_element_located((By.CSS_SELECTOR, ".panel.verifiedEducatorPage__panel___1V7VW")))
     finally:
         self.driver.get_screenshot_as_file("register_student_verified_email.png")
     self.driver.find_element_by_css_selector(".dropdown__header___11L62.userMenu__header___2KR06").click()
     time.sleep(1)
     self.driver.find_element_by_css_selector(".userMenu__option___3jenC").click()
     time.sleep(1)
     self.driver.find_element_by_css_selector(".button__button___JTdqz.personalProfile__btn-delete___1sxMt").click()
     time.sleep(1)