from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class DigestAuthPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        # URL base sin credenciales
        self.base_url = "https://the-internet.herokuapp.com/digest_auth"
        # Localizador del mensaje de éxito
        self.success_message_locator = (By.TAG_NAME, "p")

    def login_with_digest_auth(self, username, password):
        """
        Realiza el login inyectando las credenciales en la URL.
        Formato: https://user:pass@host/path
        """
        # Separamos el protocolo del resto de la URL
        protocol = "https://"
        url_without_protocol = self.base_url.replace(protocol, "")
        
        # Construimos la URL con credenciales
        auth_url = f"{protocol}{username}:{password}@{url_without_protocol}"
        
        # Navegamos a la URL modificada
        self.driver.get(auth_url)

    def get_content_text(self):
        """Obtiene el texto del párrafo principal para verificar el éxito"""
        return self.driver.find_element(*self.success_message_locator).text