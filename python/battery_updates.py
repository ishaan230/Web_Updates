import psutil
import requests
import time
import json

def send_discord_webhook(webhook_url, message):
    payload = {
        'content': message
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    if response.status_code == 204:
        print("Message sent successfully to Discord!")
    else:
        print("Failed to send message to Discord. Status code:", response.status_code)

# Replace 'YOUR_WEBHOOK_URL' with your actual Discord webhook URL
webhook_url = ''
while True:
# Check if the PC is awake
    if psutil.sensors_battery():
        a = psutil.sensors_battery()
        message = f"Battery : {a[0]}\n Power Plugged : {a[2]}"
        send_discord_webhook(webhook_url, message)
        time.sleep(300)
    else:
        print('Error connecting to PC!')

