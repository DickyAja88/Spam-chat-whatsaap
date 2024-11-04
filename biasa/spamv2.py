import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Atur opsi untuk Chrome
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=C:\\Users\\Dicky\\AppData\\Local\\Google\\Chrome\\User Data\\Default")  # Pastikan direktori data pengguna benar
service = Service('E:\\Spam-chat-whatsapp\\biasa\\chromedriver-win64\\chromedriver.exe')

# Inisialisasi webdriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Buka WhatsApp Web
driver.get('https://web.whatsapp.com')

try:
    # Tunggu elemen yang menunjukkan bahwa pengguna sudah login
    time.sleep(10)
    
    #masukkan target yang menjadi penerima pesan (whatsappweb memiliki case sensitive jadi pastikan nama target benar)
    title_text = "leCollégial."
    #isi pesan yang akan diinputkan
    pesan = 'nyoba'
    #jumlah pesan yang ingin dikirim
    jumlah_pesan = 5 

    # Temukan elemen dengan title yang sesuai
    elemen = driver.find_element(By.XPATH, f".//span[@title='{title_text}']")
    elemen.click()

    for i in range(jumlah_pesan):
        input_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
        )
        input_box.send_keys(pesan)  
        time.sleep(2)  
        input_box.send_keys(Keys.ENTER)

except Exception as e:
    print(f"Terjadi kesalahan: {e}")

finally:
    # Tunggu beberapa detik sebelum menutup browser
    time.sleep(5)
    driver.quit()
