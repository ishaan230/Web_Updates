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
    if psutil.cpu_freq():
        a = psutil.cpu_freq()
        print(a)
        current_cpu = round(a[0],2)
        min_cpu = round(a[1]/1000,2)
        max_cpu = round(a[2]/1000,2)
        message = f"\nCurrent Cpu Usage: {current_cpu}Ghz\nMin Cpu Usage : {min_cpu}Ghz\nMax Cpu Usage : {max_cpu}Ghz"
        send_discord_webhook(webhook_url, message)
        time.sleep(300)
    else:
        print('Error connecting to PC!')

