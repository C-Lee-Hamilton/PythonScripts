import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import time

# Replace 'youtube2.com' with the actual URL of the YouTube test version
initial_url = 'https://www.youtube.com/watch?v=ptCgAfANIdc&list=PLqCPt7683g8ArcGMZsTFYwUoFUHrrVDxK&ab_channel=VirgilCole'
profile_url = 'https://www.youtube.com/@PirateSoftware/streams'

# Set the delay before navigating to the streams page (in seconds)
delay_before_streams = 18000  # 1 minute

# Get the current script directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Set the relative path to the chromedriver executable in the subfolder
driver_path = os.path.join(script_directory, "drivers", "chromedriver.exe")

# Configure the Selenium WebDriver with the chromedriver executable path
chrome_service = ChromeService(executable_path=driver_path)
driver = webdriver.Chrome(service=chrome_service)

# Open the initial YouTube URL
driver.get(initial_url)

# Wait for the page to load
wait = WebDriverWait(driver, 10)

# Add a delay before navigating to the streams page (1 minute)
print(f"Waiting for {delay_before_streams} seconds before navigating to the streams page...")
time.sleep(delay_before_streams)

# Navigate to the profile streams page
driver.get(profile_url)

# Wait for the page to load
wait.until(EC.presence_of_element_located((By.ID, 'channel-header')))

# Find the first video in the streams page and click on it
first_video_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ytd-rich-grid-renderer #video-title')))
first_video_link.click()

# Wait for the video content to load (you may need to adjust this wait condition)
wait.until(EC.presence_of_element_located((By.ID, 'movie_player')))

# Get the current video title
current_video_title_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.style-scope.ytd-watch-metadata yt-formatted-string')))
current_video_title = current_video_title_element.text

# Print the current video title
print(f"Currently watching: {current_video_title}")

# Keep the browser window open for manual interaction
# driver.quit()  # Comment out or remove this line

# Allow the user to manually close the browser
input("Press Enter to close the browser...")