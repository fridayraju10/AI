import os
from datetime import datetime
from twilio.rest import Client

# Your Twilio credentials (TEMPORARY for local testing)
account_sid = os.getenv("AC78393198e6d66cdd374d1120e73b45f2")
auth_token = os.getenv("b766a80bb3851516918cc359343b63f7")

client = Client(account_sid, auth_token)

members = [
    "whatsapp:+919498010204",
    "whatsapp:+918838787127",
    "whatsapp:+919488223505"
]

messages = [
    "Im your good friend - Raju",
    "You are Nice person ",
    "Do you remember my previous note about u??",
    "Lets rock together",
    "You will get 5 more msgs in time gap of 1 hr",
    "This is 6th one",
    "Life is precious la??",
    "Shall we roam around the world ",
    "Being happy is called smartness",
    "Am i Smart"
]

current_hour = datetime.now().hour

if 0 <= current_hour <= 11:
    message_index = current_hour % len(messages)
    message_body = messages[message_index]

    for number in members:
        client.messages.create(
            body=message_body,
            from_='whatsapp:+14155238886',
            to=number
        )
        print(f"Message sent to {number}")
else:
    print("Outside scheduled time window.")
