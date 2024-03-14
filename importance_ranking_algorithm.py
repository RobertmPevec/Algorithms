from functions import importance_ranking_algorithm
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import key
summary_message = importance_ranking_algorithm()
client = Client(key.account_sid, key.auth_token)
message = client.messages.create(
    body=summary_message,
    from_=key.twilio_number,
    to=key.target_number
)
print(message.body)

app = Flask(__name__)


def sms_reply():
    incoming_msg = request.values.get('Body', '').strip()
    resp = MessagingResponse()
