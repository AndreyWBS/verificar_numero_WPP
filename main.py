import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import pandas as pd

caminho_pla_numeros = r"C:\Users\Micro\Desktop\planilhasBot\verificarNumeros\verificarNum.xlsx"
caminho_pla_num = r"C:\Users\Micro\Desktop\planilhasGeradasBOT\numerosParaMensagemCCK"

ondeMandarNumeros = "+55 48 9696-1694"

planilha_de_numeros_env = {
    "numero": [],
    "codigo": []
}
planilha_de_numeros_Erro = {
    "numero": [],
    "codigo": []
}

# iniciando o google
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
wait = WebDriverWait(driver, 120)
elemento = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '#app > div > div > div._2Ts6i._3RGKj > header > div._3WByx')))


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


def gerarPLanilahas(caminhopla):
    df_Planilha_com_ERRO = pd.DataFrame(planilha_de_numeros_Erro)
    df_Planilha_com_ENV = pd.DataFrame(planilha_de_numeros_env)

    df_Planilha_com_ERRO.to_excel(caminhopla + r"\num_erro.xlsx", index=False)
    df_Planilha_com_ENV.to_excel(caminhopla + r"\num_env.xlsx", index=False)


def obterPrimeiraLinha(texto):
    linhas = texto.split("\n")
    return linhas[0]


def comecar(driver, caminho_pla_numeros, ondeMandarNumeros):
    # try:
    numeros_df = pd.read_excel(caminho_pla_numeros)

    nomeCVS = procurarElementscomseletor("._21S-L .l7jjieqr", driver)

    for i, mensagem in enumerate(numeros_df['numero']):

        numeroTELL = numeros_df.loc[i, "numero"]
        codigo = numeros_df.loc[i, "codigo"]

        print(str(numeroTELL))

        for elemt in nomeCVS:
            # print(elemt.text)
            if elemt.text == ondeMandarNumeros:
                elemt.click()
                escrever("#main .iq0m558w", str(numeroTELL), driver)
                conversa = procurarElementscomseletor("._1jHIY , .ooty25bp", driver)

                for linha in conversa:

                    linhatxt = obterPrimeiraLinha(linha.text)

                    if linhatxt == str(numeroTELL):
                        print("esse numero é igual")

                        clicar_seletor_elemento("span._11JPr.selectable-text.copyable-text > span > a", linha,
                                                driver)

                        try:
                            conversarCOM = procurarElementocomSeletor(".iWqod._1MZM5._2BNs3.nqtxkp62.btzf6ewn",
                                                                      driver)
                            if conversarCOM.get_attribute("aria-label") == "Conversar com ":
                                print("esse numero da para mandar")
                                planilha_de_numeros_env["numero"].append(str(numeroTELL))
                                planilha_de_numeros_env["codigo"].append(str(codigo))
                                gerarPLanilahas(caminho_pla_num)
                                break
                        except:
                            planilha_de_numeros_Erro["numero"].append(str(numeroTELL))
                            planilha_de_numeros_Erro["codigo"].append(str(codigo))
                            print("esse numero não da")
                            gerarPLanilahas(caminho_pla_num)
                            break

                break
    """except Exception as e:
        print("o erro é : ", e)"""


comecar(driver, caminho_pla_numeros, ondeMandarNumeros)
