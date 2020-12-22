import requests
import re
from bs4 import BeautifulSoup

# get the lyrics of the song


def scrape_song_info(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    song_info = soup.title.string.replace(u'\xa0', u' ')
    artist = song_info.split(" - ")[0]
    title = song_info.split(" - ")[1].split(" Lyrics")[0]

    lyrics = soup.find('b', text=f'"{title}"'
                       ).find_next('div').text.split("\n")

    lyrics = '\n'.join(lyrics[2:])

    return artist, title, lyrics


# get the top five song and lyrics results
def scrape_top_five(search):
    url = f"https://search.azlyrics.com/search.php?q={search}"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    song_songs = []
    song_artists = []
    song_links = []

    lyrics_songs = []
    lyrics_artists = []
    lyrics_links = []

    song_results = soup.find('b', text="Song results:")
    lyrics_results = soup.find('b', text="Lyrics results:")

    print(song_results)
    print(lyrics_results)

    has_song_results = False
    has_lyrics_results = False

    if song_results:
        has_song_results = True

        songs_table = song_results.find_next('table')
        for item in songs_table.find_all('a')[:5]:
            link = item['href']
            song_links.append(link)

            song = item.find_next('b').text
            song_songs.append(song.replace('"', ""))

            artist = item.find_next('b').find_next('b').text
            song_artists.append(artist)

    if lyrics_results:
        has_lyrics_results = True

        lyrics_table = lyrics_results.find_next('table')

        num_results = int(soup.find(
            'div', {'class': 'panel-heading'}).find('small').text.split('of ')[1].split(' found')[0])

        lyrics_table = lyrics_table.find_all('a')[:5]
        for item in lyrics_table:
            link = item['href']
            lyrics_links.append(link)

            song = item.findChild()
            if song:
                lyrics_songs.append(song.text.replace('"', ""))

            artist = song.find_next('b')
            if artist:
                lyrics_artists.append(artist.text)

    song_results = list(zip(song_songs, song_artists, song_links))
    lyrics_results = list(zip(lyrics_songs, lyrics_artists, lyrics_links))

    if not has_song_results and not has_lyrics_results:
        return "Could not find any results.", {}

    choices = {}
    message = ""
    lyrics_start_index = 1
    if has_song_results:
        message += "Song results:\n"
        lyrics_start_index += len(song_results)

        for i, result in enumerate(song_results, 1):
            message += f"{i}. {result[1]} - {result[0]}\n"
            choices[i] = result[2]

        message += "\n"

    if has_lyrics_results:
        message += "Lyrics results:\n"

        for i, result in enumerate(lyrics_results, lyrics_start_index):
            message += f"{i}. {result[1]} - {result[0]}\n"
            choices[i] = result[2]

        message += "\n"

    message += "Choose a song by typing its number."
    return message, choices


if __name__ == "__main__":
    result = scrape_top_five("jungle")
    print(result)
