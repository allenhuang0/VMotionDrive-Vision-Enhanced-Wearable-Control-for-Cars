from websocket_server import WebsocketServer
import json
def new_client(client, server):
    print("New client connected")

def client_left(client, server):
    print("Client disconnected")

def message_received(client, server, message):
    data = json.loads(message)
    direction = data.get('direction', '')
    print(direction)

server = WebsocketServer(port=65432, host="0.0.0.0")
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()

