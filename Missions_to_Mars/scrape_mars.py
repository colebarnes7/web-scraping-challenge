# Import packages and dependencies
from splinter import Browser
import time
from bs4 import BeautifulSoup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

def scrape():

    # Setup Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL to scrape
    url = "https://redplanetscience.com/"

    # Call visit on our browser and pass in the URL we want to scrape   
    browser.visit(url)

    # Let it sleep for 1 second
    time.sleep(1)

    # Return all the HTML on our page
    html = browser.html
    
    # Create a Beautiful Soup object, pass in our HTML, and call 'html.parser'
    soup = BeautifulSoup(html, "html.parser")

    # Quit the browser
    browser.quit()

    # Stores latest news title and paragraph teaser
    news_title = soup.find("div", class_="content_title").get_text()
    news_p = soup.find("div", class_="article_teaser_body").get_text()

    # Setup Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL to scrape
    url = "https://spaceimages-mars.com/"

    # Call visit on our browser and pass in the URL we want to scrape   
    browser.visit(url)

    # Let it sleep for 1 second
    time.sleep(1)

    # Return all the HTML on our page
    html = browser.html
        
    # Create a Beautiful Soup object, pass in our HTML, and call 'html.parser'
    soup = BeautifulSoup(html, "html.parser")

    # Quit the browser
    browser.quit()

    temp = soup.find_all("img", class_="headerimage fade-in")
    featured_image_url = url + temp[0]['src']
    featured_image_url

    # URL to scrape
    url = "https://galaxyfacts-mars.com/"

    # Scrapes all tabular data off the url
    tables = pd.read_html(url)

    # Pulls just the first table out
    df = tables[0]

    # Sets appropriate header for each column
    df.columns = df.iloc[0] 
    df = df[1:]

    # Sets up the index for the dataframe
    df = df.set_index('Mars - Earth Comparison')

    # Saves table into html file
    df.to_html('table.html')

    # Setup Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL to scrape
    url = "https://marshemispheres.com/"

    # Call visit on our browser and pass in the URL we want to scrape   
    browser.visit(url)

    # Let it sleep for 1 second
    time.sleep(1)

    # Set up lists to put inside the dictionary
    title = []
    img_url = []

    # Return all the HTML on our page
    html = browser.html
        
    # Create a Beautiful Soup object, pass in our HTML, and call 'html.parser'
    soup = BeautifulSoup(html, "html.parser")

    # Stores each instance of the div tag with class description as a item of a list
    queries = soup.find_all('div', class_="description")

    # Loops through each item in the queries list
    for query in queries:
        
        # Finds each title to store and use in the splinter clicker
        temp_title = query.find("h3").get_text()
        new_title = temp_title.replace(" Enhanced", "")
        title.append(new_title)
        
        # Clicks the link using the title we just grabbed
        browser.find_by_css("h3").links.find_by_partial_text(new_title).click()
        
        # Return all the HTML on our page
        html = browser.html
        
        # Create a Beautiful Soup object, pass in our HTML, and call 'html.parser'
        soup = BeautifulSoup(html, "html.parser")
        
        # Stores our image url
        temp_img_url = soup.find_all("img", class_="wide-image")
        new_imp_url = url + temp_img_url[0]['src']
        img_url.append(new_imp_url)
        
        # Goes back to the main page
        browser.back()
        
        # Return all the HTML on our page
        html = browser.html
        
        # Create a Beautiful Soup object, pass in our HTML, and call 'html.parser'
        soup = BeautifulSoup(html, "html.parser")

    # Quit the browser
    browser.quit()

    # Sets up dictionary to hold our data
    hemisphere_image_urls = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_img_url": featured_image_url, 
        "title": [], 
        "img_url": []}

    for item in title:
        hemisphere_image_urls["title"].append(item)

    for item in img_url:
        hemisphere_image_urls["img_url"].append(item)
    
    return hemisphere_image_urls