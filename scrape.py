import pyperclip
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By

start = 0
driver = webdriver.Edge()
driver.get('https://emojipedia.org/google/')
ul = driver.find_element(By.CLASS_NAME, "emoji-grid")
listitems = ul.find_elements(By.TAG_NAME, "li")

with open('emoji.txt', 'w', encoding="utf-8") as EmojiText:
    for li in listitems:  # Control number of loops in [:NUM]
        for a in li.find_elements(By.TAG_NAME, "a"):
            try:
                # Scroll Onto View Once Loaded to prevent exception raise
                driver.execute_script("arguments[0].scrollIntoView()", a)
                mainLink = a.get_attribute("href")
                driver.execute_script("window.open('" + mainLink + "','_blank');")
                # Set Focus on Second Tab and continue
                driver.switch_to.window(driver.window_handles[1])
                # Press Copy Button Here
                button = driver.find_element(By.CLASS_NAME, "btn-clipboard")
                driver.execute_script("arguments[0].scrollIntoView()", button)
                button.click()
                # Pyclip to copy contents from clipboard
                EmojiText.write(pyperclip.paste() + '\n')
                # Close that current Tab
                driver.close()
                driver.switch_to.window(driver.window_handles[0])  # Switch back to tab 0

            except exceptions.StaleElementReferenceException:
                pass
driver.quit()
