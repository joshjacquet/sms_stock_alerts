import pandas as pd
from time import sleep
from random import randint
from scripts.init_selenium import init_selenium
from scripts.load_products import load_products

products = load_products()
driver = init_selenium()

def GetWalmart(link):
    driver.get(link)
    html2 = driver.execute_script("return document.documentElement.innerHTML;")
    print(html2)

for p in products[1]:
    print(p)

