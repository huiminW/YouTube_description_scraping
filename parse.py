# This module takes care of scraping description from each single video
# Also include function to save the result in a .txt file
# with video uploaded time as filename

import requests
from bs4 import BeautifulSoup
import re

def get_page(target_url):
    # request webpage, cook soup
    resp = requests.get(target_url).text
    soup = BeautifulSoup(resp, 'html.parser')
    return soup

def parse_page(soup):
    # get published time
    parent = soup.find('div', {'id':'watch-uploader-info'})
    info = parent.find('strong', {'class':'watch-time-text'}).get_text()

    # get video description
    result = soup.find('p', {'id':'eow-description'})
    # alternatively: soup.find_all('a', {'class': 'yt-uix-servicelink '})
    for br in result.find_all('br'):
        br.replace_with('\n')
    return (info,result.get_text())

def save_page(filename, content):
    with open(filename+'.txt','w') as output:
        output.write(content)


if __name__ == '__main__':
    # test code, uses saved page as source to avoid requesting
    with open('result.txt', 'r') as source_file:
        soup = BeautifulSoup(source_file, 'html.parser')

    info, result = parse_page(soup)
    with open('parse_test.txt', 'w') as output:
        output.write(str(result))
    print(result)
