import time
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def scrap_itra_index(
    names: list,
    chromedriver_path: str,
) -> dict:
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service)

    # Ouvrir la page
    url = "https://itra.run/Runners/FindARunner"
    driver.get(url)
    time.sleep(1)

    perf_indexes = {"nom": [], "index": []}
    for name in tqdm(names):

        # Rechercher le nom de l'athlète
        search_bar = driver.find_element(By.ID, "runnername")
        search_bar.clear()
        search_bar.send_keys(name)
        search_bar.send_keys(Keys.RETURN)

        time.sleep(2)

        # Récupérer son index
        perf_indexes["nom"].append(name)
        try:
            perf_indexes["index"].append(int(driver.find_element(By.XPATH, "//*[@id='result-container']/div[1]/div[2]/div/div[3]/span[2]").text))
        except:
            print(f"{name} : No ITRA index found")
            perf_indexes["index"].append(None)

        time.sleep(1)

    driver.quit()

    return perf_indexes