# Servidor de teste

Navegar com o terminal na pasta raiz backend e executar o seguinte comando: "python debug.py --start"

# Permissões

- DASHBOARDS
- FINANCE
- REGISTERS
- USERS
- CLIENTS
- ROLES
- PERMISSIONS
- PRODUCTS
- SERVICES
- PRODUCTS_TYPE
- MEASURES_TYPES
- VEHICLES
- SUPPLIERS
- OS
- OC
- QUICK_BUDGET
- SCHEDULER
- HISTORIC
- HISTORIC_CLIENTS

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

---
# Testes

## Testes implementados

Aplicativos | Teste de URL | Teste de View | Teste de Modelo
----------- | :------------: | :-------------: | ---------------
**Client** | X | X
**Notification** | X | X
**Payment Method** | X | X
**Permissions** | X | X
**Product** | X | X
**Purchase Order** | X | X
**Roles** | X | X
**Services** | X | X
**Service Order** | X | X
**Status** | X | X
**Supplier** | X | X
**User** | X | X
**Vehicle** | X | X
