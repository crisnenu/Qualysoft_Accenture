import unittest

from Excercise1.GoToBaseUrl import GoToUrl

from Excercise1.BaseFunctions.Site import Site
from Excercise1.Platform_Contants import Platform

my_favorite_site = "emag.ro"
site = Site()


class Main(GoToUrl, unittest.TestCase):

    def setUp(self):
        GoToUrl.setUp(self, my_favorite_site, Platform.CHROME)

    def test_eshop(self):
        print("Wait until the main page is visible")
        site.mainPageIsVisible(self.web_browser)
        print("The main page is visible")

        print("Select a category")
        site.selectACategory(self.web_browser, 1, "laptop-tablete-telefoane")
        print("Laptops, tablets and phones are selected")

        print("Select a sub-category")
        site.selectTheSubcategory(self.web_browser, "apple")
        print("Apple is choosed as a subcategory")

        print("Select a sub-sub-category")
        site.selectTheSubSubcategory(self.web_browser, "telefoane-mobile")
        print("Mobile phones are choosed as a sub-subcategory")

        print("Sort by the Decreased Price")
        site.sortByOption(self.web_browser, 3)
        print("The items was sorted decreased by Price")

        print("Add the most expensive 2 Items in the shopping cart")
        print("Add the 1st item")
        site.addTheFirstItem(self.web_browser)
        print("Add the 2nd item")
        site.addTheSecondItem(self.web_browser)

        print("Check the cart")
        site.checkTheCart(self.web_browser)

        print("Check that the most Expensive 2 Items are added to Shopping Cart")
        site.checkTheMostExpensiveItemsAreAddedToShoppingCart(self.web_browser, 2)
        print("The most expensive 2 Items from Iphone category are in the shopping cart!")

    def tearDown(self):
        print("Thank you for your attention!")


if __name__ == '__main__':
    unittest.main()
