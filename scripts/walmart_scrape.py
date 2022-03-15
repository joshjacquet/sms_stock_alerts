import pandas as pd
from time import sleep
from random import randint
from init_selenium import init_selenium
from load_products import load_products

products = load_products()
products = products['site'].to_list()

driver = init_selenium()

def GetWalmart(link):
    driver.get(link)
    sleep(5)
    #html2 = driver.execute_script("return document.documentElement.innerHTML;")
    #print(html2)

for p in products:
    GetWalmart(p)