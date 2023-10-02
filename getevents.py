import requests
from bs4 import BeautifulSoup
from image_down import image_down
from renamer import renamer
from selenium import webdriver
import time


def get_events(area):

    # Create an empty list to store the event data
    event_data = []

    number = 1

    # URL to SOUP
    url = f'https://www.meetup.com/find/?location=us--{renamer(area)}&source=EVENTS&dateRange=this-weekend&eventType=inPerson&distance=fiftyMiles&sortField=DATETIME'

    driver = webdriver.Chrome()
    driver.get(url)

    SCROLL_PAUSE_TIME = 20

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        print("Still Running")
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    soup = BeautifulSoup(driver.page_source, "html.parser")

    # response = requests.get(url)
    # html_content = response.content
    # soup = BeautifulSoup(html_content, 'html.parser')

    # Find all the event listings on the page
    event_listings = soup.find_all('div', class_='p-0 bg-clip-padding bg-cover bg-transparent relative h-full flex bg-white z-0 break-words transition-shadow duration-300 w-full flex-row justify-start py-4 border-t border-gray3 md:pt-4 md:pb-5')

    # Loop through each event listing and extract the event data
    
    for event in event_listings:
            
        print("Still Running")

        # Extract the event title and link
        title = event.find('h2', class_='text-gray7 font-medium text-base pt-0 pb-1 line-clamp-3').text.strip()
        link = event.find('a')['href']

        # Extract place
        place = event.find('p', class_='hidden md:line-clamp-1 text-gray6')

        # Extract date and place
        dates = event.find('time')

        # Extract image
        image = event.find('img')

        if image == None or title == None or link == None or place == None or dates == None:
            continue

        dates = dates.text.strip()

        splitdate = dates.split(" · ")

        if splitdate[0][:3] == "Fri":
            day = "Friday"
        elif splitdate[0][:3] == "Sat":
            day = "Saturday"
        else:
            day = "Sunday"

        eventtime = splitdate[1][0:len(splitdate[1]) - 4]

        place = place.text.strip()
        place = place.split(" • ")
        group = place[0].replace("Group name:", "")
        where = place[1]
        image_url = image['src']
        image_name = image_down(image_url, number, area)
        number += 1

        if not (title == "" or link == "" or day == "" or eventtime == "" or place == "" or image_name == ""):
            event_data.append([title, link, day, eventtime, group, where, image_name])

    return event_data
