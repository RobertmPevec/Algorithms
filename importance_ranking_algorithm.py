from functions import importance_ranking_algorithm
from twilio.rest import Client
import key
importance_ranking_algorithm()
client = Client(key.account_sid, key.auth_token)
message = client.messages.create(
    body="This is a test message",
    from_=key.twilio_number,
    to=key.target_number
)
print(message.body)
