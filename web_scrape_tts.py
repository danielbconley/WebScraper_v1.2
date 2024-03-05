from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pyttsx3 
import time
import os

def generate_tts(text, output_file):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_file)
    engine.runAndWait()  # Wait for the speaking to finish
    print(f'Audio content written to file "{output_file}"')

images_path = r"YOUR IMAGE FOLDER PATH GOES HERE"
audio_path = r"YOUR AUDIO FOLDER PATH GOES HERE"

# ensure directories exist
for path in [images_path, audio_path]:
    if not os.path.exists(path):
        os.makedirs(path)

chrome_driver_path = r'YOUR CHROME DRIVER PATH GOES HERE' # see .README for more information. make sure to include the .exe file name at the end of the directory path (ex: \chromedriver.exe)
chrome_browser_path = r'YOUR CHROME APPLICATION PATH GOES HERE' # see .README for more information. make sure to include the .exe file name at the end of the directory path (ex: \chrome.exe)

s = Service(chrome_driver_path)
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_browser_path
driver = webdriver.Chrome(service=s, options=chrome_options)

driver.get("YOUR WEBSITE URL GOES HERE")
time.sleep(5)

# function to adjust properties
def adjust_css_for_screenshot(element, property_name, value):
    driver.execute_script(f"arguments[0].style.{property_name} = '{value}';", element)

title = driver.find_element(By.XPATH, "TITLE XPATH GOES HERE") # see .README for more information. This should look something like "/html/body/div[1]/div/div/div/div/div/div/article/div/div[2]/div/div[2]/h1/strong"
# enlarge title CSS before screenshot
adjust_css_for_screenshot(title, "fontSize", "2em")  # increase title font size for better screenshot

title_text = title.text
print("Successfully acquired title text\n")
print(title_text + "\n")
title.screenshot(os.path.join(images_path, "title.png"))
print("Successfully acquired title screenshot\n")

# convert title to TTS
title_audio_filename = os.path.join(audio_path, "title.mp3")
generate_tts(title_text, title_audio_filename)

paragraph_texts = []
number = 1

while True:
    try:
        paragraph = driver.find_element(By.XPATH, f"TITLE XPATH GOES HERE[{number}]") # see .README for more information this should look something like "/html/body/div[1]/div/div/div/div/div/div/article/div/div[2]/div/div[{number}]"
        # enlarge paragraph text before screenshot
        adjust_css_for_screenshot(paragraph, "fontSize", "30px")  # increase paragraph font size
        paragraph_text = paragraph.text
        if paragraph_text:
            paragraph_texts.append(paragraph_text)
            print(f"Successfully acquired text for paragraph {number}\n")
            print(paragraph_text + "\n")
            paragraph.screenshot(os.path.join(images_path, f"paragraph{number}.png"))
            print(f"Successfully acquired screenshot for paragraph {number}\n")
            time.sleep(0.5)
            number += 1
        else:
            print(f"No text found for paragraph {number}\n")
    except Exception as e:
        print(f"Finished acquiring paragraphs or encountered an error: {e}")
        break

driver.quit()

for i, paragraph_text in enumerate(paragraph_texts, start=1):
    audio_filename = os.path.join(audio_path, f"paragraph{i}.mp3")
    generate_tts(paragraph_text, audio_filename)

print("Web scraping and TTS generation completed.")
