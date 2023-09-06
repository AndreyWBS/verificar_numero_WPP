import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import pandas as pd

caminho_pla = ""
numeros_df = pd.read_excel(caminho_pla)

#iniciando o google
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
wait = WebDriverWait(driver, 120)
elemento = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '#app > div > div > div._2Ts6i._3RGKj > header > div._3WByx')))
time.sleep(10)

