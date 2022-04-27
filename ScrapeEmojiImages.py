from urllib.request import urlopen
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from PIL import Image

start = 0
driver = webdriver.Edge()
driver.get('https://emojipedia.org/google/')
ul = driver.find_element(By.CLASS_NAME, "emoji-grid")
listitems = ul.find_elements(By.TAG_NAME, "li")

for index, li in enumerate(listitems[:]):  # Control number of loops in listitems[:number of times to loop]
    image = li.find_element(By.TAG_NAME, "img")
    driver.execute_script("arguments[0].scrollIntoView()", li)
    try:
        # Get the src attribute
        getfile = image.get_attribute('src')
        # Set Focus on Second Tab and continue
        img = Image.open(urlopen(getfile))
        img.save(f".\\Emojis\\emoji_{index}.png")
        print("Saved Emoji", index)
        # driver.close()
        # driver.switch_to.window(driver.window_handles[0])  # Switch back to tab 0

    except exceptions.StaleElementReferenceException:
        pass
driver.quit()
