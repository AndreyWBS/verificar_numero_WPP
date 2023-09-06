import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import pandas as pd

caminho_pla_numeros = ""
caminho_pla_num_ENV = ""
caminho_pla_num_ERRO = ""
numeros_df = pd.read_excel(caminho_pla_numeros)

#iniciando o google
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
wait = WebDriverWait(driver, 120)
elemento = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '#app > div > div > div._2Ts6i._3RGKj > header > div._3WByx')))
time.sleep(10)

planilha_de_numeros_env = {
    "numero": [],
    "codigo": []
}
planilha_de_numeros_Erro = {
    "numero": [],
    "codigo": []
}


def procurarElementocomSeletor(seletor, driver):
    wait = WebDriverWait(driver, 120)
    elemento = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, seletor)))
    return driver.find_element(By.CSS_SELECTOR, seletor)


def procurarElementscomseletor(seletor, driver):
    wait = WebDriverWait(driver, 25)
    elemento = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, seletor)))
    return driver.find_elements(By.CSS_SELECTOR, seletor)


def clicar_seletor_elemento(seletor, elementoP, driver):
    wait = WebDriverWait(driver, 25)
    elemento = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, seletor)))
    elementoP.find_element(By.CSS_SELECTOR, seletor).click()



def gerarPLanilahas(nomeWPP):
    df_Planilha_com_ERRO = pd.DataFrame(planilha_de_numeros_Erro)
    df_Planilha_com_ENV = pd.DataFrame(planilha_de_numeros_env)
    nome_env = f"{nomeWPP}numeros_env.xlsx"
    nome_erro = f"{nomeWPP}numeros_erros.xlsx"
    caminho_planilha = r"C:\Users\Micro\Desktop\planilhasGeradasBOT\acionamentosWPP\pla"

    df_Planilha_com_ERRO.to_excel(caminho_planilha + nome_erro, index=False)
    df_Planilha_com_ENV.to_excel(caminho_planilha + nome_env, index=False)
