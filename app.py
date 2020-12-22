import os
from scrape import scrape_song_info, scrape_top_five
from scrape import scrape_song_info
from flask import Flask, request
from twilio.rest import Client
from dotenv import load_dotenv
from twilio.twiml.messaging_response import MessagingResponse
load_dotenv()

app = Flask(__name__)

# initialize twilio
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

client = Client(ACCOUNT_SID, AUTH_TOKEN)

choices = {}


@app.route("/", methods=['GET', 'POST'])
def get_lyrics():
    global choices
    from_number = request.args.get('From')
    query = request.args.get('Body')

    resp = MessagingResponse()
    message = "\n\n"

    if query[0] == "?":
        selection = int(query[1])
        url = choices.get(selection, None)
        if not url:
            message += "Invalid selection."
        else:
            song_info = scrape_song_info(choices[selection])
            message += f"{song_info[1]} - {song_info[0]}\n\n"
            message += song_info[2]
    else:
        top_five = scrape_top_five(query)
        choices = top_five[1]
        message += top_five[0]

    print(message)
    print(len(message))
    send_message(message, "+16479458787", from_number)
    # resp.message(message)

    # return str(resp)
    return "success"


def send_message(message, from_=None, to=None):
    if len(message) < 1400:
        client.messages.create(
            body=message,
            from_=from_,
            to=to
        )
    else:
        lines = message.split("\n")
        char_count = 0
        temp_message = ""
        for line in lines:
            if char_count + len(line) >= 1400:
                try:
                    client.messages.create(
                        body=f"\n{temp_message}",
                        from_=from_,
                        to=to
                    )
                except Exception as e:
                    print("SEND FAILED")
                    print(e)
                    print(temp_message)
                    print(len(temp_message))
                char_count = 0
                temp_message = ""

            char_count += len(line) + 1
            temp_message += f"\n{line}"

        if temp_message:
            client.messages.create(
                body=f"\n{temp_message}",
                from_=from_,
                to=to
            )

    return True


if __name__ == '__main__':
    app.run(debug=True)
