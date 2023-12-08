import asyncio
import json
import websockets

from backend.settings import DEBUG

from service_order.services.service_order import ServiceOrderServices


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

async def send_expiring_today_service_order():
    await asyncio.sleep(15)
    orders = await ServiceOrderServices.service_orders_expiring_today()

    if len(orders) > 0:
        for order in orders:
            message = {
                "message": f"A ordem de serviço {order.id} está vencendo hoje",
                "type": "serviceOrderExpiringToday",
                "orderId": order.id
            }

            async with websockets.connect(URL) as websocket:
                await websocket.send(json.dumps(message))

async def send_expiring_tomorrow_service_order():
    await asyncio.sleep(15)
    orders = await ServiceOrderServices.service_orders_expiring_tomorrow()

    if len(orders) > 0:
        for order in orders:
            message = {
                "message": f"A ordem de serviço {order.id} vencerá amanhã",
                "type": "serviceOrderExpiringTomorrow",
                "orderId": order.id
            }

            async with websockets.connect(URL) as websocket:
                await websocket.send(json.dumps(message))

async def send_expiring_today_purchase_order(order_id):
    message = {
        "message": f"A ordem de compra {order_id} está vencendo hoje",
        "type": "purchaseOrderExpiringToday",
        "orderId": order_id
    }

    async with websockets.connect(URL) as websocket:
        await websocket.send(json.dumps(message))

async def send_expiring_tomorrow_purchase_order(order_id):
    message = {
        "message": f"A ordem de compra {order_id} vencerá amanhã",
        "type": "purchaseOrderExpiringTomorrow",
        "orderId": order_id
    }

    async with websockets.connect(URL) as websocket:
        await websocket.send(json.dumps(message))
