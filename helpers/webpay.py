import requests
import random 
import json 
from django.conf import Settings

import orders



def createTransaction(user_id ):
    
    order = orders.models.Order.objects.get(user_id=user_id)

    buy_order = f"orden{order.order_number}"
    session_id = f"session{str(random.randrange(1000000,99999999))}"
    amount = order.order_total
    return_url = "http://localhost:8000/orders/payment_success"
    ruta = f"{Settings.BASE_URL}/orders/webpay_callback"
    endpoint = f"{Settings.WEBPAY_URL}"
    payload = {
        "buy_order": buy_order,
        "session_id": session_id,
        "amount": amount,
        "return_url": return_url,
    }

    headers = {
        "Tbk-Api-Key-Id": Settings.WEBPAY_KEY,
        "Tbk-Api-Key-Secret": Settings.WEBPAY_SECRET_KEY,
        "Content-Type": application/json,
    }

    response = requests.post(endpoint, data=json.dumps(payload), headers=headers)
    response = response.json()
    orders.objects.filter(user_id=user_id).update(payment_id=response["token"])
    route = f"{response["url"]}{response["token"]}"
    return response


