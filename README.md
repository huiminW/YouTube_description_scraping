# YouTube_description_scraping
A toy project that scrapes descriptions of videos on YouTube

Many Beauty YouTubers leave name and links to beauty items in the description box below their videos.
This project tries to scrape for these information and possibly do something to them.

parse.py
This module takes care of scraping description from each single video
Also include function to save the result in a .txt file
with video uploaded time as filename

fetch_links.py
This module takes the url of a YouTuber's "videos" section in their home page
Loads all videos automatically (equivalent to keep clicking "load more")
Collect links to each video(all the videos uploaded by that YouTuber)
Call parse_page() from parse.py to get description for each page
Call save_page() from parse.pu to save scraped descriptions

For now, "videos" link is hard coded in to fetch_links.py(the page that shows all videos one YouTuber has uploaded)
To change target YouTuber, simply go to their YouTube "videos" page and copy the url on to fetch_links.py

ToDo:
1. If someone uploaded 2 videos in the same day, one of it will be overwriten.(There must be a better way to name files)
2. I would eventually try parsing these information better and store them in a database such as SQLite.
3. I might eventually try to parse these beauty item links as well.

This is it for now.
