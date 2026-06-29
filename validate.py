import re

def validate_mobile(mobile):
    pattern = r"^09\d{9}$"
    if not re.match(pattern, mobile):
        raise ValueError("Mobile nimber is not valid. for example: '09123456789'")

