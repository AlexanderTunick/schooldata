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
     self.driver.get("https://www.schooldata-test.com")

 def sign_in(self):
     self.driver.get("https://www.schooldata-test.com/login")
     self.driver.find_element_by_id("email").send_keys("test@gmail.com")
     self.driver.find_element_by_id("password").send_keys("123456")
     time.sleep(1)
     self.driver.find_element_by_css_selector(".button__button___JTdqz.commonForm__submit-btn___1hNXb").click()

     try:
         element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//input[@placeholder='School, City, District or Zipcode']")))
     finally:
      self.driver.find_element_by_xpath(".//input[@placeholder='School, City, District or Zipcode']")

 # SIGN UP REGISTRATION ==========
 def sign_up(self):
     self.driver.get("https://www.schooldata-test.com/register")
     self.driver.find_element_by_id("firstName").send_keys("AutoBot")
     self.driver.find_element_by_id("lastName").send_keys("Test")
     mail = self.driver.find_element_by_id("email")
     mail.send_keys(f.email())
     self.driver.find_element_by_id("password").send_keys("NewUser123456")
     self.driver.find_element_by_id("passwordConfirmation").send_keys("NewUser123456")
     time.sleep(1)
     self.driver.execute_script("window.scrollTo(50, 300);")
     self.driver.find_element_by_css_selector(".geosuggest__input").send_keys("Dallas")
     try:
         address = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".geosuggest__suggests.registerForm__suggest-list___3BB71.personalProfile__suggest-list___EmB61")))
     finally:
         self.driver.find_element_by_css_selector(".geosuggest__item.addressautocomplete__item___3rnxu").click()
         time.sleep(1)

 def sign_up_student(self):
     self.driver.get("https://www.schooldata-test.com/register")
     self.driver.find_element_by_id("firstName").send_keys("AutoBot")
     self.driver.find_element_by_id("lastName").send_keys("Test")
     self.driver.find_element_by_id("email").send_keys("drakemac2030@gmail.com")
     self.driver.find_element_by_id("password").send_keys("NewUser123456")
     self.driver.find_element_by_id("passwordConfirmation").send_keys("NewUser123456")
     time.sleep(1)
     self.driver.execute_script("window.scrollTo(50, 300);")
     self.driver.find_element_by_css_selector(".geosuggest__input").send_keys("Dallas")
     try:
         address = WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable((By.CSS_SELECTOR, ".geosuggest__suggests.registerForm__suggest-list___3BB71.personalProfile__suggest-list___EmB61")))
     finally:
         self.driver.find_element_by_css_selector(".geosuggest__item.addressautocomplete__item___3rnxu").click()
         time.sleep(1)

 def delete_profile(self):
     self.driver.find_element_by_css_selector(".dropdown__header___11L62.userMenu__header___2KR06").click()
     time.sleep(1)
     self.driver.find_element_by_css_selector(".userMenu__option___3jenC").click()
     time.sleep(1)
     self.driver.find_element_by_css_selector(".button__button___JTdqz.personalProfile__btn-delete___1sxMt").click()
     self.driver.find_element_by_css_selector(".homePage__search-bar___35y1k")
     time.sleep(1)
     self.driver.execute_script("window.scrollTo(100, document.body.scrollHeight);")
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
 #DELETE 2
 def delete_1_saved(self):
     self.driver.find_element_by_css_selector(".button__button___JTdqz.watchList__watch-list-card__btn--remove___4CdsZ").click()
     time.sleep(1)
#  ===== ===== ===== ===== ===== ===== ===== =============== ===== ===== ===== ========== =====
    # === PRECONDITION PRECONDITION PRECONDITION PRECONDITION PRECONDITION PRECONDITION PRECONDITION PRECONDITION ===
