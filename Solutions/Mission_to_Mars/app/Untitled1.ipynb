{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd\n",
    "import datetime as dt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def scrape_all():\n",
    "\n",
    "    # Initiate headless driver for deployment\n",
    "    browser = Browser(\"chrome\", executable_path=\"chromedriver\", headless=True)\n",
    "    news_title, news_paragraph = mars_news(browser)\n",
    "\n",
    "    # Run all scraping functions and store in dictionary.\n",
    "    data = {\n",
    "        \"news_title\": news_title,\n",
    "        \"news_paragraph\": news_paragraph,\n",
    "        \"featured_image\": featured_image(browser),\n",
    "        \"hemispheres\": hemispheres(browser),\n",
    "        \"weather\": twitter_weather(browser),\n",
    "        \"facts\": mars_facts(),\n",
    "        \"last_modified\": dt.datetime.now()\n",
    "    }\n",
    "\n",
    "    # Stop webdriver and return data\n",
    "    browser.quit()\n",
    "    return data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def mars_news(browser):\n",
    "    url = \"https://mars.nasa.gov/news/\"\n",
    "    browser.visit(url)\n",
    "\n",
    "    # Get first list item and wait half a second if not immediately present\n",
    "    browser.is_element_present_by_css(\"ul.item_list li.slide\", wait_time=0.5)\n",
    "\n",
    "    html = browser.html\n",
    "    news_soup = BeautifulSoup(html, \"html.parser\")\n",
    "\n",
    "    try:\n",
    "        slide_elem = news_soup.select_one(\"ul.item_list li.slide\")\n",
    "        news_title = slide_elem.find(\"div\", class_=\"content_title\").get_text()\n",
    "        news_p = slide_elem.find(\n",
    "            \"div\", class_=\"article_teaser_body\").get_text()\n",
    "\n",
    "    except AttributeError:\n",
    "        return None, None\n",
    "\n",
    "    return news_title, news_p\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def featured_image(browser):\n",
    "    url = \"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "    browser.visit(url)\n",
    "\n",
    "    # Find and click the full image button\n",
    "    full_image_elem = browser.find_by_id(\"full_image\")\n",
    "    full_image_elem.click()\n",
    "\n",
    "    # Find the more info button and click that\n",
    "    browser.is_element_present_by_text(\"more info\", wait_time=0.5)\n",
    "    more_info_elem = browser.find_link_by_partial_text(\"more info\")\n",
    "    more_info_elem.click()\n",
    "\n",
    "    # Parse the resulting html with soup\n",
    "    html = browser.html\n",
    "    img_soup = BeautifulSoup(html, \"html.parser\")\n",
    "\n",
    "    # Find the relative image url\n",
    "    img = img_soup.select_one(\"figure.lede a img\")\n",
    "\n",
    "    try:\n",
    "        img_url_rel = img.get(\"src\")\n",
    "\n",
    "    except AttributeError:\n",
    "        return None\n",
    "\n",
    "    # Use the base url to create an absolute url\n",
    "    img_url = f\"https://www.jpl.nasa.gov{img_url_rel}\"\n",
    "\n",
    "    return img_url\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def hemispheres(browser):\n",
    "\n",
    "    # A way to break up long strings\n",
    "    url = (\n",
    "        \"https://astrogeology.usgs.gov/search/\"\n",
    "        \"results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "    )\n",
    "\n",
    "    browser.visit(url)\n",
    "\n",
    "    # Click the link, find the sample anchor, return the href\n",
    "    hemisphere_image_urls = []\n",
    "    for i in range(4):\n",
    "\n",
    "        # Find the elements on each loop to avoid a stale element exception\n",
    "        browser.find_by_css(\"a.product-item h3\")[i].click()\n",
    "\n",
    "        hemi_data = scrape_hemisphere(browser.html)\n",
    "\n",
    "        # Append hemisphere object to list\n",
    "        hemisphere_image_urls.append(hemi_data)\n",
    "\n",
    "        # Finally, we navigate backwards\n",
    "        browser.back()\n",
    "\n",
    "    return hemisphere_image_urls\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def twitter_weather(browser):\n",
    "    url = \"https://twitter.com/marswxreport?lang=en\"\n",
    "    browser.visit(url)\n",
    "\n",
    "    html = browser.html\n",
    "    weather_soup = BeautifulSoup(html, \"html.parser\")\n",
    "\n",
    "    # First, find a tweet with the data-name `Mars Weather`\n",
    "    tweet_attrs = {\"class\": \"tweet\", \"data-name\": \"Mars Weather\"}\n",
    "    mars_weather_tweet = weather_soup.find(\"div\", attrs=tweet_attrs)\n",
    "\n",
    "    # Next, search within the tweet for the p tag containing the tweet text\n",
    "    mars_weather = mars_weather_tweet.find(\"p\", \"tweet-text\").get_text()\n",
    "\n",
    "    return mars_weather\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def scrape_hemisphere(html_text):\n",
    "\n",
    "    # Soupify the html text\n",
    "    hemi_soup = BeautifulSoup(html_text, \"html.parser\")\n",
    "\n",
    "    # Try to get href and text except if error.\n",
    "    try:\n",
    "        title_elem = hemi_soup.find(\"h2\", class_=\"title\").get_text()\n",
    "        sample_elem = hemi_soup.find(\"a\", text=\"Sample\").get(\"href\")\n",
    "\n",
    "    except AttributeError:\n",
    "\n",
    "        # Image error returns None for better front-end handling\n",
    "        title_elem = None\n",
    "        sample_elem = None\n",
    "\n",
    "    hemisphere = {\n",
    "        \"title\": title_elem,\n",
    "        \"img_url\": sample_elem\n",
    "    }\n",
    "\n",
    "    return hemisphere\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def mars_facts():\n",
    "    try:\n",
    "        df = pd.read_html(\"http://space-facts.com/mars/\")[0]\n",
    "    except BaseException:\n",
    "        return None\n",
    "    #Since the number of column can be varied hence just renamong the first column by position to create index on it .\n",
    "    #    df.columns = [\"description\", \"value\"]\n",
    "    df.rename(columns={ df.columns[0]: \"description\" }, inplace = True)\n",
    "    df.set_index(\"description\", inplace=True)\n",
    "\n",
    "    # Add some bootstrap styling to <table>\n",
    "    return df.to_html(classes=\"table table-striped\")\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'news_title': \"NASA's Mars 2020 Rover Does Biceps Curls \", 'news_paragraph': \"In this time-lapse video, the robotic arm on NASA's Mars 2020 rover maneuvers its 88-pound (40-kilogram) sensor-laden turret as it moves from a deployed to stowed configuration.\", 'featured_image': 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA19964_hires.jpg', 'hemispheres': [{'title': 'Cerberus Hemisphere Enhanced', 'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'}, {'title': 'Schiaparelli Hemisphere Enhanced', 'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'}, {'title': 'Syrtis Major Hemisphere Enhanced', 'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'}, {'title': 'Valles Marineris Hemisphere Enhanced', 'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}], 'weather': 'InSight sol 233 (2019-07-23) low -98.8ºC (-145.9ºF) high -25.7ºC (-14.2ºF)\\nwinds from the SE at 4.6 m/s (10.2 mph) gusting to 16.2 m/s (36.2 mph)\\npressure at 7.60 hPapic.twitter.com/ksOXPg28yb', 'facts': '<table border=\"1\" class=\"dataframe table table-striped\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>Mars</th>\\n      <th>Earth</th>\\n    </tr>\\n    <tr>\\n      <th>description</th>\\n      <th></th>\\n      <th></th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>Diameter:</th>\\n      <td>6,779 km</td>\\n      <td>12,742 km</td>\\n    </tr>\\n    <tr>\\n      <th>Mass:</th>\\n      <td>6.39 × 10^23 kg</td>\\n      <td>5.97 × 10^24 kg</td>\\n    </tr>\\n    <tr>\\n      <th>Moons:</th>\\n      <td>2</td>\\n      <td>1</td>\\n    </tr>\\n    <tr>\\n      <th>Distance from Sun:</th>\\n      <td>227,943,824 km</td>\\n      <td>149,598,262 km</td>\\n    </tr>\\n    <tr>\\n      <th>Length of Year:</th>\\n      <td>687 Earth days</td>\\n      <td>365.24 days</td>\\n    </tr>\\n    <tr>\\n      <th>Temperature:</th>\\n      <td>-153 to 20 °C</td>\\n      <td>-88 to 58°C</td>\\n    </tr>\\n  </tbody>\\n</table>', 'last_modified': datetime.datetime(2019, 8, 2, 19, 33, 12, 386917)}\n"
     ]
    }
   ],
   "source": [
    "\n",
    "if __name__ == \"__main__\":\n",
    "\n",
    "    # If running as script, print scraped data\n",
    "    print(scrape_all())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
