import platform
import socket
import psutil
import requests
import time
from getpass import getuser
from datetime import datetime
import json
import pygetwindow as gw

# URL endpoints
API = "https://tegmon.pythonanywhere.com"

REGISTER_URL = f"{API}/api/device/register/"
ACTIVITY_URL = f"{API}/api/activity/"

def get_system_info():
    system_name = platform.node()
    username = getuser()
    os_version = platform.version()
    ip_address = socket.gethostbyname(socket.gethostname())

    return {
        "system_name": system_name,
        "username": username,
        "last_login": datetime.now().isoformat(),
        "ip_address": ip_address,
        "os_version": os_version
    }

def register_device():
    headers = {"Content-Type": "application/json"}
    system_info = get_system_info()

    try:
        response = requests.post(REGISTER_URL, json=system_info, headers=headers)

        if response.status_code == 201:
            print("Device registered successfully!")
        elif response.status_code == 200:
            print("Device already registered. Last login updated.")
        else:
            print("Failed to register device:", response.json().get("message"))

    except Exception as e:
        print("Error connecting to the server:", e)

def send_activity_data(activity_data):
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(ACTIVITY_URL, json=activity_data, headers=headers)
        if response.status_code == 201:
            pass
        else:
            print(f"Failed to send activity data: {response.status_code}")
    except Exception as e:
        print(f"Error sending data: {e}")

def monitor_activity():
    system_info = get_system_info()

    app_names = ["code.exe", "notepad.exe", "chrome.exe"]
    app_state = {}

    for app in app_names:
        app_state[app] = {'process_found': False, 'minimized': False}

    while True:
        for app in app_names:
            process_found = False

            for process in psutil.process_iter(['pid', 'name']):
                if process.info['name'].lower() == app.lower():
                    process_found = True
                    if not app_state[app]['process_found']:
                        log_message = f"{app} opened!"
                        send_activity_data(create_activity_payload(system_info, log_message, "green"))
                        app_state[app]['process_found'] = True
                    break

            if not process_found and app_state[app]['process_found']:
                log_message = f"{app} closed!"
                send_activity_data(create_activity_payload(system_info, log_message, "red"))
                app_state[app]['process_found'] = False
                app_state[app]['minimized'] = False

            if process_found:
                windows = gw.getWindowsWithTitle(app.replace(".exe", "").capitalize())
                if windows:
                    window = windows[0]
                    if window.isMinimized != app_state[app]['minimized']:
                        if window.isMinimized:
                            log_message = f"{app} minimized!"
                            send_activity_data(create_activity_payload(system_info, log_message, "yellow"))
                        else:
                            log_message = f"{app} restored!"
                            send_activity_data(create_activity_payload(system_info, log_message, "blue"))
                        app_state[app]['minimized'] = window.isMinimized

        time.sleep(1)

def create_activity_payload(system_info, activity_log, color):
    return {
        "device": {
            "system_name": system_info["system_name"],
            "username": system_info["username"],
            "ip_address": system_info["ip_address"],
            "os_version": system_info["os_version"]
        },
        "activity_log": activity_log,
        "color": color,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

if __name__ == "__main__":
    register_device()
    monitor_activity()