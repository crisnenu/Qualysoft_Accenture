import unittest
import os
from Excercise1.MainTests.MyFavoriteEshop import MyFavoriteEshopTest

# get the directory path to output report file
dir = os.getcwd()

# get all tests from SearchText and HomePageTest class
eshop_test = unittest.TestLoader().loadTestsFromTestCase(MyFavoriteEshopTest)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([eshop_test])

# open the report file
outfile = open(dir + "\SeleniumPythonTestSummary.html", "w")
