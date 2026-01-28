from app import app


def test_uppercase():
    """
    Tests that a fully lowercase text input is returned fully capitalized.
    """
    app.testing = True
    client = app.test_client()
    response = client.get("/uppercase/hello")
    assert response.get_json() == "HeLLO"


def test_mixed_uppercase():
    """
    Tests that a partially lowercase text input is returned fully capitalized.
    """
    app.testing = True
    client = app.test_client()
    response = client.get("/uppercase/Hello")
    assert response.get_json() == "HELLO"


def test_lowercase():
    """
    Tests that a fully uppercase text input is returned fully lowercase.
    """
    app.testing = True
    client = app.test_client()
    response = client.get("/lowercase/HELLO")
    assert response.get_json() == "hello"


def test_mixed_lowercase():
    """
    Tests that a partially uppercase text input is returned fully lowercase.
    """
    app.testing = True
    client = app.test_client()
    response = client.get("/lowercase/HeLLO")
    assert response.get_json() == "hello"


def test_charcount():
    """
    Tests that a standard string's character count is properly returned
    """
    app.testing = True
    client = app.test_client()
    response = client.get("/charcount/hello")
    assert response.get_json() == 5


def test_charcount_ignores_spaces():
    """
    Tests that a string that includes spaces in it still returns the correct
    character count (spaces are not characters)
    """
    app.testing = True
    client = app.test_client()
    response = client.get("/charcount/h%20ello")
    assert response.get_json() == 5
