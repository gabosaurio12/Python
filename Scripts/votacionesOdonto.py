from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://forms.gle/aH4aq2ja2gxgeAQx5'
opcion_deseada = 5
repeticiones = 1
print("Se harán: ", repeticiones, " envíos")

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)

for i in range(repeticiones):
	driver.get(url)

	opcion = wait.until(EC.element_to_be_clickable((By.XPATH, f'(//div[@role="radio"])[{opcion_deseada}]')))
	opcion.click()

	enviar = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Enviar"]')))
	enviar.click()

	wait.until(EC.presence_of_element_located((By.XPATH, '//a[text()="Enviar otra respuesta"]')))

print(f'{repeticiones} envios completados')
driver.quit()
