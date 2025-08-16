import data
from data import DataForOrder


def modify_order_body(key, value):
    body = DataForOrder.CREATE_ORDER_BODY.copy()
    body[key] = value
    return body