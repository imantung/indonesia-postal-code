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
page = 1
url = 'https://kodepos.nomor.net/_kodepos.php?_i=desa-kodepos'

if print_header: 
    print(sep.join(("no","kode_pos", "kelurahan", "kode_wilayah", "kecamatan", "kota")))

while len(url) > 0: 
    driver.get(url)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'header_mentok')))

    table_header = driver.find_element(By.CLASS_NAME, 'header_mentok')

    table_data = table_header.find_element(By.XPATH, "following-sibling::*[1]")
    rows = table_data.find_elements(By.TAG_NAME, 'tr')

    # get the data
    for row in rows:    
        cols = row.find_elements(By.TAG_NAME, 'td')
        kode_pos = cols[1].find_elements(By.TAG_NAME, 'a')[1].get_attribute('innerHTML')
        if len(kode_pos) > 0:
            no = cols[0].get_attribute('innerHTML')
            kelurahan = cols[2].find_element(By.TAG_NAME, 'a').get_attribute('innerHTML') 
            kode_wilayah = cols[3].find_element(By.TAG_NAME, 'a').get_attribute('innerHTML') 
            kecamatan = cols[4].find_element(By.TAG_NAME, 'a').get_attribute('innerHTML') 
            dt2 = cols[5].get_attribute('innerHTML')  # kota atau kabupaten
            kota = cols[6].find_element(By.TAG_NAME, 'a').get_attribute('innerHTML') 

            rec = sep.join((no,kode_pos, kelurahan, kode_wilayah, kecamatan, dt2 + ' ' + kota))
            print(rec)

    # get next page link
    url = ''
    links = table_header.find_element(By.XPATH, "..//..").find_elements(By.CSS_SELECTOR, 'a.tpage')
    for link in links:
        if link.get_attribute('innerHTML') == str(page + 1):
            url = link.get_attribute('href')
            i = i + 1
            break


