# JSON (англ. JavaScript Object Notation) — текстовый формат обмена данными, основанный на JavaScript.
# Формат легко читается людьми и может использоваться практически с любым языком программирования.
# За счёт своей лаконичности по сравнению с XML формат JSON может быть более подходящим для сериализации сложных структур

import json


str_json = """
{
  "ok": true,
  "result": {
    "count": 3,
    "orders": [
      {
        "id": 105096412,
        "orderId": "7120273",
        "userId": 19630,
        "pair": "del_usdt",
        "pairId": 24,
        "quantity": "250",
        "price": "0.0192",
        "executedPrice": "0",
        "fee": null,
        "orderCid": null,
        "executed": "0",
        "expires": null,
        "baseDecimals": 18,
        "quoteDecimals": 6,
        "timestamp": 1699630313,
        "status": "accepted",
        "side": "sell",
        "type": "limit",
        "createdAt": "2023-11-10T15:31:53.131Z",
        "updatedAt": "2023-11-10T15:31:53.131Z"
      },
      {
        "id": 105096426,
        "orderId": "7120274",
        "userId": 19630,
        "pair": "del_usdt",
        "pairId": 24,
        "quantity": "270",
        "price": "0.0195",
        "executedPrice": "0",
        "fee": null,
        "orderCid": null,
        "executed": "0",
        "expires": null,
        "baseDecimals": 18,
        "quoteDecimals": 6,
        "timestamp": 1699630324,
        "status": "accepted",
        "side": "sell",
        "type": "limit",
        "createdAt": "2023-11-10T15:32:04.956Z",
        "updatedAt": "2023-11-10T15:32:04.956Z"
      },
      {
        "id": 105096537,
        "orderId": "668214",
        "userId": 19630,
        "pair": "farms_usdt",
        "pairId": 44,
        "quantity": "100",
        "price": "0.049",
        "executedPrice": "0",
        "fee": null,
        "orderCid": null,
        "executed": "0",
        "expires": null,
        "baseDecimals": 8,
        "quoteDecimals": 6,
        "timestamp": 1699630381,
        "status": "accepted",
        "side": "buy",
        "type": "limit",
        "createdAt": "2023-11-10T15:33:01.842Z",
        "updatedAt": "2023-11-10T15:33:01.842Z"
      }
    ]
  }
}
"""

data = json.loads(str_json)
print(type(str_json))
print(type(data))
for item in data['result']['orders']:
    del item['pairId']
    item[('price')] = float(item['price'])
    item[('quantity')] = float(item['quantity'])
    print(item)

new_json = json.dumps(data, indent=2)
print(type(new_json))
print(new_json)

# Сохранить в файл
with open(r'files/data.json', mode='w') as file:
    json.dump(data, file, indent=2)

# Прочитать с Файла
with open(r'files/data.json', mode='r') as file:
    from_file_data = json.load(file)
print('--------------')
print(from_file_data)