import os
from flask import Flask
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# initialize twilio
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

client = Client(ACCOUNT_SID, AUTH_TOKEN)


@app.route("/")
def get_lyrics():
    # message = client.messages.create(
    #     body="Hello there",
    #     from_='+16479458787',
    #     to='+16479838785'
    # )
    return "hello, world"


if __name__ == '__main__':
    app.run(debug=True)
