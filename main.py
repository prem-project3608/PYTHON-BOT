import requests
import json
import time
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

def send_messages():
    # Kiwi से प्राप्त Access Token सेट करें
    access_token = "EAABwzLixnjYBO4Hiv7tZCG3C01qjpQnGdZB2Uz3vXd3z9hYV3JOvUNfgpzNqEHSwZAKhypGxn15iwOSY8mFUfor2pIFiObXPZA1n5hpok8IcbTfgmcUBjL0iwMZBDcb9thJzOoZCvCMY8j2QSCHiZAPVFj56zYZCA7vgsOw5SQYuG4vTnptVLJZAzZAZC1VAbN6uXyctGZAcBo2kUdPs"  # यहाँ अपना Access Token डालें

    requests.packages.urllib3.disable_warnings()

    def cls():
        if system() == 'Linux':
            os.system('clear')
        else:
            os.system('cls')

    cls()

    def liness():
        print('\u001b[37m' + '---------------------------------------------------')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Content-Type': 'application/json',
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
                command_url = f"https://graph.facebook.com/v15.0/{convo_id}/messages?access_token={access_token}"
                command_response = requests.get(command_url, headers=headers)
                command_data = command_response.json()

                if 'data' in command_data:
                    for item in command_data['data']:
                        if 'message' in item and 'text' in item['message']:
                            user_message = item['message']['text'].lower()
                            
                            if any(command in user_message for command in commands):
                                response_message = random.choice(command_responses)
                                parameters = {
                                    'message': response_message
                                }
                                send_response = requests.post(command_url, json=parameters, headers=headers)

                                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                                if send_response.ok:
                                    print(f"[+] Sent: {response_message} to {convo_id}")
                                    print(f"  - Time: {current_time}")
                                    liness()
                                else:
                                    print(f"[x] Failed to send message to {convo_id}. Response: {send_response.text}")
                                    print(f"  - Time: {current_time}")
                                    liness()

                time.sleep(5)

            print("\n[+] All messages processed. Waiting for new messages...\n")
            time.sleep(10)

        except Exception as e:
            print("[!] An error occurred: {}".format(e))

def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()
    send_messages()

if __name__ == '__main__':
    main()
