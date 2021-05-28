#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 27 19:55:48 2021

@author: ichiv
"""
#!/usr/bin/python

import socket
menu = dict()
menu["msg_get_name"] = "Digite seu nome:"
menu["loading"] = "Aguarde.."
menu["input_char"] = "digite uma letra: "
menu["msg_win"] = "é o ganhador!"

address = ("localhost", 8015)

# Create sockets
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(address)
name = ''

# Echo
while True:
    msg = client_socket.recv(4096)
    if msg == menu["msg_get_name"]:
        print(msg)
        nome = input()
        client_socket.send(str.encode(nome))
    elif msg == menu["msg_get_name"]:
        print(msg)
        _char = input()
        client_socket.send(str.encode(_char))
    elif msg == menu["msg_win"]:
        print(msg)
        break
