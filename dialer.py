from flask import Flask, request, Response
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
import time

# Twilio Credentials (Replace with your own)
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_number'

app = Flask(__name__)
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Route to handle call instructions
@app.route('/voice', methods=['POST'])
def voice():
    response = VoiceResponse()
    response.say("Hello, this is an automated call from your Twilio dialer.", voice='alice')
    return Response(str(response), mimetype='text/xml')

# Function to make an outbound call
def make_call(to_phone_number):
    call = client.calls.create(
        to=to_phone_number,
        from_=TWILIO_PHONE_NUMBER,
        url="http://your-server-address/voice"  # Replace with your public server URL
    )
    print(f"Call initiated: {call.sid}")

if __name__ == "__main__":
for i in range (1,12000)
    time.sleep(60)
    app.run(host='0.0.0.0', port=5000, debug=True)
    time.sleep(81)
    app.run(host='0.0.0.0', port=5000, debug=True)
    time.sleep(111)
    app.run(host='0.0.0.0', port=5000, debug=True)
