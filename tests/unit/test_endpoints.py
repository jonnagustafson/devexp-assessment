from unittest.mock import MagicMock
from main.endpoints import contacts, messages


def test_get_contact():
    client = MagicMock()
    contact = contacts.Contacts(client)
    client.request.return_value = {
        "id": "1", "name": "John Doe", "phone": "+46700000000"
    }

    response = contact.get_contact(contact_id="1")

    client.request.assert_called_once_with("GET", "contacts/1")
    assert isinstance(response, dict)


def test_get_contacts():
    client = MagicMock()
    contact = contacts.Contacts(client)
    client.request.return_value = {
        "contactsList": [
            {"id": "1", "name": "John Doe", "phone": "+46700000000"}
        ],
        "pageNumber": 1,
        "pageSize": 10
    }

    response = contact.get_all_contacts(page=1)

    client.request.assert_called_once_with(
        "GET",
        "contacts",
        params={"pageIndex": 1, "max": 10}
    )
    assert isinstance(response, dict)


def test_create_contact():
    client = MagicMock()
    contact = contacts.Contacts(client)
    client.request.return_value = {
        "id": "1", "name": "John Doe", "phone": "+46700000000"
    }

    response = contact.create_contact(name="John Doe", phone="+46700000000")

    client.request.assert_called_once_with(
        "POST",
        "contacts",
        data={"name": "John Doe", "phone": "+46700000000"}
    )
    assert isinstance(response, dict)


def test_delete_contact():
    client = MagicMock()
    contact = contacts.Contacts(client)
    client.request.return_value = None

    response = contact.delete_contact(contact_id="1")

    client.request.assert_called_once_with("DELETE", "contacts/1")
    assert response is None


def test_update_contact():
    client = MagicMock()
    contact = contacts.Contacts(client)
    client.request.return_value = {
        "id": "1", "name": "John Doe", "phone": "+46700000001"
    }

    response = contact.update_contact(
        contact_id="1",
        name="John Doe",
        phone="+46700000001"
    )

    client.request.assert_called_once_with(
        "PATCH",
        "contacts/1",
        data={"name": "John Doe", "phone": "+46700000001"}
    )
    assert isinstance(response, dict)


def test_get_all_messages():
    client = MagicMock()
    message = messages.Messages(client)
    client.request.return_value = {
        "messages": [
            {
                "from": "2",
                "content": "Hello world!",
                "id": "1",
                "status": "queued",
                "createdAt": "2024-12-15T20:45:17.155Z",
                "deliveredAt": "2024-12-15T20:45:17.155Z",
                "to": {
                    "name": "John Doe",
                    "phone": "+46700000000",
                    "id": "1"
                }
            }
        ],
        "page": 1,
        "quantityPerPage": 10
    }

    response = message.get_all_messages(page=1)

    client.request.assert_called_once_with(
        "GET",
        "messages",
        params={"page": 1, "limit": 100}
    )

    assert isinstance(response, dict)


def test_get_message():
    client = MagicMock()
    message = messages.Messages(client)
    client.request.return_value = {
        "from": "2",
        "content": "Hello world!",
        "id": "1",
        "status": "queued",
        "createdAt": "2024-12-15T20:49:01.489Z",
        "deliveredAt": "2024-12-15T20:49:01.490Z",
        "to": {
            "name": "John Doe",
            "phone": "+46700000000",
            "id": "1"
        }
    }

    response = message.get_message(message_id="1")

    client.request.assert_called_once_with("GET", "messages/1")

    assert isinstance(response, dict)


def test_send_message():
    client = MagicMock()
    message = messages.Messages(client)
    client.request.return_value = {
        "from": "2",
        "content": "Hello world!",
        "id": "1",
        "status": "queued",
        "createdAt": "2024-12-15T20:37:09.838Z",
        "deliveredAt": "2024-12-15T20:37:09.838Z",
        "to": {
            "name": "John Doe",
            "phone": "+46700000000",
            "id": "1"
        }
    }

    response = message.send_message(
        sender_id="2",
        message="Hello world!",
        reciever_id="1"
    )

    client.request.assert_called_once_with(
        "POST",
        "messages",
        data={
            "from": "2",
            "content": "Hello world!",
            "to": {"id": "1"}
        }
    )
    assert isinstance(response, dict)
