def to_string(s):
    if isinstance(s, str) or not isinstance(s, bytes):
        return s
    else:
        return s.decode("utf-8", "ignore")
