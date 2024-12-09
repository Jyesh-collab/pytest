import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import pytest
import time
from PageObject.qualitrix_page_object import Qualitrix_page_object_one


@pytest.mark.usefixtures("browser_cbt")

class Test_Qualitrix_e2e:

    def test_homepage_validation(self, readJson):
        homepage = Qualitrix_page_object_one(self.driver)  # Activating the driver which we have created in supporting file (qualitrix_page_object.py).
        homepage.launch_the_app(readJson['url_qualitrix'])
        homepage.Validate_header_menu()
        homepage.Validate_button_color()

