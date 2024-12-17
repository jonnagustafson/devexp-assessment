from main.client import Client
from main.endpoints.messages import Messages
from main.endpoints.contacts import Contacts

BASE_URL = "http://localhost:3000"


class MySDK:
    def __init__(self):
        """
        Initialize the SDK.
        """
        self.client = Client(BASE_URL)

        # Initialize individual endpoints
        self.messages = Messages(self.client)
        self.contacts = Contacts(self.client)
