#!/usr/bin/env python

import http.client

# get http server ip
http_server = "127.0.0.1"
# create a connection
conn = http.client.HTTPConnection(http_server)

while 1:
    cmd = input('input command (ex. GET index.html): ')
    cmd = cmd.split()

    # params = urllib.parse.urlencode({'name': 'UFMG'})
    headers = {"Content-type": "application/json", "Accept": "text/plain"}

    # request command to server
    if cmd[0] == 'exit':  # tipe exit to end it
        break
    elif cmd[0] == "GET":
        #conn.request("GET", "rsc.txt")
        conn.request(cmd[0], cmd[1])
    elif cmd[0] == "POST":
        #conn.request("POST", "rsc.txt", 'UFMG', headers)
        conn.request(cmd[0], cmd[1], cmd[2], headers)
    elif cmd[0] == "PUT":
        #conn.request("PUT", "rsc.txt", 'UFPE')
        conn.request(cmd[0], cmd[1], cmd[2])
    elif cmd[0] == "DELETE":
        #conn.request("DELETE", "rsc.txt", 'UFMG', headers)
        conn.request(cmd[0], cmd[1], cmd[2], headers)

    # get response from server
    rsp = conn.getresponse()

    # print server response and data
    print(rsp.status, rsp.reason)
    data_received = str(rsp.read()).replace("b'", "")
    print(data_received)

conn.close()