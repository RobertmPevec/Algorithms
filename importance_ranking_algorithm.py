from functions import importance_ranking_algorithm
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import key
tasks = [
    {"name": "MA122 homework", "due_date": "n/a", "weight": 8},
    {"name": "EN107 essay", "due_date": "2024-03-14", "weight": 8},
    {"name": "MA102 webwork", "due_date": "2024-03-25", "weight": 9},
    {"name": "OL140 guided reflection", "due_date": "2024-03-10", "weight": 9}
]
summary_message = importance_ranking_algorithm(tasks)
client = Client(key.account_sid, key.auth_token)
message = client.messages.create(
    body=summary_message,
    from_=key.twilio_number,
    to=key.target_number
)
print(message.body)

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("The Robots are coming! Head for the hills!")
    return str(resp)


print(sms_reply)

if __name__ == "__main__":
    app.run(debug=False)
