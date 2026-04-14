import requests
import logging

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json", "Accept": "application/json"})

    def _send_request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        logging.info(f"Sending {method} request to {url}")
        
        if 'payload' in kwargs:
            kwargs['json'] = kwargs.pop('payload')
            
        response = self.session.request(method, url, **kwargs)
        logging.info(f"Received response: {response.status_code}")
        return response

    def get(self, endpoint, **kwargs):
        return self._send_request("GET", endpoint, **kwargs)

    def post(self, endpoint, payload=None, **kwargs):
        return self._send_request("POST", endpoint, payload=payload, **kwargs)

    def put(self, endpoint, payload=None, **kwargs):
        return self._send_request("PUT", endpoint, payload=payload, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._send_request("DELETE", endpoint, **kwargs)
