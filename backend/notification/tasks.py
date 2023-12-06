import asyncio
import json
import websockets

from backend.settings import DEBUG

if DEBUG:
    URL = 'ws://127.0.0.1:8000/ws/notification'
else:
    URL = 'wss://jeunesse-system-back.onrender.com/ws/notification'

async def send_test():
    message = {
        "message": f"service order test canceled",
        "type": "serviceOrderCanceled",
        "orderId": "test"
    }

    await asyncio.sleep(5)

    async with websockets.connect(URL) as websocket:
        await websocket.send(json.dumps(message))

async def schedule_send_test():
    while True:
        await send_test()
