import requests
import json
import time
import sys
import random
from platform import system
import os
import http.server
import socketserver
import threading

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(
            b"ITZ HACKER FOLLOW ME ON FACEBOOK (www.facebook.com/prembabu001)"
        )

def execute_server():
    PORT = 4000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()

def read_appstate_cookies(file_path):
    with open(file_path, 'r') as file:
        cookies = [line.strip() for line in file.readlines() if line.strip()]
    return cookies

def send_messages():
    # Read appstate cookies
    appstate_cookies = read_appstate_cookies('tokennum.txt')
    num_cookies = len(appstate_cookies)

    requests.packages.urllib3.disable_warnings()

    def cls():
        if system() == 'Linux':
            os.system('clear')
        else:
            if system() == 'Windows':
                os.system('cls')

    cls()

    def liness():
        print('\u001b[37m' + '---------------------------------------------------')

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    # Read all conversation IDs (UIDs)
    with open('convo.txt', 'r') as file:
        convo_ids = [line.strip() for line in file.readlines()]

    # Read messages from file.txt
    with open('file.txt', 'r') as file:
        command_responses = [line.strip() for line in file.readlines()]

    liness()

    # Define commands
    commands = ['bot', 'taklu', 'beta', 'babu']

    while True:
        try:
            for convo_id in convo_ids:
                cookie_index = random.randint(0, num_cookies - 1)  # Randomly select a cookie
                cookie = appstate_cookies[cookie_index]

                # Check for a command from the bot
                command_url = f"https://graph.facebook.com/v15.0/{convo_id}/messages"
                command_response = requests.get(command_url, cookies={"cookie": cookie})  # Use cookie for request
                command_data = command_response.json()

                if 'data' in command_data:
                    for item in command_data['data']:
                        if 'message' in item and 'text' in item['message']:
                            user_message = item['message']['text'].lower()
                            
                            # Check if any command is present in the user message
                            if any(command in user_message for command in commands):
                                # Choose a random response from command_responses
                                response_message = random.choice(command_responses)

                                # Send the response message
                                parameters = {
                                    'message': response_message
                                }
                                response = requests.post(command_url, json=parameters, cookies={"cookie": cookie}, headers=headers)  # Use cookie for sending message

                                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                                if response.ok:
                                    print(f"[+] Sent: {response_message} to {convo_id} using Cookie {cookie_index + 1}")
                                    print(f"  - Time: {current_time}")
                                    liness()
                                else:
                                    print(f"[x] Failed to send message to {convo_id} with Cookie {cookie_index + 1}. Response: {response.text}")
                                    print(f"  - Time: {current_time}")
                                    liness()

                time.sleep(5)  # Adjust the delay as needed

            print("\n[+] All messages processed. Waiting for new messages...\n")
            time.sleep(10)  # Wait before restarting the process

        except Exception as e:
            print("[!] An error occurred: {}".format(e))

def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()
    send_messages()

if __name__ == '__main__':
    main()
