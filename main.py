from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
# options = webdriver.ChromeOptions()
# options.add_extension(r'C:\Users\maoliveira\OneDrive - Trident Energy Management LTD\Documents\My files\free')

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.maximize_window()
navegador.execute_script('Object.defineProperty(navigator, "webdriver", {get: () => false});')

# https://chrome.google.com/webstore/detail/recaptcha-autoclick/caahalkghnhbabknipmconmbicpkcopl
# navegador.get('https://chrome.google.com/webstore/detail/recaptcha-autoclick/caahalkghnhbabknipmconmbicpkcopl')
input()
# navegador.get('https://chrome.google.com/webstore/detail/buster-captcha-solver-for/mpbjkejclgfgadiemmefgebjfooflfhl')
input()
# https://chrome.google.com/webstore/detail/buster-captcha-solver-for/mpbjkejclgfgadiemmefgebjfooflfhl

input()
navegador.get('https://web.trf3.jus.br/consultas/Internet/ConsultaReqPag/Consultar')
navegador.find_element(By.XPATH, '//*[@id="ProcessoOrigem"]').send_keys('02789896120214039900')
pyautogui.sleep(5)
while navegador.find_element(By.XPATH, '//*[@id="pesquisar"]').is_enabled() == False:
    pyautogui.click(x=595, y=971)
    print(navegador.find_element(By.XPATH, '//*[@id="pesquisar"]').is_enabled())

navegador.find_element(By.XPATH, '//*[@id="pesquisar"]').click()
# print(navegador.find_element(By.XPATH, '//*[@id="rc-imageselect"]/div[2]/div[1]/div[1]/div/strong').text)
# element = navegador.find_element(By.XPATH, '//div[@id="recaptcha-checkbox-border"]')
# element.click()

# pyautogui.click(x=387, y=850)
input()
