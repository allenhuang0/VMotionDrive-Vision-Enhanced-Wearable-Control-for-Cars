#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:39:51 2023

@author: qianguanyu
"""


import websocket
import json


def initialize_socket(url):
    ws = websocket.WebSocket()
    ws.connect(url)
    return ws

def send_direction(ws, direction):
    if direction in ["right", "left","forward","backward"]:
        message = json.dumps({"direction": direction})
        ws.send(message)