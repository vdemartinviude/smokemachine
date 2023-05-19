from twilio.rest import Client

def sendmessage(msg):
    account_sid = 'ACd3d30a9828604e06415c782e6d2176ac'
    auth_token = '922b7cc4102ce2d83a001b57ea6e8d29'
    twilio_phone = '+12543823808'

    client = Client(account_sid,auth_token)

    message = client.messages.create(
        body=msg,
        from_= twilio_phone,
        to='+5511949001081'
    )

    print(message.sid)
    print(message.status)

if (__name__=='__main__'):
    sendmessage("Hello Vinicius how are you?")
print(__name__)