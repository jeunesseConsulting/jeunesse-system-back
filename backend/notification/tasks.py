import asyncio
import json
import websockets

from backend.settings import DEBUG

from service_order.services.service_order import ServiceOrderServices
from purchase_order.services.purchase_order import PurchaseOrderServices
from notification.services.notification import NotificationServices


if DEBUG:
    URL = 'ws://127.0.0.1:8000/ws/notification'
else:
    URL = 'wss://jeunesse-system-back.onrender.com/ws/notification'


async def send_expiring_today_service_order():
    orders = await ServiceOrderServices.service_orders_expiring_today()

    await asyncio.sleep(15)

    if orders and len(orders) > 0:
        for order in orders:
            message = {
                "message": f"A ordem de servico {order.id} esta vencendo hoje",
                "type": "serviceOrderExpiringToday",
                "orderId": order.id
            }

            async with websockets.connect(URL) as websocket:
                await websocket.send(json.dumps(message))
                await NotificationServices.create_valid_notification(
                    type = message['type'],
                    message = message['message'],
                    relationship_key = message["orderId"]
                )

async def send_expiring_tomorrow_service_order():
    orders = await ServiceOrderServices.service_orders_expiring_tomorrow()

    await asyncio.sleep(15)

    if orders and len(orders) > 0:
        for order in orders:
            message = {
                "message": f"A ordem de servico {order.id} vencera amanha",
                "type": "serviceOrderExpiringTomorrow",
                "orderId": order.id
            }

            async with websockets.connect(URL) as websocket:
                await websocket.send(json.dumps(message))
                await NotificationServices.create_valid_notification(
                    type = message['type'],
                    message = message['message'],
                    relationship_key = message["orderId"]
                )

async def send_expiring_today_purchase_order():
    orders = await PurchaseOrderServices.purchase_orders_expiring_today()

    if orders and len(orders) > 0:
        for order in orders:
            message = {
                "message": f"A ordem de compra {order.id} esta vencendo hoje",
                "type": "purchaseOrderExpiringToday",
                "orderId": order.id
            }

            async with websockets.connect(URL) as websocket:
                await websocket.send(json.dumps(message))
                await NotificationServices.create_valid_notification(
                    type = message['type'],
                    message = message['message'],
                    relationship_key = message["orderId"]
                )

async def send_expiring_tomorrow_purchase_order():
    orders = await PurchaseOrderServices.purchase_orders_expiring_tomorrow()

    if orders and len(orders) > 0:
        for order in orders:
            message = {
                "message": f"A ordem de compra {order.id} vencera amanha",
                "type": "purchaseOrderExpiringTomorrow",
                "orderId": order.id
            }

            async with websockets.connect(URL) as websocket:
                await websocket.send(json.dumps(message))
                await NotificationServices.create_valid_notification(
                    type = message['type'],
                    message = message['message'],
                    relationship_key = message["orderId"]
                )
