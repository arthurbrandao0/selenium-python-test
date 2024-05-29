from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    # Configurar opções do Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ativar modo headless
    chrome_options.add_argument("--disable-gpu")  # Desativar GPU (recomendado para o modo headless)
    chrome_options.add_argument("--no-sandbox")  # Desativar o sandbox (necessário para algumas configurações de CI)
    chrome_options.add_argument("--disable-dev-shm-usage")  # Superar problemas de recursos limitados

    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

def after_all(context):
    context.driver.close()