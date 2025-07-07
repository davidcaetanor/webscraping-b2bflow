from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.monteleste.com.br/camisetas-lisas')
sleep(5)

product_names = driver.find_elements(By.XPATH,"//h3[@class='product-name h-auto text-color-black mt-space-12 block overflow-hidden text-[1em] leading-[1.25em] max-h-[2.5em]']")
product_prices = driver.find_elements(By.XPATH,"//span[@class='text-[1.25em] font-semibold max-sm:text-[1em]']")

for product_names, product_prices in zip(product_names,product_prices):
    with open('webscraping-b2bflow.txt','a+',encoding='utf-8') as file:
        file.write(f'{product_names.text}, {product_prices.text}\n')

input('')