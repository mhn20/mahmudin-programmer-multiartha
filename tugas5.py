import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestChatGPTLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Inisialisasi WebDriver
        cls.driver = webdriver.Chrome()  # Ganti dengan driver sesuai browser Anda
        cls.driver.get("https://chat.openai.com")  # URL untuk ChatGPT

    def test_login(self):
        driver = self.driver

        # Mencari dan mengisi kolom email
        # Ganti dengan selector yang tepat
        email_input = driver.find_element(By.NAME, "email")
        # Ganti dengan email yang valid
        email_input.send_keys("your_email@example.com")
        email_input.send_keys(Keys.RETURN)

        # Mencari dan mengisi kolom password
        time.sleep(2)  # Tunggu agar elemen muncul
        # Ganti dengan selector yang tepat
        password_input = driver.find_element(By.NAME, "password")
        # Ganti dengan password yang valid
        password_input.send_keys("your_password")
        password_input.send_keys(Keys.RETURN)

        # Tunggu hingga dashboard muncul
        time.sleep(5)  # Tunggu beberapa detik
        # Pastikan judul halaman sesuai
        self.assertIn("Dashboard", driver.title)

    def test_access_dashboard(self):
        driver = self.driver

        # Verifikasi apakah elemen dashboard dapat diakses
        time.sleep(5)  # Tunggu untuk memuat halaman
        dashboard_element = driver.find_element(
            By.XPATH, "//div[@class='dashboard']")  # Ganti dengan selector yang tepat
        self.assertIsNotNone(dashboard_element)

    def test_chatgpt_response(self):
        driver = self.driver

        # Mencari input untuk chat
        time.sleep(2)  # Tunggu untuk memuat halaman
        # Ganti dengan selector yang tepat
        chat_input = driver.find_element(
            By.XPATH, "//textarea[@id='chat-input']")
        chat_input.send_keys("Hello, ChatGPT!")  # Mengirim pesan
        chat_input.send_keys(Keys.RETURN)

        # Tunggu hingga respons muncul
        time.sleep(5)  # Tunggu beberapa detik
        response_element = driver.find_element(
            By.XPATH, "//div[@class='chat-response']")  # Ganti dengan selector yang tepat
        # Sesuaikan dengan respons yang diharapkan
        self.assertIn("Hi!", response_element.text)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  # Menutup browser setelah pengujian selesai


if __name__ == "__main__":
    unittest.main()
