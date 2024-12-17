from main.custom_exceptions import ClientError, ServerError, CustomError


class Messages:
    def __init__(self, client):
        self.client = client

    def send_message(
            self, sender_id: str, message: str, reciever_id: str
    ) -> dict:
        """
        Send a message.

        Args:
            sender_id (str): The sender of the message.
            message (str): The message to send.
            reciever_id (str): The id of the reciever.

        Returns:
            dict: The message details.
        """
        payload = {
            "from": sender_id,
            "content": message,
            "to": {
                "id": reciever_id
            }
        }
        try:
            return self.client.request("POST", "messages", data=payload)
        except ClientError as e:
            print(f"Failed to send message: {e.message}")
            raise
        except ServerError as e:
            print(f"Server error: {e.message}")
            raise
        except CustomError as e:
            print(f"Unexpected error: {e}")
            raise

    def get_message(self, message_id: str) -> dict:
        """
        Fetch details for a specific message.

        Args:
            message_id (str): The id of the message.

        Returns:
            dict: The message details.
        """
        try:
            return self.client.request("GET", f"messages/{message_id}")
        except ClientError as e:
            print(f"Failed to get message {message_id}: {e.message}")
            raise
        except ServerError as e:
            print(f"Server error: {e.message}")
            raise
        except CustomError as e:
            print(f"Unexpected error: {e}")
            raise

    def get_all_messages(self, page: int, limit: int = 100) -> dict:
        """
        Fetch details for all messages.

        Args:
            page (int): Page number to fetch.
            limit (int): Max number of messages per page. Default 100.

        Returns:
            dict: All available messages.
        """
        try:
            return self.client.request(
                "GET",
                "messages",
                params={"page": page, "limit": limit}
            )

        except ClientError as e:
            print(f"Failed to get messages: {e.message}")
            raise
        except ServerError as e:
            print(f"Server error: {e.message}")
            raise
        except CustomError as e:
            print(f"Unexpected error: {e}")
            raise
