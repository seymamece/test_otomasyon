from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Test_Sauce():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    sleep(5)
    
    def empty_login(self):
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID, "password")
        sleep(2)
        usernameInput.send_keys()
        passwordInput.send_keys()
        sleep(2)
        loginBtn = self.driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        errorMessage = self.driver.find_element(
            By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"TEST SONUCU: {testResult}")

    def empty_login_password(self):
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID, "password")
        sleep(2)
        usernameInput.send_keys("a")
        passwordInput.send_keys()
        sleep(2)
        loginBtn = self.driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        errorMessage = self.driver.find_element(
            By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"TEST SONUCU: {testResult}")

    def invalid_login(self):
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID, "password")
        sleep(2)
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn = self.driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        errorMessage = self.driver.find_element(
            By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU: {testResult}")

    def x_icon(self):
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID, "password")
        sleep(2)
        usernameInput.send_keys()
        passwordInput.send_keys()
        sleep(2)
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)
        cancelBtn = self.driver.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        cancelBtn.click()

    def enter_invertory(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.get("https://www.saucedemo.com/inventory.html")
        sleep(2)
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID, "password")
        sleep(2)
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(3)
        inventoryList = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"There are {len(inventoryList)} items in list")


Class = Test_Sauce()
Class.empty_login()
Class.empty_login_password()
Class.invalid_login()
Class.x_icon()
Class.enter_invertory()

    
