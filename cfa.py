from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import date
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import password as pw

opts = webdriver.ChromeOptions()
opts.add_argument("--user-data-dir=/Users/brianzhu/Library/Application Support/Google/Chrome/Profile 3")
driver = webdriver.Chrome(options = opts, executable_path="chromedriver")
driver.get("https://www.chick-fil-a.com/missedtransaction")
email = pw.email
password = pw.password

if "SIGN IN" in driver.title:
  username = driver.find_element(By.NAME, "pf.username")
  username.clear()
  username.send_keys(email)
  passfield = driver.find_element(By.NAME, "pf.pass")
  passfield.clear()
  passfield.send_keys(password)
  passfield.send_keys(Keys.RETURN)

rnum = input()
todate = date.today().strftime("%m/%d/%Y")
onum = input()
total = input()

if "MissedTransaction" in driver.title:
  element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.NAME, "RestaurantNumber"))
  )
  rnum_input = driver.find_element(By.NAME, "RestaurantNumber")
  date_input = driver.find_element(By.NAME, "Date")
  onum_input = driver.find_element(By.NAME, "OrderNumber")
  total_input = driver.find_element(By.NAME, "OrderTotal")
  rnum_input.clear()
  rnum_input.send_keys(rnum)
  js = f"document.getElementById('Date').setAttribute('value','{todate}')"
  driver.execute_script(js)
  onum_input.clear()
  onum_input.send_keys(int(onum))
  total_input.clear()
  total_input.send_keys(total)
  total_input.send_keys(Keys.RETURN)
  driver.get("https://www.chick-fil-a.com/missedtransaction")

input()



driver.close()
