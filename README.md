**DISCLAIMER**: I AM NOT RESPONSIBLE FOR WHAT YOU DO WITH THIS SCRIPT. THIS SCRIPT IS SIMPLY PROOF OF CONCEPT, AND SHOULD NOT BE USED TO CLAIM OR SELL COPYRIGHTED MATERIAL. BY USING THIS SCRIPT, YOU AGREE THAT YOU ARE RESPONSIBLE FOR HOW IT IS USED.

Description: This program captures screenshots of various website elements to create short 1 minute videos for use on social media.

Before we start: I have provided sample folders to use, although this is completely optional. I recommend using these for simplicity sake, as your folders need to be consistent between the scripts.

**Instructions to set up the scripts:**

1. Install Python: Download and install Python from https://www.python.org/

2. Install Dependencies:
   - For generate_video.py and split_video.py: 
     Run pip install moviepy in the terminal or command prompt.
   - For web_scrape_tts.py: 
     Run pip install selenium pyttsx3 in the terminal or command prompt.

3. Download WebDriver: For web_scrape_tts.py, download the WebDriver for your browser. For Chrome, download ChromeDriver from https://sites.google.com/chromium.org/driver/. I recommend storing this in the "chromewebdriver" folder I've included.

4. Download ImageMagick: For split_video.py, download and install ImageMagick and make sure to choose the option "Install legacy utilities (e.g. convert)". ImageMagick can be found at: https://imagemagick.org/

5. Download FFMPEG: moviepy uses FFMPEG to function properly. FFMPEG can be installed from https://ffmpeg.org/download.html



**Setting Up generate_video.py**

- Line 5, 6, 7: Replace YOUR IMAGE FOLDER PATH GOES HERE, YOUR AUDIO FOLDER PATH GOES HERE, and YOUR BACKGROUND VIDEO FOLDER PATH GOES HERE with your actual folder paths. *NOTE: You must put a background video in the background videos folder, and it must be long enough for all the content. 30-45 minutes is a safe bet, although this can vary based on how much content you're converting to TTS.
- Line 49: Replace YOUR OUTPUT FOLDER GOES HERE with the path where you want the final video to be saved.



**Setting Up web_scrape_tts.py**

- Line 14, 15: Replace YOUR IMAGE FOLDER PATH GOES HERE and YOUR AUDIO FOLDER PATH GOES HERE with your actual folder paths.
- Line 22, 23: Replace YOUR CHROME DRIVER PATH GOES HERE with the path to your downloaded WebDriver file. Replace YOUR CHROME APPLICATION PATH GOES HERE if necessary.
- Line 30: Replace YOUR WEBSITE URL GOES HERE with the URL of the website you want to scrape.
- Lines 37 and 56: Replace TITLE XPATH GOES HERE and PARAGRAPH XPATH GOES HERE with the actual XPaths for the elements you want to scrape and convert to text and images. XPATH can be found by downloading a generic "XPATH finder" extension on chrome. Line 56 is responsible for capturing the screenshots of the paragraphs. Make sure your selected site uses a consistent XPATH format so that the accumulator variable works properly. The reason this works is because for every screenshot grabbed it increases the count by 1. Below I've included how it should be modeled

Example:

"/html/body/div[1]/div/div/div/div/div/div/article/div/div[2]/div/p[1]"

"/html/body/div[1]/div/div/div/div/div/div/article/div/div[2]/div/p[2]"

"/html/body/div[1]/div/div/div/div/div/div/article/div/div[2]/div/p[3]"
                                                                    
So our variable in line 56 should look like:   

paragraph = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div/div/div/div/article/div/div[2]/div/p[{number}]") 



**Setting Up split_video.py**

- Line 5: Replace YOUR VIDEO FOLDER PATH GOES HERE with the path to your video file.
- Line 6: Replace YOUR OUTPUT FOLDER PATH GOES HERE with the path where the split video segments should be saved.
- Line 29: Replace YOUR CHANNEL NAME GOES HERE with your YouTube channel name or any text you want to add to the video.



**Running the Scripts**

After setting up, navigate to the folder containing your script in a terminal or command prompt and run the main.py script.


I've included a sample video on my YouTube. You can access it by clicking [here](https://youtube.com/shorts/ZNIUgRpytX0?feature=share)
