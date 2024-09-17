import asyncio
import websockets

# Dictionary to store connected clients
clients = {}

async def register_client(websocket, client_name):
    clients[client_name] = websocket
    print("----------------------------------------------------")
    print(f"Client {client_name} registered.")
    print("----------------------------------------------------")

async def unregister_client(client_name):
    if client_name in clients:
        del clients[client_name]
        print("----------------------------------------------------")
        print(f"Client {client_name} unregistered.")
        print("----------------------------------------------------")

async def handle_message(message,sender_name):
    if ":" in message:
        target_client, data = message.split(":", 1)
        if target_client in clients:
            websocket = clients[target_client]
            await websocket.send(data)
            print(f"Message from {sender_name} sent to {target_client}: {data}")

        else:
            print(f"Target client {target_client} not found.")
    else:
        print(f"Invalid message format: {message}")

async def handler(websocket, path):
    # Register the client when it connects
    client_name = await websocket.recv()
    await register_client(websocket, client_name)

    try:
        # Continuously receive and handle messages from the client
        async for message in websocket:
            await handle_message(message,client_name)
    # finally:
    #     # Unregister the client when it disconnects
    #     await unregister_client(client_name)
    except websockets.exceptions.ConnectionClosed:
        await unregister_client(client_name)

# Start the WebSocket server
start_server = websockets.serve(handler, "0.0.0.0", 8000)
print("Started server.....")

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
