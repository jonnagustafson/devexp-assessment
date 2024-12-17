class Authentication:
    """
    Handles API authentication by managing the token.
    """

    def __init__(self):
        """
        Initialize with the provided API key.
        """
        self.api_key = "there-is-no-key"

    def get_headers(self) -> dict:
        """
        Returns the headers required for authentication.

        Returns:
            dict: Headers containing the authentication token.
        """
        return {"Authorization": f"Bearer {self.api_key}"}
