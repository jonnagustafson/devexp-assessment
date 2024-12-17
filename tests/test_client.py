import pytest
from main.client import Client
from main.custom_exceptions import ClientError
from main.endpoints.contacts import Contacts
from main.endpoints.messages import Messages

BASE_URL = "http://localhost:3000"
client = Client(base_url=BASE_URL)


def test_delete_all_contacts():
    contacts = Contacts(client)
    all_contacts = contacts.get_all_contacts(1)
    for contact in all_contacts["contacts"]:
        contacts.delete_contact(contact.get("id"))


def test_client_requests():
    contacts = Contacts(client)

    contact_1 = contacts.create_contact("John Doe", "+46700000000")
    contact_1 = contacts.get_contact(contact_1.get("id"))
    assert contact_1.get("name") == "John Doe"
    assert contact_1.get("phone") == "+46700000000"

    contact_1 = contacts.update_contact(
        contact_1.get("id"), "John Doe", "+46700000001"
    )
    assert contact_1.get("name") == "John Doe"
    assert contact_1.get("phone") == "+46700000001"

    contact_2 = contacts.create_contact("John Doe 2", "+46760000000")
    all_contacts = contacts.get_all_contacts(1)
    assert len(all_contacts["contacts"]) == 2

    messages = Messages(client)

    message_1 = messages.send_message(
        contact_1.get("id"), "Hello!", contact_2.get("id")
    )
    message_1 = messages.get_message(message_1.get("id"))
    assert message_1.get("content") == "Hello!"

    all_messages = messages.get_all_messages(1)
    assert len(all_messages["messages"]) > 1

    for contact in all_contacts["contacts"]:
        contacts.delete_contact(contact.get("id"))


def test_input_error():
    contacts = Contacts(client)
    messages = Messages(client)

    with pytest.raises(ClientError):
        contacts.create_contact("John Doe", "1")
        contacts.get_contact(1)
        contacts.get_all_contacts(1)
        messages.send_message("1", "Hello!", "2")
        messages.get_message("1")
        messages.get_all_messages(1)
