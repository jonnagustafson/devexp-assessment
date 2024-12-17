from main.authentication import Authentication


def test_authentication():
    auth = Authentication()
    headers = auth.get_headers()
    headers["Content-Type"] = "application/json"

    assert headers == {
        "Content-Type": "application/json",
        "Authorization": "Bearer there-is-no-key"
    }
