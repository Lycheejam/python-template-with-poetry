from src.hello_world import HelloWorld


def test_hello_world():
    hello = HelloWorld()
    assert hello.hello_world() == "Hello World!"
