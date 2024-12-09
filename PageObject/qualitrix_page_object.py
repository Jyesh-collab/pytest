from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.color import Color
import pytest
import time
from Locators import Qualitrix_home
from PageObject import common


class Qualitrix_page_object_one:

    def __init__(self, driver):
        self.driver = driver

    def launch_the_app(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        print("Qualitrix Application is launched Successfully ... ..... PASS")

    def Validate_header_menu(self):
        assert len(self.driver.find_elements(By.XPATH, Qualitrix_home.Qualitrix_logo())) == 1
        assert self.driver.find_element(By.XPATH, Qualitrix_home.Qualitrix_logo()).is_displayed() == True
        print ("Qualitrix logo is present")

    def Validate_button_color(self):
       
    #validate get a quote button text color and background color

       Get_a_quote= self.driver.find_element(By.XPATH, Qualitrix_home.get_a_quote())
       Get_a_quote_color= Get_a_quote.value_of_css_property("color")
       Get_a_quote_bg_color= Get_a_quote.value_of_css_property("background-color")

    #    print(Get_a_quote_color)
    #    print(Get_a_quote_bg_color)

    #    print(Color.from_string(Get_a_quote_color).hex)
    #    print(Color.from_string(Get_a_quote_bg_color).hex)

       print("Get a quote text color is: " +common.color_picker((Color.from_string(Get_a_quote_color).hex)))
       print("Get a quote background color is: " +common.color_picker((Color.from_string(Get_a_quote_bg_color).hex)))

   #validate 

    #    padding = Get_a_quote.value_of_css_property(padding)
    #    text_align = Get_a_quote.gvalue_of_css_property(text_align)
    #    print(padding + text_align)

      

#### Look from recording 7th Dec