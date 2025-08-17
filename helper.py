from generators import generate_order_body


def modify_order_body(key, value):
    body = generate_order_body()
    body[key] = value
    return body