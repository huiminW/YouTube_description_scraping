# This module takes the url of a YouTuber's "videos" section in their home page
# Loads all videos automatically (equivalent to keep clicking "load more")
# Collect links to each video(all the videos uploaded by that YouTuber)
# Call parse_page() from parse.py to get description for each page
# Call save_page() from parse.pu to save scraped descriptions

import requests
from bs4 import BeautifulSoup
import re
import json
import parse

def load_more(source_string):
    # load more from database using link found on webpage
    # use get() on the link returns an json tile
    try:
        ajax_href = re.search('data\-uix\-load\-more\-href\=\".*?\"', source_string)
        cont_href = 'https://www.youtube.com/' + ajax_href.group()[25:-1]
        cont_resp = requests.get(cont_href).text
        cont_data = json.loads(cont_resp)
        return cont_data
    except:
        return None


# set target url(a certain YouTuber's "videos" section in their home page)
target_url = 'https://www.youtube.com/channel/UClVJCkItoSHxRLmVVzmjoEA/videos'

# put content from "videos" page along with results from "load more" in a list(soups_to_parse)
orig_soup = parse.get_page(target_url)
soups_to_parse = [orig_soup]
load_button = orig_soup.find('button', {'aria-label':"Load more\n"})

# load more amd append it to soups_to_parse list
while(load_button!=None):
    cont_data = load_more(str(load_button))
    if cont_data==None:
        break
    cont_soup = BeautifulSoup(cont_data.get('content_html'),'html.parser')
    soups_to_parse.append(cont_soup)
    load_button = cont_data.get('load_more_widget_html')


# Extract links from soups_to_parse and put it in a dictionary
# With link_title as key and link_href as value
link_dict={}
for soup in soups_to_parse:
    for link in soup.find_all('a', {'class':'yt-uix-sessionlink yt-uix-tile-link spf-link yt-ui-ellipsis '+
                                            'yt-ui-ellipsis-2'}):
        link_title = link.get_text()
        link_href_raw = re.search('href\=.+?\\"',str(link)).group()
        link_href = 'https://www.youtube.com/'+link_href_raw[6:-1]
        # print(link_href)
        link_dict[link_title] = link_href

# print(link_dict)
# print(len(link_dict))

# Extract description from each link and save them to files
for link_title in link_dict.keys():
    soup = parse.get_page(link_dict[link_title])
    info, result = parse.parse_page(soup)
    parse.save_page(info, link_title+'\n'+result)

