import requests


def call_api(url: str, headers: dict = None, body: dict = None, method: str = "GET"):

    if method.upper() == "GET":
        res = requests.get(url, headers=headers, data=body)
        if res.status_code < 200 and res.status_code >399:
            raise Exception(f"Error to call API {url}. Error: {res.text}")
        return res.json()
    raise Exception("Method not Allowed")