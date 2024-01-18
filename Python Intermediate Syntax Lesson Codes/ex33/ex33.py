# 举例一
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


sum_result = add(5, '3')
product_result = multiply(sum_result, 2)
print(f"Sum: {sum_result}, Product: {product_result}")

# 举例二
# def process_order(order_id):
#     print(f"Processing order {order_id}")
#     verify_payment(order_id)
#     update_inventory(order_id)
#     print(f"Order {order_id} processed successfully.")


# def verify_payment(order_id):
#     print(f"Verifying payment for order {order_id}")
#     # 模拟支付验证
#     print("Payment verified.")


# def update_inventory(order_id):
#     print(f"Updating inventory for order {order_id}")
#     check_inventory()
#     # 模拟库存更新
#     print("Inventory updated.")


# def check_inventory():
#     print("Checking inventory levels.")
#     # 模拟库存检查
#     print("Inventory levels are sufficient.")


# order_ids = [101, 102, 103]
# for order_id in order_ids:
#     process_order(order_id)
