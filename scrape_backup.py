import requests
import re
from bs4 import BeautifulSoup

# get the data


def scrape_song_info(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    song_info = soup.title.string.replace(u'\xa0', u' ')

    artist = song_info.split(" – ")[0]
    title = song_info.split(" – ")[1].split(" Lyrics")[0]
    div = soup.find('div', {'class': 'lyrics'})
    for p in div.find_all('p'):
        lyrics_raw = p.text
        no_ws = lyrics_raw.replace(u'\xa0', u' ')
        no_ws = no_ws.replace(u'\u2005', u' ')
        no_ws = no_ws.replace(u'\u205f', u' ')
        no_ws = no_ws.split("\n")

    return title, artist, no_ws


def scrape_top_five(search):
    url = f"https://genius.com/search?q={search}"
    options = se.webdriver.ChromeOptions()
    options.add_argument('headless')
    # page = requests.get(url)
    # soup = BeautifulSoup(page.text, 'html.parser')

    songs = []
    artists = []
    links = []
    # for result in soup.find('div', {'class': 'mini_card-title'}):
    #     songs.append(result.text)

    # for result in soup.find('div', {'class': 'mini_card-subtitle'}):
    #     artists.append(result.text)

    # for result in soup.find('a', {'class': 'mini_card'}):
    #     links.append(result.get('href'))

    return a


if __name__ == "__main__":
    print(scrape_top_five("changes"))
    # page = requests.get("https://genius.com/search?q=changes")
    # soup = BeautifulSoup(page.content, "html.parser")
    # print(soup.prettify())
