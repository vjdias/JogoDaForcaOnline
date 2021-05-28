#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 27 19:53:53 2021

@author: ichiv
"""

import socket
import threading

class Player:
    def __init__(self, id, name, client, address, score):
        self._id = id
        self._name = name
        self._client = client
        self._address = address
        self._score = score
        self._players = dict()

    def add(self, id, player):
        self._players[id] = player

    def get(self, id):
        return self._players[id]

    def get_all(self):
        return self._players

    def set(self, id, value):
        self._players[id] = value


class Hangman:
    def __init__(self, server_name, port):
        self._server_name = server_name
        self._address = (server_name, port)
        self._players = Player("", "", "", "", 0)
        self._menu = dict()
        self._menu["msg_get_name"] = "Digite seu nome:"
        self._menu["loading"] = "Aguarde.."
        self._menu["input_char"] = "digite uma letra: "
        self._menu["msg_win"] = "é o ganhador!"
        self._word = 'paralelogramo'
        self._secret_word = '_'*len(self._word)

    def verify_word(self, input_char):
        s = list(self._secret_word)
        count = 0
        count_hits = 0
        # for every character in secret_word
        for _char in self._word:
        # see if the character is in the players guess
            if _char == input_char:
                s[count] = _char
                self._secret_word = ''.join(s)
                count_hits += 1
            count += 1

        return count_hits


    def send_wlc_message(client_connection, y):
        client_connection.send("Seja bem vindo!")


    def accept_clients(self, the_server, y):
        count = 0
        while True:
            if len(self._players.get_all()) < 3:
                client, addr = the_server.accept()
                client.send(str.encoder(self._menu["msg_get_name"]))
                client_name = client.recv(4096)
                self._players.add(count, Player(client_name, client, addr, 0))
                count += 1
                threading._start_new_thread(self.send_wlc_message, (client, addr))


    def connect(self):
        # Create sockets
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect sockets
        server_socket.bind(self._address)
        server_socket.listen(1)

        threading._start_new_thread(self.accept_clients, (server_socket, " "))


    def start(self):
        self.connect()
        count = 0
        while True:

            while True:
                if len(self._players.get_all()) == 2:
                    break

            cliente = self._players.get(count)
            cliente._client.send(self._players.get(count)._name+" "+self._menu["input_char"])
            input_char = cliente._client.recv(4096)

            hits = self.verify_word(input_char)
            cliente._score += hits
            self._players.set(count, cliente)

            if self._secret_word == self._word:
                cliente._client.send(self._players.get(count)._name+" "+self._menu["msg_win"])
                break
            else:
                cliente._client.send(self._secret_word)

            count += 1


hagman = Hangman('localhost', 8018)
hagman.start()
