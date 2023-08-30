from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# to install driver for first run, other brower check https://github.com/SergeyPirogov/webdriver_manager 
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

print_header = True
sep = ","
url = 'https://kodepos.nomor.net/_kodepos.php?_i=kota-kodepos'

if print_header: 
    print(sep.join(("no","kota", "kode_wilayah", "provinsi")))


driver.get(url)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'header_mentok')))

table_header = driver.find_element(By.CLASS_NAME, 'header_mentok')

table_data = table_header.find_element(By.XPATH, "following-sibling::*[1]")
rows = table_data.find_elements(By.TAG_NAME, 'tr')

# get the data
for row in rows:    
    cols = row.find_elements(By.TAG_NAME, 'td')
    no = cols[0].get_attribute('innerHTML')
    dt2 = cols[1].get_attribute('innerHTML')  # kota atau kabupaten
    kota = cols[2].find_element(By.TAG_NAME, 'a').get_attribute('innerHTML') 
    kode_wilayah = cols[7].find_element(By.TAG_NAME, 'b').get_attribute('innerHTML')
    provinsi = cols[8].find_element(By.TAG_NAME, 'a').get_attribute('innerHTML') 

    rec = sep.join((no,dt2 + ' ' + kota, kode_wilayah, provinsi))
    print(rec)


