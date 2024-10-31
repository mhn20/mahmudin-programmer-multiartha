import pickle
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# URL login Shopee (atau website serupa)
url_login = "https://shopee.co.id/buyer/login"

# Inisialisasi WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Fungsi untuk login dan menyimpan cookie


def login_and_save_session():
    # Buka halaman login
    driver.get(url_login)
    time.sleep(5)  # Tunggu halaman selesai dimuat

    # Temukan elemen input untuk username/email dan password
    # Sesuaikan dengan 'name' dari input username
    username_input = driver.find_element(By.NAME, "loginKey")
    # Sesuaikan dengan 'name' dari input password
    password_input = driver.find_element(By.NAME, "password")

    # Isi username dan password
    username_input.send_keys("your_username")  # Ganti dengan username
    password_input.send_keys("your_password")  # Ganti dengan password

    # Klik tombol login
    login_button = driver.find_element(
        By.XPATH, '//button[contains(text(),"Log in")]')
    login_button.click()

    # Tunggu beberapa saat untuk verifikasi login
    time.sleep(10)

    # Simpan cookie ke file setelah login berhasil
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
    print("Cookie berhasil disimpan!")

# Fungsi untuk memuat sesi dari cookie


def load_session():
    driver.get(url_login)  # Muat halaman awal sebelum menggunakan cookie

    # Muat cookie yang sudah disimpan
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

    # Refresh halaman untuk melihat apakah login berhasil dengan cookie
    driver.refresh()
    time.sleep(5)
    print("Session berhasil dipertahankan dengan cookie!")

# Fungsi untuk menangani CAPTCHA atau 2FA (jika muncul)


def handle_captcha():
    # Placeholder: Anda mungkin perlu menggunakan layanan pengenalan CAPTCHA
    print("Deteksi CAPTCHA/2FA. Memerlukan intervensi manual atau menggunakan layanan CAPTCHA.")


# Eksekusi
try:
    # Jika file cookie tidak ada, lakukan login
    login_and_save_session()
except Exception as e:
    print(f"Error saat login: {e}")
finally:
    # Tutup browser
    driver.quit()
