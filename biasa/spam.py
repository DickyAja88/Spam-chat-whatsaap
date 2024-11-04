import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Atur opsi untuk Chrome
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=C:\\Users\\Dicky\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
service = Service('E:\\Spam-chat-whatsapp\\biasa\\chromedriver-win64\\chromedriver.exe')

# Inisialisasi webdriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# membuka whatsapp web
driver.get('https://web.whatsapp.com')

# Tunggu pengguna untuk memindai kode QR
print("Silakan pindai kode QR untuk masuk ke WhatsApp Web.")
time.sleep(30)

#masukkan target yang menjadi penerima pesan (whatsappweb memiliki case sensitive jadi pastikan nama target benar)
title_text = "leCollégial."
#isi pesan yang akan diinputkan
pesan = 'nyoba'
#jumlah pesan yang ingin dikirim
jumlah_pesan = 5 

try:
    div_container = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "_ak8q"))
    )
    
    elemen = div_container.find_element(By.XPATH, f".//span[@title='{title_text}']")
    elemen.click()

    for i in range(jumlah_pesan):
        input_box = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
        )
        input_box.send_keys(f"{pesan} #{i + 1}")  # Variasi pesan
        time.sleep(2)
        input_box.send_keys(Keys.ENTER)

except Exception as e:
    print(f"Terjadi kesalahan: {e}")


time.sleep(5)
driver.quit()

