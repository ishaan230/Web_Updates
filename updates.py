import psutil
import requests
import time
import json
import os
from datetime import datetime

time_now = datetime.now()
current_time = time_now.strftime("%H:%M:%S")
def send_discord_webhook_battery(message):
    payload = {
        'content': message
    }

    headers = {
        'Content-Type': 'application/json'
    }

    webhook_url_battery = ''

    response = requests.post(webhook_url_battery, data=json.dumps(payload), headers=headers)

    if response.status_code == 204:
        os.system(f"echo 'Battery update sent successfully to Discord! at {current_time}' >> ./logs/log.txt")
    else:
        os.system(f"echo 'Failed to send Battery update to Discord at {current_time}' >> ./logs/log.txt")

def send_discord_webhook_temp(message):
    payload = {
        'content': message
    }

    headers = {
        'Content-Type': 'application/json'
    }

    webhook_url_temp = ''

    response = requests.post(webhook_url_temp, data=json.dumps(payload), headers=headers)
    if response.status_code == 204:
        os.system(f"echo 'Temp update sent successfully to Discord! at {current_time}' >> ./logs/log.txt")
    else:
        os.system(f"echo 'Failed to send Temp update to Discord at {current_time}' >> ./logs/log.txt")


def send_discord_webhook_cpu(message):
    payload = {
        'content': message
    }

    headers = {
        'Content-Type': 'application/json'
    }

    webhook_url_cpu = ''

    response = requests.post(webhook_url_cpu, data=json.dumps(payload), headers=headers)
    if response.status_code == 204:
        os.system(f"echo 'Cpu update sent successfully to Discord! at {current_time}' >> ./logs/log.txt")
    else:
        os.system(f"echo 'Failed to send CPU update to Discord at {current_time}' >> ./logs/log.txt")

while True:
# Check if the PC is awake
    if psutil.CONN_ESTABLISHED == 'ESTABLISHED':
        
        # For Battery Info
        battery_info = psutil.sensors_battery()
        message = f"Battery : {battery_info[0]}\n Power Plugged : {battery_info[2]}"
        send_discord_webhook_battery(message)
        
        
        # For CPU Info
        cpu_info = psutil.cpu_freq()
        current_cpu = round(cpu_info[0],2)
        min_cpu = round(cpu_info[1]/1000,2)
        max_cpu = round(cpu_info[2]/1000,2)
        message = f"\nCurrent Cpu Usage: {current_cpu}Ghz\nMin Cpu Usage : {min_cpu}Ghz\nMax Cpu Usage : {max_cpu}Ghz"
        send_discord_webhook_cpu(message)


        #For Temp Info 
        a = psutil.sensors_temperatures()
        # print(a)
        # exit()
        cputemp_str = a['k10temp'][0] 
        cpu_current = cputemp_str[1]
        cpu_peak = cputemp_str[2]

        disk_str = a['nvme'][0]
        disk_current = disk_str[1]
        disk_peak = disk_str[2]

        gpu_str = a['amdgpu'][0]
        gpu_current = gpu_str[1]
        gpu_peak = gpu_str[2]
        
        message = f"\nCurrent CPU Temp : {cpu_current}°C\n Highest Temp : {cpu_peak}°C\n\n Current Disk Temp : {disk_current}°C\n Peak Disk : {disk_peak}°C\n\n Current Gpu Temp : {gpu_current}°C\nPeak Gpu Temp : {gpu_peak}°C"
        send_discord_webhook_temp(message)


        #send message
        # message = f"Battery : {battery_info[0]}\n Power Plugged : {battery_info[2]}\n\nCurrent Cpu Usage: {current_cpu}Ghz\nMin Cpu Usage : {min_cpu}Ghz\nMax Cpu Usage : {max_cpu}Ghz\n\nCurrent CPU Temp : {cpu_current}°C\n Highest Temp : {cpu_peak}°C\n\n Current Disk Temp : {disk_current}°C\n Peak Disk : {disk_peak}°C\n\n Current Gpu Temp : {gpu_current}°C\nPeak Gpu Temp : {gpu_peak}°C"
        # send_discord_webhook(webhook_url, message)
        exit()
    else:
        print('Error connecting to PC!')
        exit()