# lyricSMS

SMS texting app that allows you to find the lyrics to a song just by searching its song name or a sample of some lyrics. Great for when you're in the car and want to get the lyrics to this really good song that's playing so you can sing along!

## How to use it
1. Authenticate your phone number on the Twillio account.
2. Send your query to the Twillio trial phone number.
3. You should receive the top songs by song name and lyrics, or an error message if no results were found.
4. To choose a song, type '?' followed by the number of the song. E.g.: if I wanted the fifth selection, I'd type '?5'.
5. You should get the lyrics to your selected song!

## Technologies Used
* Twillio - allows lyricSMS to send and receive SMS messages to and from users
* BeautifulSoup4 - scrapes the lyrics and top songs based on the user's query, from [AZLyrics](azlyrics.com)
* Flask
* Python

## Future Improvements
* Implement two databases using MongoDB:
  * Storing user's phone numbers and their queries
  * Storing a bunch of songs and their lyrics for faster access
* Experiment with other lyrics APIs that would allow Heroku deployment
