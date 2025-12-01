from app.email_ingestor import clean_header

def test_clean_header():
    assert clean_header("Hello") == "Hello"
    assert clean_header(None) == ""
