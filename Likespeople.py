from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import re
from random import randint
from time import sleep
import traceback
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def opendriver():
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2, "permissions.default.stylesheet": 2,
             "javascript.enabled": False, "profile.default_content_setting_values.notifications": 1}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.maximize_window()
    driver.get('https://www.facebook.com')
    driver.find_element_by_id("email").clear()
    driver.find_element_by_id("email").send_keys('YOUR_EMAIL')
    driver.find_element_by_id("pass").clear()
    driver.find_element_by_id("pass").send_keys('YOUR_PASSWORD')
    driver.find_element_by_id("pass").send_keys(Keys.ENTER)
    return driver

def obtainlike(driver,fileid,postid):
    link = 'https://www.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier='+postid
    driver.get(link)
    seemore = [1]

    #click see more
    while len(seemore)>0:
        driver.implicitly_wait(10)
        #WebDriverWait(driver, 20, 0.5).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'See More')]")))
        seemore = driver.find_elements_by_link_text("See More")
        #seemore = driver.find_elements_by_xpath("//a[contains(text(),'See More')]")

        for i in seemore:
            driver.execute_script("arguments[0].scrollIntoView();", i)
            print(i.text)
            driver.execute_script("arguments[0].click();", i)

        try:
            WebDriverWait(driver, 10, 0.5).until(EC.presence_of_all_elements_located(By.XPATH, "//a[contains(text(),'See More')]"))
        except:
           pass
        #sleep(7)
        seemore = driver.find_elements_by_link_text("See More")
        print('seemore have ',len(seemore))

    #obtain people name and their link
    print('All data has been loaded')
    g = driver.find_elements_by_xpath("//div[@class='_5j0e fsl fwb fcb']/a")
    with open(str(fileid)+'_'+str(postid)+'likes.txt','w') as f:
        for i in g:
            name = i.text
            link = i.get_attribute('href')
            uid = i.get_attribute('data-hovercard')
            uid = int(re.findall(r"\d\d\d\d+", uid)[0])
            #print(name,uid,link)
            f.write(str(name) + '  '+str(uid)+'  '+str(link)+'\n')


file = open("/Users/mia/PycharmProjects/facebook/acsi_postids.txt")

with open('Errorlikes.txt','w') as f:
    for line in file.readlines():
        line = line.strip('\n')
        l = line.split(' : ')
        fileid = l[0]
        postid = l[1].split('_')[1]
        driver = opendriver()

        try:
            obtainlike(driver, fileid, postid)
            driver.quit()
            print(fileid, postid, 'is finished')

        except:
            driver.quit()
            traceback.print_exc()
            f.write(fileid + '  ' + postid + '\n')
            print('-----------------------')
            print('Error!!!Cannot Find the Post', fileid, postid)
            print('-----------------------')
        sleep(randint(2,7))
#
# fileid = '102621172007'
# postid = '10154842459607008'
# driver = opendriver()
# obtainlike(driver, fileid, postid)
#102621172007 : 102621172007_10154842459607008
