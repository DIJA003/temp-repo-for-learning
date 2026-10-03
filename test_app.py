from app import hello

def test_default():
    assert hello() == "Hello, World!"

def test_name():
    assert hello("CI") == "Hello, CI!"
