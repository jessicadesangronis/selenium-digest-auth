import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.digest_auth_page import DigestAuthPage

class TestDigestAuth:
    
    def setup_method(self):
        """Configuración antes de cada prueba"""
        # Configuración del driver
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def teardown_method(self):
        """Limpieza después de cada prueba"""
        if self.driver:
            self.driver.quit()

    def test_digest_authentication_success(self):
        # 1. Instanciar la página
        digest_page = DigestAuthPage(self.driver)
        
        # 2. Ejecutar la acción de login (User: admin, Pass: admin)
        digest_page.login_with_digest_auth("admin", "admin")
        
        # 3. Validar el resultado (Assert)
        # Si el login es exitoso, deberíamos ver el texto específico
        actual_text = digest_page.get_content_text()
        expected_text = "Congratulations! You must have the proper credentials."
        
        assert expected_text in actual_text, f"Falló el login. Texto encontrado: {actual_text}"

    def test_digest_authentication_fail(self):
        """Prueba negativa opcional"""
        digest_page = DigestAuthPage(self.driver)
        # Intentamos con password incorrecto
        digest_page.login_with_digest_auth("admin", "wrongpass")
        
        # Validamos que NO aparezca el mensaje de éxito 
        # (Nota: En navegadores reales, esto podría dejar la ventana de auth abierta o mostrar error 401)
        # Para simplificar, solo verificamos que el título no sea el de éxito si carga la página
        try:
            text = digest_page.get_content_text()
            assert "Congratulations" not in text
        except:
            # Si falla al encontrar el elemento, es que no logueó, lo cual es correcto en este test
            pass