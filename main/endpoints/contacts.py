from main.custom_exceptions import ClientError, ServerError, CustomError


class Contacts:
    def __init__(self, client):
        self.client = client

    def get_contact(self, contact_id: str) -> dict:
        """
        Fetch details for a specific contact.

        Args:
            contact_id (str): The unique id of the contact.

        Returns:
            dict: The contact details.
        """

        try:
            return self.client.request("GET", f"contacts/{contact_id}")
        except ClientError as e:
            print(f"Failed to get contact {contact_id}: {e.message}")
            raise
        except ServerError as e:
            print(f"Server error: {e.message}")
            raise
        except CustomError as e:
            print(f"Unexpected error: {e}")
            raise

    def create_contact(self, name: str, phone: str) -> dict:
        """
        Create a new contact.

        Args:
            name (str): The name of the contact.
            phone (str): The phone of the contact.

        Returns:
            dict: The contact details.
        """
        payload = {
            "name": name,
            "phone": phone,
        }

        try:
            return self.client.request("POST", "contacts", data=payload)
        except ClientError as e:
            print(f"Failed to create contact: {e.message}")
            raise
        except ServerError as e:
            print(f"Server error: {e.message}")
            raise
        except CustomError as e:
            print(f"Unexpected error: {e}")
            raise

    def get_all_contacts(self, page: int, max: int = 10) -> dict:
        """
        Fetch details for all available contacts.

        Args:
            page (int): Page index.
            max (int): Maximum number of elements per page. Default 10.

        Returns:
            dict: All contacts and their details.

        """
        params = {
            "pageIndex": page,
            "max": max,
        }

        try:
            return self.client.request("GET", "contacts", params=params)
        except ClientError as e:
            print(f"Failed to get contacts: {e.message}")
            raise
        except ServerError as e:
            print(f"Server error: {e.message}")
            raise
        except CustomError as e:
            print(f"Unexpected error: {e}")
            raise

    def update_contact(self, contact_id: str, name: str, phone: str) -> dict:
        """
        Update details for a specific contact.

        Args:
            contact_id (str): The unique id of the contact.
            name (str): The name of the contact.
            phone (str): The phone of the contact.

        Returns:
            dict: The updated contact details.
        """
        payload = {
            "name": name,
            "phone": phone,
        }

        try:
            return self.client.request(
                "PATCH",
                f"contacts/{contact_id}",
                data=payload
            )
        except ClientError as e:
            print(f"Failed to update contact {contact_id}: {e.message}")
            raise
        except ServerError as e:
            print(f"Server error: {e.message}")
            raise
        except CustomError as e:
            print(f"Unexpected error: {e}")
            raise

    def delete_contact(self, contact_id: str):
        """
        Delete a specific contact.

        Args:
            contact_id (str): The unique id of the contact.
        """

        try:
            return self.client.request("DELETE", f"contacts/{contact_id}")
        except ClientError as e:
            print(f"Failed to delete contact {contact_id}: {e.message}")
            raise
        except ServerError as e:
            print(f"Server error: {e.message}")
            raise
        except CustomError as e:
            print(f"Unexpected error: {e}")
            raise
