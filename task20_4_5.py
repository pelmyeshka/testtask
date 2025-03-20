import json

with open("task20.json", "r") as my_file:
    orders = json.load(my_file)

max_price_order = None
max_price = 0
for order_num, order_data in orders.items():
    if order_data['price'] > max_price:
        max_price = order_data['price']
        max_price_order = order_num
print(f"Самый дорогой заказ: {max_price_order} цена: {max_price}")

max_quantity_order = None
max_quantity = 0
for order_num, order_data in orders.items():
    if order_data['quantity'] > max_quantity:
        max_quantity = order_data['quantity']
        max_quantity_order = order_num
print(f"Заказ с самым большим количеством товаров: {max_quantity_order} с количеством {max_quantity}")

order_counts = {}
for order_data in orders.values():
    date = order_data['date']
    if date in order_counts:
        order_counts[date] += 1
    else:
        order_counts[date] = 1

busiest_day = None
max_orders = 0
for date, count in order_counts.items():
    if count > max_orders:
        max_orders = count
        busiest_day = date
print(f"День с наибольшим количеством заказов: {busiest_day} с {max_orders} заказами")

user_order_counts = {}
for order_data in orders.values():
    user_id = order_data['user_id']
    if user_id in user_order_counts:
        user_order_counts[user_id] += 1
    else:
        user_order_counts[user_id] = 1

most_orders_user = None
max_user_orders = 0
for user_id, count in user_order_counts.items():
    if count > max_user_orders:
        max_user_orders = count
        most_orders_user = user_id
print(f"Пользователь с наибольшим количеством заказов: {most_orders_user} с {max_user_orders} заказами")

user_total_spent = {}
for order_data in orders.values():
    user_id = order_data['user_id']
    price = order_data['price']
    if user_id in user_total_spent:
        user_total_spent[user_id] += price
    else:
        user_total_spent[user_id] = price

top_spender = None
max_spent = 0
for user_id, total in user_total_spent.items():
    if total > max_spent:
        max_spent = total
        top_spender = user_id
print(f"Пользователь с наибольшей суммарной стоимостью заказов: {top_spender} с суммой {max_spent}")

total_orders = len(orders)
total_price = sum(order_data['price'] for order_data in orders.values())
average_order_price = total_price / total_orders
print(f"Средняя стоимость заказа: {average_order_price:.2f}")

total_quantity = sum(order_data['quantity'] for order_data in orders.values())
average_item_price = total_price / total_quantity
print(f"Средняя стоимость товара: {average_item_price:.2f}")