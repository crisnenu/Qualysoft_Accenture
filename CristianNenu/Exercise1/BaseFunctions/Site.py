import time
from unittest import TestCase

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Site:
    def check_the_page(self, web_browser, name):
        TestCase.assertIn(self, name, web_browser.current_url)

    def waitXUntilElementIsVisibleBy(self, web_browser, timeSec, byType, name):
        WebDriverWait(web_browser, timeSec).until(EC.presence_of_element_located((byType, name)))

    def waitXUntilElementsAreVisibleBy(self, web_browser, timeSec, byType, name):
        WebDriverWait(web_browser, timeSec).until(EC.presence_of_all_elements_located((byType, name)))

    def mainPageIsVisible(self, web_browser):
        self.check_the_page(web_browser, "emag")
        self.waitXUntilElementIsVisibleBy(web_browser, 10, By.ID, "masthead")

    def selectACategory(self, web_browser, numberInList, name):
        self.waitXUntilElementsAreVisibleBy(web_browser, 10, By.CLASS_NAME, "megamenu-list-department__department-name")
        item_category = web_browser.find_elements_by_class_name("megamenu-list-department__department-name")
        item_category.pop(numberInList).click()
        self.check_the_page(web_browser, name)

    def selectTheSubcategory(self, web_browser, name):
        self.waitXUntilElementIsVisibleBy(web_browser, 10, By.CLASS_NAME, "widget-column-type-banner_1_1")
        apple_shop = web_browser.find_element_by_class_name("widget-column-type-banner_1_1")
        apple_shop.click()
        self.check_the_page(web_browser, name)

    def selectTheSubSubcategory(self, web_browser, name):
        self.waitXUntilElementsAreVisibleBy(web_browser, 10, By.CLASS_NAME, "apple-category-image")
        iphone_shop = web_browser.find_elements_by_class_name("apple-category-image")
        iphone_shop.pop(0).click()
        self.check_the_page(web_browser, name)

    def sortByOption(self, web_browser, option):
        self.waitXUntilElementIsVisibleBy(web_browser, 10, By.CLASS_NAME, "gtm_ejaugtrtnc")
        sort_field = web_browser.find_element_by_class_name("gtm_ejaugtrtnc")
        sort_field.click()

        self.waitXUntilElementsAreVisibleBy(web_browser, 10, By.CLASS_NAME, "js-sort-option")
        sort_list = web_browser.find_elements_by_class_name("js-sort-option")
        sort_list.pop(option).click()
        time.sleep(2)
        self.waitXUntilElementIsVisibleBy(web_browser, 10, By.CLASS_NAME, "js-accept")
        web_browser.find_element_by_class_name("js-accept").click()
        time.sleep(2)

    def addTheFirstItem(self, web_browser):
        self.waitXUntilElementsAreVisibleBy(web_browser, 10, By.CLASS_NAME, "card-item")
        web_browser.find_elements_by_class_name("card-item").pop(0).find_elements_by_class_name(
            "yeahIWantThisProduct").pop(0).click()
        self.closeThePopup(web_browser)

    def addTheSecondItem(self, web_browser):
        self.waitXUntilElementsAreVisibleBy(web_browser, 10, By.CLASS_NAME, "card-item")
        web_browser.find_elements_by_class_name("card-item").pop(1).find_elements_by_class_name(
            "yeahIWantThisProduct").pop(0).click()
        self.closeThePopup(web_browser)

    def closeThePopup(self, web_browser):
        print("Close the popup")
        self.waitXUntilElementsAreVisibleBy(web_browser, 10, By.CLASS_NAME, "gtm_6046yfqs")
        web_browser.find_elements_by_class_name("gtm_6046yfqs").pop(0).click()

    def checkTheCart(self, web_browser):
        web_browser.find_element_by_id("my_cart").click()
        self.check_the_page(web_browser, "cart")

    def checkTheMostExpensiveItemsAreAddedToShoppingCart(self, web_browser, nrOfItems):
        self.waitXUntilElementsAreVisibleBy(web_browser, 10, By.CLASS_NAME, "main-product-details-container")
        number_of_existing_items = len(web_browser.find_elements_by_class_name("main-product-details-container"))
        assert number_of_existing_items == nrOfItems, \
            "number greater than {} expected, got: {}".format(nrOfItems,number_of_existing_items)
