from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class Fundation(object):
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.fundaciondiabetes.org/sabercomer/tabla_de_raciones_de_hidratos_de_carbono#filtro'
        self.id_filter = 'cboGrupo'
        self.xpath_rows_elements = 'tbody>tr'
        self.xpath_title_food = '//*[@id="divPagina"]/main/div[1]/div/div[2]/article/h2/span'

    def get_items(self):
        options_names = []
        foods_groups = Select(self.driver.find_element_by_id(self.id_filter))
        for food_group in foods_groups.options:
            options_names.append(food_group.text)
        return options_names, foods_groups

    def changeGroup(self):
        options_names, foods_groups = self.get_items()

        for option in options_names:
            foods_groups.select_by_visible_text(option)
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.xpath, self.xpath_title_food)))
