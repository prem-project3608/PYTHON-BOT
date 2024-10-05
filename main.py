import requests
import time
import sys
import threading
from platform import system
import os
import http.server
import socketserver

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"ITZ HACKER FOLLOW ME ON FACEBOOK (www.facebook.com/prembabu001)")

def execute_server():
    PORT = 4000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()

def send_messages():
    with open('tokennum.txt', 'r') as file:
        access_tokens = [token.strip() for token in file.readlines()]

    with open('convo.txt', 'r') as file:
        convo_id = file.read().strip()

    with open('file.txt', 'r') as file:
        messages = file.readlines()

    with open('time.txt', 'r') as file:
        speed = int(file.read().strip())

    current_message_index = 0

    while True:
        command = "bot"  # Set command directly to 'bot'

        if command == "bot":
            if current_message_index < len(messages):
                message = messages[current_message_index].strip()
                access_token = access_tokens[0]  # Only use the first token

                url = "https://graph.facebook.com/v15.0/{}/".format('t_' + convo_id)
                parameters = {
                    'access_token': access_token,
                    'message': message
                }
                response = requests.post(url, json=parameters)

                if response.ok:
                    print("[+] Message sent: {}".format(message))
                else:
                    print("[x] Failed to send message: {}".format(message))

                time.sleep(speed)

                # Move to the next message after sending
                current_message_index += 1
            else:
                print("No more messages to send.")
                break  # Stop if no more messages
        else:
            print("Unknown command! Please use 'bot'.")

def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()
    send_messages()

if __name__ == '__main__':
    main()
