from app.region_classifier import classify_region

def test_classify_region():
    assert classify_region("north@mail.com", "update") == "NORTH"
    assert classify_region("team@mail.com", "south report") == "SOUTH"
    assert classify_region("user@mail.com", "east msg") == "EAST"
    assert classify_region("westteam@mail.com", "info") == "WEST"
