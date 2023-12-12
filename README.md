# Notificações

- _Link:_ <ws://jeunesse-system-back.onrender.com/ws/notification>

## Notificações sem jobs

##### Ordem de serviço cancelada

Enviado quando o status da ordem de serviço é alterado para "Cancelada"

**Json:**
```json
{
    "type": "send_order_notification",
    "message": "ordem de servico <order_id> cancelada",
    "notificationType": "serviceOrderCanceled",
    "orderId": order_id,
}
```
---
##### Ordem de serviço finalizada

Enviado quando o status da ordem de serviço é alterado para "Finalizada"

**Json:**
```json
{
    "type": "send_order_notification",
    "message": "ordem de servico <order_id> finalizada",
    "notificationType": "serviceOrderFinished",
    "orderId": order_id,
}
```

### Notificações com jobs (09:00hrs, 12:30hrs, 16:00hrs)

##### Ordem de serviço vencendo hoje

Enviado quando a ordem de serviço tem a data de vencimento para o dia atual

**Json:**
```json
{
    "type": "send_order_notification",
    "message": "ordem de servico <order_id> esta vencendo hoje",
    "notificationType": "serviceOrderExpiringToday",
    "orderId": order_id,
}
```
---
##### Ordem de serviço vencendo amanhã

Enviado quando a ordem de serviço tem a data de vencimento para amanhã

**Json:**
```json
{
    "type": "send_order_notification",
    "message": "ordem de servico <order_id> vencera amanha",
    "notificationType": "serviceOrderExpiringTomorrow",
    "orderId": order_id,
}
```
---
##### Ordem de compra vencendo hoje

Enviado quando a ordem de compra tem a data de vencimento para o dia atual

**Json:**
```json
{
    "type": "send_purchase_order_notification",
    "message": "ordem de compra <order_id> esta vencendo hoje",
    "notificationType": "purchaseOrderExpiringToday",
    "orderId": order_id,
}
```
---
##### Ordem de compra vencendo amanhã

Enviado quando a ordem de compra tem a data de vencimento para amanhã

**Json:**
```json
{
    "type": "send_purchase_order_notification",
    "message": "ordem de compra <order_id> vencera amanha",
    "notificationType": "purchaseOrderExpiringTomorrow",
    "orderId": order_id,
}
```
