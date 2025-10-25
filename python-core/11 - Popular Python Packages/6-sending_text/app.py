from twilio.rest import Client
from config import acc_sid, auth_token


client = Client(acc_sid, auth_token)

msg = client.messages.create(
    from_='+13412373571', # my twilio number
    to='+998880212224',
    # to='+998770122407',
    body='Hey Shakhzod, how is it going?'
)

print('created at:', msg.date_created)
print('sent at:', msg.date_sent)
print('status:', msg.status)
print('direction:', msg.direction)
print('price:', msg.price, msg.price_unit)

# additional features
# client.calls
# client.video
# client.chat
