from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class infow:
    def __init__(self):
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)

    def get_info(self, query):
        
        try:
            self.driver.get("https://www.wikipedia.org/")
            search = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="searchInput"]'))
            )
            search.click()
            search.send_keys(query)
            enter = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
            enter.click()
        except Exception as e:
            print(f"An error occurred while searching Wikipedia: {e}")

    def get_data(self, query):
        
        try:
            self.driver.get("https://chatgpt.com/")
            search = self.driver.find_element(By.XPATH, '//*[@id="composer-background"]/div[1]')
            search.click()
            search.send_keys(query)
            enter = self.driver.find_element(By.XPATH, '//*[@id="main"]/article/div[1]/div/div[1]/div/form/div')
            enter.click()
        except Exception as e:
            print(f"An error occurred while querying OpenAI: {e}")

    def play_video(self, query):
        
        try:
            self.driver.get("https://www.youtube.com/results?search_query=" + query)
            # Wait for the video elements to load
            enter = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="dismissible"]'))
            )
            enter.click()
        except Exception as e:
            print(f"An error occurred while playing video: {e}")

    def close_driver(self):
       
        self.driver.quit()
