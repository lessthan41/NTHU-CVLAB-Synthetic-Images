import numpy as np
from selenium.webdriver.chrome.service import Service
import time
import urllib
import urllib.request
import os
from selenium.webdriver.common.by import By
import tqdm
from selenium import webdriver
import shutil
import glob
import json

SRC = "/path/to/dir"
DST = "/path/to/output/dir"

def get_images_from_image(scr="./src/",
                        dst="./dst/"):
    import pyautogui
    chromeDriver = 'C:/Users/lessthan41/Desktop/crawler/chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    s =  Service(chromeDriver)
    driver = webdriver.Chrome(service=s, options=options)
    driver.maximize_window()
    
    for dir in os.listdir(scr):
        os.makedirs(os.path.join(dst,dir), exist_ok=True)
        for path in glob.glob(os.path.join(scr,dir)+"/*.*"):
            url = "https://www.google.com.tw/webhp?source=search_app"
            driver.get(url)
            driver.find_element(By.CLASS_NAME,"Gdd5U").click()
            time.sleep(0.5)

            driver.find_element(By.CLASS_NAME,"DV7the").click()
            time.sleep(0.5)
            pyautogui.write(str(os.path.realpath(path))) 
            pyautogui.press('enter')
            time.sleep(5)
            
            pyautogui.scroll(-800)
            time.sleep(1)
            pyautogui.scroll(-800)
            time.sleep(1)
            pyautogui.scroll(-800)
            time.sleep(1)
            pyautogui.scroll(-800)
            time.sleep(1)
            pyautogui.scroll(-800)
            time.sleep(1)
            pyautogui.scroll(-800)
            time.sleep(1)
            pyautogui.scroll(-800)
            time.sleep(1)
            pyautogui.scroll(-800)
            time.sleep(1)
            pyautogui.scroll(-800)
            time.sleep(1)
            pyautogui.scroll(-800)
            time.sleep(1)
            
            url_list = []
            for i in range(1,21):
                try:
                    time.sleep(0.5)
                    # selector="#yDmH0d > div.IEBj9 > c-wiz > div > c-wiz > c-wiz > div > div.jXKZBd > div > div > div > div.IopELe > div > div > div:nth-child(2) > div > div > div:nth-child("+str(i%2+1)+") > div:nth-child("+str(i//2+1)+") > a > div > div.jPzKF.BiYFJe > div > img"
                    selector = "#yDmH0d > div.IEBj9 > c-wiz > div > div:nth-child(2) > c-wiz > div > div.b57KQc > div > div > div > div.IopELe > div > div > div:nth-child(2) > div > div > div:nth-child("+str(i%2+1)+") > div:nth-child("+str(i//2+1)+") > div > a > div > div.jPzKF.lE2DFd.OFiffe > div > img"
                    
                    element = driver.find_element(By.CSS_SELECTOR, selector)
                    img_url = element.get_attribute('src')
                    if img_url != None:
                        ext = img_url.split('/')[-1]
                        # print(ext)
                        filename = str(i).zfill(3) + '.png'
                        
                        _ = {"img_path": "./" + dir + "/" + filename, "url": img_url}
                        url_list.append(_)

                        save_path = os.path.join(os.path.join(dst,dir), filename)
                        urllib.request.urlretrieve(
                            img_url, save_path)
                except:
                    print("/html/body/div[4]/c-wiz/div/c-wiz/c-wiz/div/div[2]/div/div/div/div[1]/div/div[3]/div[2]/div/div/div["+str(i//2)+"]/div["+str(i%2)+"]/a/div/div[1]/div/img")
                    pass
            
            with open(dst + "/" + dir + "/" + "img_url.json", "w+") as fw:
                json.dump(url_list, fw, indent=4)

if __name__ == "__main__":
    get_images_from_image(SRC, DST)