#===== ======  ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== =====


 # ==============================================================================================================
 #======================================== TEST SEARCH FROM AUTOCOMPLETE ===================================
 # ==============================================================================================================
 def search_daycares(self): #Daycare 100
     self.driver.find_element_by_css_selector(".homePage__query-wrapper___2CdIM>input").send_keys("Parkdale Private")
     self.driver.find_element_by_css_selector(".autocomplete__menu___370cg").click()
     time.sleep(5)
     self.driver.get_screenshot_as_file("daycare.png")
     element = self.driver.find_element_by_xpath(".//*[@id='general']")
     time.sleep(2)
     actionse = ActionChains(self.driver)
     actionse.move_to_element(element)
     actionse.perform()
     time.sleep(1)
     element = self.driver.find_element_by_xpath(".//*[@id='diversity']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     element = self.driver.find_element_by_xpath(".//*[@id='programs']")
     actionsi = ActionChains(self.driver)
     actionsi.move_to_element(element).perform()
     time.sleep(1)
     #element = self.driver.find_element_by_xpath(".//*[@id='finances']")
     actionsii = ActionChains(self.driver)
     actionsii.move_to_element(element).perform()
     time.sleep(1)

 def search_schools(self):
     self.driver.find_element_by_css_selector(".homePage__query-wrapper___2CdIM>input").send_keys("Abbott Loop Elementary")
     time.sleep(1)
     self.driver.find_element_by_css_selector(".autocomplete__menu___370cg").click()
     time.sleep(5)
     self.driver.get_screenshot_as_file("school.png")
     element = self.driver.find_element_by_xpath(".//*[@id='general']")
     actionsa = ActionChains(self.driver)
     actionsa.move_to_element(element).perform()
     time.sleep(1)
     #element = self.driver.find_element_by_xpath(".//*[@id='teachers']")
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
     self.driver.find_element_by_css_selector(".homePage__query-wrapper___2CdIM>input").send_keys("Saratoga Union")
     time.sleep(2)
     self.driver.find_element_by_css_selector(".autocomplete__menu___370cg").click()
     time.sleep(5)
     self.driver.get_screenshot_as_file("district.png")
     element = self.driver.find_element_by_xpath(".//*[@id='general']")
     actione = ActionChains(self.driver)
     actione.move_to_element(element).perform()
     time.sleep(1)
     #element = self.driver.find_element_by_xpath(".//*[@id='teachers']")
     #actions = ActionChains(self.driver)
     #actions.move_to_element(element).perform()
     #time.sleep(1)
     element = self.driver.find_element_by_xpath(".//*[@id='diversity']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     #element = self.driver.find_element_by_xpath(".//*[@id='programs']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     element = self.driver.find_element_by_xpath(".//*[@id='finances']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)

 def search_colleges(self):
     self.driver.find_element_by_css_selector(".homePage__query-wrapper___2CdIM>input").send_keys("Smith College")
     self.driver.find_element_by_css_selector(".autocomplete__menu___370cg").click()
     time.sleep(5)
     self.driver.get_screenshot_as_file("college.png")
     element = self.driver.find_element_by_xpath(".//*[@id='general']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     element = self.driver.find_element_by_xpath(".//*[@id='diversity']")
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()
     time.sleep(1)
     #element = self.driver.find_element_by_xpath(".//*[@id='teachers']")
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
     self.driver.find_element_by_xpath(".//*[label/text()='Daycare']").click()
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     #ASSERT
     self.driver.find_element_by_css_selector(".geosuggest__input")
     self.driver.get_screenshot_as_file("daycare_empty_tfield.png")


 def search_college_empty_field(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-1']").click()
     #check box
     self.driver.find_element_by_xpath(".//*[label/text()='College']").click()
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[1]/div")
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[2]/div")
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[3]/div")
     self.driver.get_screenshot_as_file("college_empty_tfield.png")

 def search_elementary_empty_field(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-1']").click()
     #check box
     self.driver.find_element_by_xpath(".//*[label/text()='Elementary School']").click()
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     #ASSERT
     self.driver.find_element_by_css_selector(".geosuggest__input")
     self.driver.get_screenshot_as_file("elementary_empty_tfield.png")

 def search_middle_empty_field(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-1']").click()
     # check box
     self.driver.find_element_by_xpath(".//*[label/text()='Middle School']").click()
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     #ASSER
     self.driver.find_elements_by_xpath("//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[1]/div")
     self.driver.find_elements_by_xpath("//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[2]/div")
     self.driver.find_elements_by_xpath("//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[3]/div")
     self.driver.find_element_by_css_selector(".geosuggest__input")
     self.driver.get_screenshot_as_file("middle_empty_tfield.png")

 def search_high_empty_field(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-1']").click()
     # check box
     self.driver.find_element_by_xpath(".//*[label/text()='High School']").click()
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     self.driver.find_element_by_css_selector(".geosuggest__input")
     self.driver.get_screenshot_as_file("high_empty_tfield.png")

 def search_elementary_middle_empty_field(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-1']").click()
     # check box
     self.driver.find_element_by_xpath(".//*[label/text()='Middle School']").click()
     self.driver.find_element_by_xpath(".//*[label/text()='Elementary School']").click()
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     self.driver.find_element_by_css_selector(".geosuggest__input")
     self.driver.get_screenshot_as_file("elementary_middle_empty_tfield.png")

 def search_elementary_high_empty_field(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-1']").click()
     # check box
     self.driver.find_element_by_xpath(".//*[label/text()='Elementary School']").click()
     self.driver.find_element_by_xpath(".//*[label/text()='High School']").click()
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     self.driver.find_element_by_css_selector(".geosuggest__input")
     self.driver.get_screenshot_as_file("elementary_high_empty_tfield.png")

 def search_middle_high_empty_field(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-1']").click()
     # check box
     self.driver.find_element_by_xpath(".//*[label/text()='High School']").click()
     self.driver.find_element_by_xpath(".//*[label/text()='Middle School']").click()
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     self.driver.find_element_by_css_selector(".geosuggest__input")
     self.driver.get_screenshot_as_file("middle_high_empty_tfield.png")

 # ==============================================================================================================
 # ======================================== TEST SEARCH WITH ONE LETTER(Input) AND STATE, ZIPCODE ===============
 # ==============================================================================================================

 def search_d_letter_allstates(self):
     self.driver.find_element_by_css_selector(".homePage__query-wrapper___2CdIM>input").send_keys("d")
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
     self.driver.find_element_by_css_selector(".homePage__query-wrapper___2CdIM>input").send_keys("s")
     # check box
     self.driver.find_element_by_xpath(".//*[label/text()='Daycare']").click()
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     # ASSERT
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label/div")
     self.driver.get_screenshot_as_file("s_letter__daycare_state.png")

 def search_elementary_a_letter_state(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-37']").click()
     self.driver.find_element_by_css_selector(".homePage__query-wrapper___2CdIM>input").send_keys("a")
     # check box
     self.driver.find_element_by_xpath(".//*[label/text()='Elementary School']").click()
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
     self.driver.find_element_by_css_selector(".homePage__query-wrapper___2CdIM>input").send_keys("j")
     # check box
     self.driver.find_element_by_xpath(".//*[label/text()='Middle School']").click()
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
     self.driver.find_element_by_css_selector(".homePage__query-wrapper___2CdIM>input").send_keys("s")
     # check box
     self.driver.find_element_by_xpath(".//*[label/text()='High School']").click()
     time.sleep(1)
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     # ASSERT
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[1]/div")
     self.driver.get_screenshot_as_file("s_letter__high_state.png")

 def search_college_s_letter_state(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-6']").click()
     self.driver.find_element_by_css_selector(".homePage__query-wrapper___2CdIM>input").send_keys("s")
     # check box
     self.driver.find_element_by_xpath(".//*[label/text()='College']").click()
     time.sleep(1)
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(3)
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[1]/div")
     self.driver.get_screenshot_as_file("s_letter__college_state.png")

 def search_elem_middle_s_letter_state(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-6']").click()
     self.driver.find_element_by_css_selector(".homePage__query-wrapper___2CdIM>input").send_keys("s")
     # check box
     self.driver.find_element_by_xpath(".//*[label/text()='Elementary School']").click()
     self.driver.find_element_by_xpath(".//*[label/text()='Middle School']").click()
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
     self.driver.find_element_by_css_selector(".homePage__query-wrapper___2CdIM>input").send_keys("d")
     # check box
     self.driver.find_element_by_xpath(".//*[label/text()='Elementary School']").click()
     self.driver.find_element_by_xpath(".//*[label/text()='High School']").click()
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
     self.driver.find_element_by_css_selector(".homePage__query-wrapper___2CdIM>input").send_keys("s")
     # check box
     self.driver.find_element_by_xpath(".//*[label/text()='Middle School']").click()
     self.driver.find_element_by_xpath(".//*[label/text()='High School']").click()
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
     self.driver.find_element_by_css_selector(".homePage__query-wrapper___2CdIM>input").send_keys("90005")
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
     self.driver.find_element_by_css_selector(".homePage__query-wrapper___2CdIM>input").send_keys("90005")
     time.sleep(1)
     # ASSERT
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[1]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[2]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[3]/div")
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/form/div[1]/div/div[1]/div/label[4]/div")
     self.driver.get_screenshot_as_file("zipcode_no_criteria.png")

 def search_city_no_state(self):
     self.driver.find_element_by_css_selector(".homePage__query-wrapper___2CdIM>input").send_keys("Los Angeles")
     time.sleep(1)
     self.driver.find_element_by_css_selector(".homePage__query-wrapper___2CdIM>input").click()
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
     field = self.driver.find_element_by_css_selector(".homePage__query-wrapper___2CdIM>input")
     field.send_keys(f.random_element(elements=('los','los','los')))
     time.sleep(1)
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     self.driver.implicitly_wait(5)
     self.driver.find_element_by_xpath("//a[text()='Diocese of San Jose Ed Office']")
     #Assert
     N = 4
     actions = ActionChains(self.driver)
     actions.send_keys(Keys.SPACE * N)
     actions.perform()
     time.sleep(2)

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
     self.driver.find_element_by_xpath(".//input[@placeholder='School, City, District or Zipcode']").send_keys("saratoga")
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     self.driver.implicitly_wait(5)
     time.sleep(2)
     actions = ActionChains(self.driver)
     actions.send_keys(Keys.SPACE)
     actions.perform()
     time.sleep(1)
     #Los Gatos High School
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[3]/div/div/div/div[1]/table/tbody/tr[7]/td[6]/button").click()
     time.sleep(6)
     #Saratoga High School
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[3]/div/div/div/div[1]/table/tbody/tr[8]/td[6]/button").click()
     try:
         element = WebDriverWait(self.driver, 10).until(
             EC.visibility_of_element_located((By.CSS_SELECTOR, ".watchList__watch-list__body___10hTS"))
         )
     finally:
      self.driver.implicitly_wait(5)
      time.sleep(1)
      self.driver.get_screenshot_as_file("saved_schools.png")
     #DELETE SAVED

 def save_from_product_page(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-3--option-6']").click()
     self.driver.find_element_by_xpath(".//input[@placeholder='School, City, District or Zipcode']").send_keys("saratoga union")
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     time.sleep(1)
     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
     self.driver.find_element_by_xpath("//*[p/text()='Saratoga Union School District']").click()
     time.sleep(2)
     actions = ActionChains(self.driver)
     actions.send_keys(Keys.ARROW_UP).perform()
     time.sleep(1)
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
     self.driver.find_element_by_xpath(".//input[@placeholder='School, City, District or Zipcode']").send_keys("saratoga")
     self.driver.find_element_by_xpath("//button[@type='submit']").click()
     self.driver.implicitly_wait(5)
     time.sleep(2)
     actions = ActionChains(self.driver)
     actions.send_keys(Keys.SPACE)
     actions.perform()
     time.sleep(1)
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[3]/div/div/div/div[1]/table/tbody/tr[7]/td[6]/button").click()
     try:
           myElem = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[h3/text()='Argonaut Elementary School']")))
           print("OPENED ")
     except TimeoutException:
           print('DIDNT OPENED')
     finally:
      self.driver.find_element_by_xpath("//*[h3/text()='Argonaut Elementary School']").click()
      time.sleep(1)
      self.driver.get_screenshot_as_file("link_in_watchlist.png")
      self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[2]/div[1]/button").click()
      time.sleep(1)

 def all_schools_link(self):
     self.driver.find_element_by_css_selector(".homePage__closed-arrow___2HRFM").click()
     self.driver.find_element_by_xpath(".//*[@id='react-select-2--option-6']").click()
     self.driver.find_element_by_xpath(".//input[@placeholder='School, City, District or Zipcode']").send_keys("Saratoga Union")
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
     self.driver.find_element_by_xpath(".//*[label/text()='Student']").click()
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/form/div[2]/button").click()
     try:
      student = WebDriverWait(self.driver, 0).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".reviewPage__panel___36xzG.panel")))
     finally:
      self.driver.get_screenshot_as_file("register_student.png")

 def register_parent(self):
     time.sleep(1)
     self.driver.find_element_by_xpath(".//*[label/text()='Parent']").click()
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/form/div[2]/button").click()
     try:
      parent = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".homePage__welcome___PPNOA")))
     finally:
      self.driver.get_screenshot_as_file("register_parent.png")

 def register_other(self):
     time.sleep(1)
     self.driver.find_element_by_xpath(".//*[label/text()='Other']").click()
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/form/div[2]/button").click()
     try:
      parent = WebDriverWait(self.driver, 10).until(
         EC.presence_of_element_located((By.CSS_SELECTOR, ".homePage__welcome___PPNOA")))
     finally:
      self.driver.get_screenshot_as_file("register_other.png")

 def register_member(self):
     time.sleep(1)
     self.driver.find_element_by_xpath(".//*[label/text()='Community member']").click()
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/form/div[2]/button").click()
     try:
         parent = WebDriverWait(self.driver, 10).until(
             EC.presence_of_element_located((By.CSS_SELECTOR, ".homePage__welcome___PPNOA")))
     finally:
         self.driver.get_screenshot_as_file("register_member.png")

 def register_teacher_em1_em2ver(self):
     self.driver.find_element_by_xpath(".//*[label/text()='Teacher']").click()
     time.sleep(1)
     got = ActionChains(self.driver)
     got.send_keys(Keys.SPACE)
     got.perform()
     self.driver.find_element_by_id("workEmail").send_keys("drakemac2030@gmail.com") #===== Work EMAIL =====
     time.sleep(1)
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/form/div[2]/button").click()
     try:
         parent = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".panel.verifiedEducatorPage__panel___1V7VW")))
     finally:
         time.sleep(1)
         self.driver.get_screenshot_as_file("register_teacher_em1_em2Ver.png")

 def register_teacher_em1_em2unver(self):
     self.driver.find_element_by_xpath(".//*[label/text()='Teacher']").click()
     time.sleep(1)
     got = ActionChains(self.driver)
     got.send_keys(Keys.SPACE)
     got.perform()
     self.driver.find_element_by_id("workEmail").send_keys("noneteacher@mail.ua")  # ===== Work EMAIL =====
     time.sleep(1)
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/form/div[2]/button").click()
     try:
         parent = WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".popup__popup__body___UKUmr>div>p"),
            "We have registered your personal email address, but we are unable to verify your school email address against our database of active educators."))
     finally:
         time.sleep(1)
         self.driver.get_screenshot_as_file("register_teacher_em1_em2UnVer.png")

 def register_student_verified_email(self):
     time.sleep(1)
     self.driver.find_element_by_xpath(".//*[label/text()='Student']").click()
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/form/div[2]/button").click()
     try:
         student = WebDriverWait(self.driver, 10).until(
             EC.presence_of_element_located((By.CSS_SELECTOR, ".panel.verifiedEducatorPage__panel___1V7VW")))
     finally:
         self.driver.get_screenshot_as_file("register_student_verified_email.png")
        # ===> DELETE_PROFILE
 def register_parent_verified_email(self):
     time.sleep(1)
     self.driver.find_element_by_xpath(".//*[label/text()='Parent']").click()
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/form/div[2]/button").click()
     try:
         student = WebDriverWait(self.driver, 0).until(
             EC.presence_of_element_located((By.CSS_SELECTOR, ".panel.verifiedEducatorPage__panel___1V7VW")))
     finally:
         self.driver.get_screenshot_as_file("register_parent_verified_email.png")
         # ===> DELETE_PROFILE

 def register_other_verified_email(self):
     time.sleep(1)
     self.driver.find_element_by_xpath(".//*[label/text()='Other']").click()
     self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/form/div[2]/button").click()
     try:
         student = WebDriverWait(self.driver, 0).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".panel.verifiedEducatorPage__panel___1V7VW")))
     finally:
         self.driver.get_screenshot_as_file("register_parent_verified_email.png")

