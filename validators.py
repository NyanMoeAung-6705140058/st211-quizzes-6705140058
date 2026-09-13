import re

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def validate_email(email):
    if not isinstance(email, str) or not EMAIL_RE.match(email):
        raise ValueError(f"invalid email: {email!r}")
    return True

def validate_age(age):
    if isinstance(age, bool) or not isinstance(age, int):
        raise TypeError(f"age must be an int, got {type(age).__name__}")
    if not (0 <= age <= 150):
        raise ValueError(f"age must be between 0 and 150, got {age}")
    return True
