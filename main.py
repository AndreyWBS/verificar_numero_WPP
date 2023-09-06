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


planilha_de_numeros_env = {
    "numero": [],
    "codigo": []
}
planilha_de_numeros_Erro = {
    "numero": [],
    "codigo": []
}

#iniciando o google
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
wait = WebDriverWait(driver, 120)
elemento = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '#app > div > div > div._2Ts6i._3RGKj > header > div._3WByx')))
time.sleep(10)


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


def escrever(seletor, txt, driver):
    wait = WebDriverWait(driver, 25)
    elemento = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, seletor)))
    for letra in txt:
        if letra == "#":
            driver.find_element(By.CSS_SELECTOR, seletor).send_keys(Keys.CONTROL, Keys.ENTER)
        else:
            driver.find_element(By.CSS_SELECTOR, seletor).send_keys(letra)
    driver.find_element(By.CSS_SELECTOR, seletor).send_keys(Keys.ENTER)



def gerarPLanilahas(nomeWPP):
    df_Planilha_com_ERRO = pd.DataFrame(planilha_de_numeros_Erro)
    df_Planilha_com_ENV = pd.DataFrame(planilha_de_numeros_env)
    nome_env = f"{nomeWPP}numeros_env.xlsx"
    nome_erro = f"{nomeWPP}numeros_erros.xlsx"
    caminho_planilha = r"C:\Users\Micro\Desktop\planilhasGeradasBOT\acionamentosWPP\pla"

    df_Planilha_com_ERRO.to_excel(caminho_planilha + nome_erro, index=False)
    df_Planilha_com_ENV.to_excel(caminho_planilha + nome_env, index=False)


def comecar(driver, caminho_pla_numeros,ondeMandarNumeros):
    numeros_df = pd.read_excel(caminho_pla_numeros)
    try:

        nomeCVS = procurarElementscomseletor("._21S-L .l7jjieqr", driver)

        for i, mensagem in enumerate(numeros_df['numero']):


            numeroTELL = numeros_df.loc[i, "numero"]
            codigo = numeros_df.loc[i, "codigo"]

            print(str(numeroTELL))

            for elemt in nomeCVS:
                print(ondeMandarNumeros)
                if elemt.text == ondeMandarNumeros:
                    print("oi")
                    elemt.click()
                    escrever("#main .iq0m558w", str(numeroTELL), driver)
                    conversa = procurarElementscomseletor("._1jHIY , .ooty25bp", driver)

    except:
        print("não deu")