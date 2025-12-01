def classify_region(sender: str, subject: str) -> str:
    sender = sender.lower()
    subject = subject.lower()

    if "north" in sender or "north" in subject:
        return "NORTH"
    if "south" in sender or "south" in subject:
        return "SOUTH"
    if "east" in sender or "east" in subject:
        return "EAST"
    if "west" in sender or "west" in subject:
        return "WEST"

    return "UNKNOWN"