#===============================================================================================================
 #===============================================================================================================
 #===============================================================================================================


 #===============================================================================================================
 #======================================== Login, Registration through Pop-up ================================================
 #===============================================================================================================

 def login_pop_write_review_page(self):
     self.driver.find_element_by_link_text("Write a Review").click()
     try:
      popup = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".popup__popup___1SW_t")))
     finally:
       self.driver.find_element_by_id("email").send_keys("test@gmail.com")
     self.driver.find_element_by_id("password").send_keys("123456")
     #remember me
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[5]/div/div[2]/form/div[2]/div/div/div/label").click()
     self.driver.find_element_by_xpath(".//*[@id='root']/div/div[5]/div/div[2]/form/div[2]/button").click()
     #ASSER
     try:
      review_page = WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".reviewPage__headline-from-link___2eHjn"), "Search for your school or district"))
     finally:
      try:
          review_page = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.NAME, "query")))
      finally:
       self.driver.find_element_by_name("query").send_keys("Correct!!!")
      try:
           review_page = WebDriverWait(self.driver, 5).until(
               EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".reviewPage__headline-from-link___2eHjn"), "Search for your school or district"))
      finally:
       time.sleep(1)
       self.driver.get_screenshot_as_file("Login_pop_review.png")

 def login_pop_search_result(self):
      self.driver.find_element_by_css_selector(".homePage__query-wrapper___2CdIM>input").send_keys("saratoga")
      self.driver.find_element_by_css_selector(".button__button___JTdqz.homePage__btn-search___2hBG6").click()
      try:
       resultpage = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[p/text()='Saratoga Elementary School']")))
      finally:
       self.driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div/div/div/div[1]/table/tbody/tr[1]/td[6]/button").click()
      try:
          popup = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".popup__popup___1SW_t")))
          print("OK")
      except TimeoutException:
          print('DIDNT OPENED')
      finally:
       self.driver.find_element_by_id("email").send_keys("test@gmail.com")
       self.driver.find_element_by_id("password").send_keys("123456")
       # remember me
       self.driver.find_element_by_xpath(".//*[@id='root']/div/div[5]/div/div[2]/form/div[2]/div/div/div/label").click()
       self.driver.find_element_by_xpath(".//*[@id='root']/div/div[5]/div/div[2]/form/div[2]/button").click()
       time.sleep(3)
       text = self.driver.find_element_by_css_selector(".watchList__watch-list-card__header___3oaYC").text
       assert text == "Saratoga Elementary School"
       print("Test is correct")
       self.driver.get_screenshot_as_file("login_pop_result.png")
       #precondition DELETE 2

 def login_pop_product(self):
      self.driver.find_element_by_css_selector(".homePage__query-wrapper___2CdIM>input").send_keys("saratoga")
      self.driver.find_element_by_css_selector(".button__button___JTdqz.homePage__btn-search___2hBG6").click()
      try:
         resultpage = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[p/text()='Saratoga Elementary School']")))
      finally:
       self.driver.find_element_by_xpath("//*[p/text()='Saratoga Elementary School']").click()
       try:
           resultpage = WebDriverWait(self.driver, 10).until(
               EC.presence_of_element_located((By.CSS_SELECTOR, ".button__button___JTdqz.institutionPanel__save-btn___2SKd5")))
       finally:
        self.driver.find_element_by_css_selector(".button__button___JTdqz.institutionPanel__save-btn___2SKd5").click()
        self.driver.find_element_by_id("email").send_keys("test@gmail.com")
        self.driver.find_element_by_id("password").send_keys("123456")
        # remember me
        self.driver.find_element_by_xpath(
            ".//*[@id='root']/div/div[5]/div/div[2]/form/div[2]/div/div/div/label").click()
        self.driver.find_element_by_xpath(".//*[@id='root']/div/div[5]/div/div[2]/form/div[2]/button").click()
        time.sleep(3)
        text = self.driver.find_element_by_css_selector(".watchList__watch-list-card__header___3oaYC").text
        assert text == "Saratoga Elementary School"
        print("Test is correct")
        self.driver.get_screenshot_as_file("login_pop_product.png")
        # precondition DELETE 2

  #def register_pop_review_page(self):
      #self.driver.find_element_by_link_text("Write a Review").click()
      #try:
      #    popup = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".popup__popup___1SW_t")))
      #finally:
