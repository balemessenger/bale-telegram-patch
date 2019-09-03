import json

import requests
import logging

payment_logger = logging.getLogger(__name__)


class BalePayment:

    def __init__(self, bot_token, logger=None):
        self.bot_token = bot_token
        self.logger = logger if logger else payment_logger

    def send_invoice_with_payment_id(self, chat_id, title, description, prices, additional_parameters, payload=None,
                                     photo_url=None):
        url = "https://tapi.bale.ai/{}/sendInvoice".format(self.bot_token)
        photo_url = ("https://dev.bale.ai/sites/default/files/styles/large/public/1397-12/404733-PCXHHU-813.jpg?itok"
                     "=3WLQI4eW ") if photo_url is None else photo_url
        payload = "payload" if payload is None else payload
        headers = {
            'content-type': "application/json",
        }
        body = {
            "chat_id": chat_id, "title": title, "description": description, "provider_token": "",
            "prices": prices, "additional_parameters": additional_parameters,
            "payload": payload, "photo_url": photo_url
        }
        response = requests.post(url, data=json.dumps(body), headers=headers)
        if response.status_code == 200:
            self.logger.info("successful payment request sent with payment id.")
        else:
            self.logger.error(
                "message is not send.\nResponse Code -> {}\nResponse body -> {}".format(response.status_code,
                                                                                        response.text))
