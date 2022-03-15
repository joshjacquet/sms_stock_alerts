from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def init_selenium():

    # Load up chrome options, add a headless option so it doesn't open a window.
    webdriver.Chrome(executable_path='drivers/chromedriver.exe')
    chrome_options = Options()
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--log-level=3')
    #chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # Open a chrome window, load up the website
    driver = webdriver.Chrome(options=chrome_options)
    return(driver)