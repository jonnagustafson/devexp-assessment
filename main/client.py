import requests
from main.authentication import Authentication
from main.custom_exceptions import ClientError, ServerError, CustomError


class Client:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.auth = Authentication()

    def request(
        self, method: str, endpoint: str, params=None, data=None
    ) -> dict:
        url = f"{self.base_url}/{endpoint}"
        headers = self.auth.get_headers()
        headers["Content-Type"] = "application/json"

        try:
            response = requests.request(
                method, url, headers=headers, params=params, json=data
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            if 400 == response.status_code:
                raise ClientError(
                    response.status_code,
                    response.json().get("error", "Unknown client error"),
                    response
                )
            elif 401 <= response.status_code < 500:
                raise ClientError(
                    response.status_code,
                    response.json().get("message", "Unknown client error"),
                    response
                )
            elif 500 <= response.status_code < 600:
                raise ServerError(
                    response.status_code,
                    response.json().get("message", "Unknown server error"),
                    response
                )
        except requests.exceptions.RequestException as req_err:
            raise CustomError(f"Request failed: {req_err}")

        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return {"response": response, "status_code": response.status_code}
