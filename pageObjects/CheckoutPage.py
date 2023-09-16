# --CheckoutPage

from selenium.webdriver.common.by import By

#it created pom called get card title
from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self,driver):
        self.driver=driver

    #driver.find_elements_by_css_selector(".card-title a")
    # driver.find_element_by_xpath("//button[@class='btn btn-success']")
    cardTitle=(By.CSS_SELECTOR,".card-title a")
    cardFooter=(By.CSS_SELECTOR,".card-footer button")
    checkOut=(By.XPATH,"//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle) # * made serielized

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter) # * made serielized

    def checkOutItems(self):
         self.driver.find_element(*CheckOutPage.checkOut).click() # * made serielized
         confirmPage=ConfirmPage(self.driver)
         return confirmPage #confirmPage has to be constructor otherwise it ll give an error
