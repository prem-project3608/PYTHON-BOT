import requests
import json
import time
import sys
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
            b"ITZ HACKER FOLLOW ME ON FACEBOOK (www.facebook.com/prembabu001)")

def execute_server():
    PORT = 4000

    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()

def send_messages():
    with open('tokennum.txt', 'r') as file:
        tokens = file.readlines()
    num_tokens = len(tokens)

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

    liness()

    access_tokens = [token.strip() for token in tokens]

    # Read all conversation IDs (UIDs) and corresponding hater names
    with open('convo.txt', 'r') as file:
        convo_data = [line.strip().split(' ', 1) for line in file.readlines()]

    convo_ids = [data[0] for data in convo_data]
    haters_names = [data[1] for data in convo_data]  

    with open('file.txt', 'r') as file:
        messages = file.readlines()

    num_messages = len(messages)

    liness()

    response_count = {}  # Store response counts for each convo_id

    while True:
        try:
            for message_index in range(num_messages):
                convo_index = message_index % len(convo_ids)
                convo_id = convo_ids[convo_index]
                haters_name = haters_names[convo_index]

                token_index = message_index % num_tokens
                access_token = access_tokens[token_index]

                message = messages[message_index].strip()

                # Initialize response count for the convo_id if not present
                if convo_id not in response_count:
                    response_count[convo_id] = 0

                # Check for specific commands and set reply based on count
                if "hello" in message.lower():
                    reply = "Hello! How can I assist you today?" if response_count[convo_id] == 0 else "I'm here to help!"
                elif "bot" in message.lower():
                    reply = "What do you want, human?" if response_count[convo_id] == 0 else "Still here, what do you need?"
                else:
                    continue  # Skip any messages that are not commands

                # Increment response count
                response_count[convo_id] += 1

                url = "https://graph.facebook.com/v15.0/{}/".format('t_' + convo_id)
                parameters = {
                    'access_token': access_token,
                    'message': reply
                }
                response = requests.post(url, json=parameters, headers=headers)

                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print("[+] Message sent to Convo {} by Token {}: {}".format(convo_id, token_index + 1, reply))
                    print("  - Time: {}".format(current_time))
                    liness()
                else:
                    print("[x] Failed to send message to Convo {} with Token {}: {}".format(convo_id, token_index + 1, reply))
                    print("  - Time: {}".format(current_time))
                    liness()

                time.sleep(1)  # Add a small delay between requests

            print("\n[+] All messages sent. Restarting the process...\n")
        except Exception as e:
            print("[!] An error occurred: {}".format(e))

def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()

    send_messages()

if __name__ == '__main__':
    main()
